import pandas as pd
import altair as alt
import sqlite3
import StockList
import warnings
warnings.filterwarnings("ignore")
import streamlit as st

#---------------------------------
# Constants
PORTFOLIO_NAMES = [portfolio for portfolio in StockList.Portfolio.portfolio]
PORTFOLIOS = StockList.Portfolio.portfolio
STOCKS = StockList.Stocks.stock_dict
SECTORS = StockList.Stocks.sectors
portfolio_stock_names = []
sql_query_columns = []
sector_stats = {}
long_sector_stats = {}
df = {}
df_expected = pd.DataFrame()
df_5 = pd.DataFrame()
df_95 = pd.DataFrame()
df_nmbr_shares_expected = pd.DataFrame()
df_cone = pd.DataFrame()
INVEST_AMOUNT = 1000000
WEIGHT = 1.0
AMOUNT_PER_STOCK = 1
number_of_constituents = 1
cone_expected = pd.DataFrame()
cone_5 = pd.DataFrame()
cone_95 = pd.DataFrame()

# connect to database
conn = sqlite3.connect('mcpricepaths.db', timeout=30)
c = conn.cursor()

#here starts the UI
st.image('Logo_ALLindice_H-Blanc.gif', width=300)
st.title('Forecasting Portfolio Performance with Monte Carlo')
st.write(
    "From a given portfolio the prices for each constituent are simulated forward (in this example for one year). The NAV of the porfolio is then "
    "calculated on a daily basis. In order to understand how the portfolio develops the expected value "
    "and the boundaries where the value of the portfolio will most likely end up (95% confindence) are shown.")

# select portfolio name
portfolio = st.selectbox('Select Portfolio',PORTFOLIO_NAMES)

# retrieve individual stocks, which are the table names in database
portfolio_stock_names = PORTFOLIOS[portfolio]
sql_query_columns = [stock.split('.')[0] for stock in portfolio_stock_names]

# create statistics about sectors for display
for stock in portfolio_stock_names:
    sector = SECTORS[stock]
    if sector in sector_stats:
        sector_stats[sector] += 1
    else:
        sector_stats[sector] = 1

# retrieve the simulated prices for each stock as dataframe, stored in tables names by stock
for column in sql_query_columns:
    df[column] = pd.read_sql_query("SELECT * from "+ column, conn)
conn.close()

# build dataframes for expected_price and the percentiles
for stock in df:
      df_expected[stock] = df[stock]['expected_price']
      df_5[stock] = df[stock]['5percentile']
      df_95[stock] = df[stock]['95percentile']

# build equal weighted portfolios and calculate daily NAV
nmbr_of_constituents = len(sql_query_columns)
WEIGHT = 1 / nmbr_of_constituents
AMOUNT_PER_STOCK = INVEST_AMOUNT * WEIGHT

# calculate number of shares for amount invested, this can be expanded to add rebalancing periods
for stock in df:
    cone_expected[stock] = [int(AMOUNT_PER_STOCK / df_expected[stock].iloc[0])]
    cone_5[stock] = [int(AMOUNT_PER_STOCK / df_5[stock].iloc[0])]
    cone_95[stock] = [int(AMOUNT_PER_STOCK / df_95[stock].iloc[0])]

# calculate the portfolio value for each day
result_expected = df_expected.multiply(cone_expected.iloc[0], axis='columns')
result_5 = df_5.multiply(cone_5.iloc[0], axis='columns')
result_95 = df_95.multiply(cone_95.iloc[0], axis='columns')

# put all expected and percentile frame together by summing along rows for each df
# then create final df for display
result_expected['value'] = result_expected.sum(axis=1)
result_5['value'] = result_5.sum(axis=1)
result_95['value'] = result_95.sum(axis=1)

df_cone['expected'] = result_expected['value']
df_cone['5perc'] = result_5['value']
df_cone['95perc'] = result_95['value']

st.write('Forward Simulation of ', portfolio, ' portfolio with a 95% confidence intervall.')
st.line_chart(100 * df_cone / INVEST_AMOUNT) #normalise the plot to 100, horribly hardcoded

# create donut for sector breakdown
st.write('Sector breakdown for ',portfolio, ' portfolio.' )
long_sector_stats['Sector'] = []
long_sector_stats['Count'] = []
for sector in sector_stats:
    long_sector_stats['Sector'].append(sector)
    long_sector_stats['Count'].append(str(sector_stats[sector]))

source = pd.DataFrame.from_dict(long_sector_stats)
fig = alt.Chart(source).mark_arc().encode(
    theta="Count:Q",
    color="Sector:N"
)
st.altair_chart(fig, use_container_width=True)


# contains the top 50 stocks from S&P500

class Stocks():
    stock_dict = {
        'Microsoft Corp': 'MSFT.US',
        'Apple Inc.': 'AAPL.US',
        'Amazon.com Inc': 'AMZN.US',
        'Nvidia Corp': 'NVDA.US',
        'Alphabet Inc. Class A': 'GOOGL.US',
        'Meta Platforms, Inc. Class A': 'META.US',
        'Alphabet Inc. Class C': 'GOOG.US',
        'Tesla, Inc.': 'TSLA.US',
        'Unitedhealth Group Incorporated': 'UNH.US',
        'Jpmorgan Chase & Co.': 'JPM.US',
        'Broadcom Inc.': 'AVGO.US',
        'Eli Lilly & Co.': 'LLY.US',
        'Visa Inc.': 'V.US',
        'Exxon Mobil Corporation': 'XOM.US',
        'Johnson & Johnson': 'JNJ.US',
        'Procter & Gamble Company': 'PG.US',
        'Mastercard Incorporated': 'MA.US',
        'Home Depot, Inc.': 'HD.US',
        'Costco Wholesale Corp': 'COST.US',
        'Merck & Co., Inc.': 'MRK.US',
        'Abbvie Inc.': 'ABBV.US',
        'Adobe Inc.': 'ADBE.US',
        'Chevron Corporation': 'CVX.US',
        'Salesforce, Inc.': 'CRM.US',
        'Pepsico, Inc.': 'PEP.US',
        'Bank of America Corporation': 'BAC.US',
        'Coca-Cola Company': 'KO.US',
        'Walmart Inc.': 'WMT.US',
        'Advanced Micro Devices': 'AMD.US',
        'Accenture Plc': 'ACN.US',
        'Mcdonalds Corporation':'MCD.US',
        'Thermo Fisher Scientific, Inc.':'TMO.US',
        'Netflix Inc': 'NFLX.US',
        'Cisco Systems, Inc.': 'CSCO.US',
        'Intel Corp': 'INTC.US',
        'Linde Plc': 'LIN.US',
        'Abbott Laboratories': 'ABT.US',
        'Wells Fargo & Co.': 'WFC.US',
        'Comcast Corp': 'CMCSA.US',
        'Intuit Inc': 'INTU.US',
        'Pfizer Inc.': 'PFE.US',
        'The Walt Disney Company': 'DIS.US',
        'Oracle Corp': 'ORCL.US',
        'Verizon Communications': 'VZ.US',
        'Amgen Inc': 'AMGN.US',
        'Qualcomm Inc': 'QCOM.US',
        'Danaher Corporation': 'DHR.US',
        'Texas Instruments Incorporated': 'TXN.US',
        'Caterpillar Inc.': 'CAT.US'
        }
    sectors = {
        'MSFT.US': 'Technology',
        'AAPL.US': 'Technology',
        'AMZN.US': 'Consumer Cyclical',
        'NVDA.US': 'Technology',
        'GOOGL.US': 'Communication Services',
        'META.US': 'Communication Services',
        'GOOG.US': 'Communication Services',
        'TSLA.US': 'Consumer Cyclical',
        'UNH.US': 'Healthcare',
        'JPM.US': 'Financial Services',
        'AVGO.US': 'Technology',
        'LLY.US': 'Healthcare',
        'V.US': 'Financial Services',
        'XOM.US': 'Energy',
        'JNJ.US': 'Healthcare',
        'PG.US': 'Consumer Defensive',
        'MA.US': 'Financial Services',
        'HD.US': 'Consumer Cyclical',
        'COST.US': 'Consumer Defensive',
        'MRK.US': 'Healthcare',
        'ABBV.US': 'Healthcare',
        'ADBE.US': 'Technology',
        'CVX.US': 'Energy',
        'CRM.US': 'Technology',
        'PEP.US': 'Consumer Defensive',
        'BAC.US': 'Financial Services',
        'KO.US': 'Consumer Defensive',
        'WMT.US': 'Consumer Defensive',
        'AMD.US': 'Technology',
        'ACN.US': 'Technology',
        'MCD.US': 'Consumer Cyclical',
        'TMO.US': 'Healthcare',
        'NFLX.US': 'Communication Services',
        'CSCO.US': 'Technology',
        'INTC.US': 'Technology',
        'LIN.US': 'Basic Materials',
        'ABT.US': 'Healthcare',
        'WFC.US': 'Financial Services',
        'CMCSA.US': 'Communication Services',
        'INTU.US': 'Technology',
        'PFE.US': 'Healthcare',
        'DIS.US': 'Communication Services',
        'ORCL.US': 'Technology',
        'VZ.US': 'Communication Services',
        'AMGN.US': 'Healthcare',
        'QCOM.US': 'Technology',
        'DHR.US': 'Healthcare',
        'TXN.US': 'Technology',
        'CAT.US': 'Industrials'
    }
    industries = {
        'MSFT.US': 'Software - Infrastructure',
        'AAPL.US': 'Consumer Electronics',
        'AMZN.US': 'Internet Retail',
        'NVDA.US': 'Semiconductors',
        'GOOGL.US': 'Internet Content & Information',
        'META.US': 'Internet Content & Information',
        'GOOG.US': 'Internet Content & Information',
        'TSLA.US': 'Auto Manufacturers',
        'UNH.US': 'Healthcare Plans',
        'JPM.US': 'Banks - Diversified',
        'AVGO.US': 'Semiconductors',
        'LLY.US': 'Drug Manufacturers - General',
        'V.US': 'Credit Services',
        'XOM.US': 'Oil & Gas Integrated',
        'JNJ.US': 'Drug Manufacturers - General',
        'PG.US': 'Household & Personal Products',
        'MA.US': 'Credit Services',
        'HD.US': 'Home Improvement Retail',
        'COST.US': 'Discount Stores',
        'MRK.US': 'Drug Manufacturers - General',
        'ABBV.US': 'Drug Manufacturers - General',
        'ADBE.US': 'Software - Infrastructure',
        'CVX.US': 'Oil & Gas Integrated',
        'CRM.US': 'Software - Application',
        'PEP.US': 'Beverages - Non-Alcoholic',
        'BAC.US': 'Banks - Diversified',
        'KO.US': 'Beverages - Non-Alcoholic',
        'WMT.US': 'Discount Stores',
        'AMD.US': 'Semiconductors',
        'ACN.US': 'Information Technology Services',
        'MCD.US': 'Restaurants',
        'TMO.US': 'Diagnostics & Research',
        'NFLX.US': 'Entertainment',
        'CSCO.US': 'Communication Equipment',
        'INTC.US': 'Semiconductors',
        'LIN.US': 'Specialty Chemicals',
        'ABT.US': 'Medical Devices',
        'WFC.US': 'Banks - Diversified',
        'CMCSA.US': 'Telecom Services',
        'INTU.US': 'Software - Application',
        'PFE.US': 'Drug Manufacturers - General',
        'DIS.US': 'Entertainment',
        'ORCL.US': 'Software - Infrastructure',
        'VZ.US': 'Telecom Services',
        'AMGN.US': 'Drug Manufacturers - General',
        'QCOM.US': 'Semiconductors',
        'DHR.US': 'Diagnostics & Research',
        'TXN.US': 'Semiconductors',
        'CAT.US': 'Farm & Heavy Construction Machinery'
        }
class Portfolio():
    portfolio = {
        'Technology': ['MSFT.US', 'AAPL.US', 'NVDA.US', 'AVGO.US', 'ADBE.US', 'CRM.US', 'AMD.US', 'ACN.US', 'CSCO.US','INTC.US', 'INTU.US', 'ORCL.US', 'QCOM.US', 'TXN.US'],
        'Consumer Cyclical': ['AMZN.US', 'TSLA.US', 'HD.US', 'MCD.US'],
        'Communication Services': ['GOOGL.US', 'META.US', 'GOOG.US', 'NFLX.US', 'CMCSA.US', 'DIS.US', 'VZ.US'],
        'Healthcare': ['UNH.US', 'LLY.US', 'JNJ.US', 'MRK.US', 'ABBV.US', 'TMO.US', 'ABT.US', 'PFE.US', 'AMGN.US','DHR.US'],
        'Financial Services': ['JPM.US', 'V.US', 'MA.US', 'BAC.US', 'WFC.US'],
        'Consumer Defensive': ['PG.US', 'COST.US', 'PEP.US', 'KO.US', 'WMT.US'],
        'Global Growth and Tech Titans': ['AAPL.US', 'ACN.US', 'AMGN.US', 'WMT.US', 'META.US', 'LLY.US', 'CMCSA.US', 'MA.US', 'BAC.US', 'NFLX.US', 'DHR.US', 'HD.US', 'KO.US', 'COST.US', 'MCD.US', 'AMD.US', 'JPM.US', 'TXN.US', 'INTC.US', 'UNH.US', 'LIN.US', 'QCOM.US', 'INTU.US', 'VZ.US', 'V.US', 'PG.US', 'XOM.US', 'TSLA.US'],
        'Healthcare Giants and Global Leaders': ['ACN.US', 'CVX.US', 'AMZN.US', 'WMT.US', 'GOOG.US', 'META.US', 'CMCSA.US', 'CSCO.US', 'BAC.US', 'NFLX.US', 'DHR.US', 'HD.US', 'ORCL.US', 'KO.US', 'NVDA.US', 'COST.US', 'TMO.US', 'PEP.US', 'AVGO.US', 'AMD.US', 'WFC.US', 'ABBV.US', 'INTC.US', 'INTU.US', 'QCOM.US', 'MSFT.US', 'ADBE.US', 'CAT.US', 'CRM.US', 'PG.US', 'ABT.US', 'XOM.US', 'TSLA.US'],
        'Future-Proof Dividends': ['AAPL.US', 'MRK.US', 'ACN.US', 'AMZN.US', 'AMGN.US', 'WMT.US', 'DIS.US', 'XOM.US', 'META.US', 'LLY.US', 'CMCSA.US', 'NFLX.US', 'DHR.US', 'HD.US', 'ORCL.US', 'NVDA.US', 'MCD.US', 'PEP.US', 'AVGO.US', 'AMD.US', 'GOOGL.US', 'WFC.US', 'ABT.US', 'TXN.US', 'INTC.US', 'INTU.US', 'LIN.US', 'QCOM.US', 'MSFT.US', 'ADBE.US', 'CAT.US', 'V.US', 'PG.US', 'COST.US', 'TSLA.US'],
        'Top Tech Stocks': ['AAPL.US', 'MRK.US', 'CVX.US', 'AMGN.US', 'AMZN.US', 'JNJ.US', 'META.US', 'DIS.US', 'LLY.US', 'CSCO.US', 'MA.US', 'BAC.US', 'NFLX.US', 'ORCL.US', 'KO.US', 'COST.US', 'TMO.US', 'MCD.US', 'PEP.US', 'AVGO.US', 'AMD.US', 'GOOGL.US', 'WFC.US', 'UNH.US', 'LIN.US', 'INTU.US', 'QCOM.US', 'VZ.US', 'V.US', 'PG.US', 'ABT.US', 'XOM.US', 'TSLA.US'],
        'Defensive Champions': ['MRK.US', 'ACN.US', 'CVX.US', 'PFE.US', 'DIS.US', 'LLY.US', 'CMCSA.US', 'MA.US', 'CSCO.US', 'NFLX.US', 'DHR.US', 'HD.US', 'ORCL.US', 'COST.US', 'TMO.US', 'PEP.US', 'ABBV.US', 'JPM.US', 'TXN.US', 'INTC.US', 'LIN.US', 'MSFT.US', 'ADBE.US', 'CAT.US', 'PG.US', 'ABT.US', 'XOM.US'],
        'High-Growth Technology': ['ACN.US', 'MRK.US', 'AMGN.US', 'AMZN.US', 'WMT.US', 'PFE.US', 'JNJ.US', 'LLY.US', 'CSCO.US', 'MA.US', 'CMCSA.US', 'DHR.US', 'ORCL.US', 'NVDA.US', 'MCD.US', 'AVGO.US', 'AMD.US', 'ABBV.US', 'JPM.US', 'INTC.US', 'INTU.US', 'QCOM.US', 'MSFT.US', 'ADBE.US', 'V.US', 'CRM.US', 'ABT.US', 'XOM.US'],
        'Value Hybrid and Healthcare Giants': ['AAPL.US', 'MRK.US', 'CVX.US', 'AMGN.US', 'WMT.US', 'GOOG.US', 'PFE.US', 'JNJ.US', 'META.US', 'LLY.US', 'CSCO.US', 'MA.US', 'BAC.US', 'NFLX.US', 'HD.US', 'NVDA.US', 'TMO.US', 'MCD.US', 'PEP.US', 'AVGO.US', 'GOOGL.US', 'ABBV.US', 'JPM.US', 'UNH.US', 'LIN.US', 'QCOM.US', 'INTU.US', 'VZ.US', 'MSFT.US', 'ADBE.US', 'CAT.US', 'V.US', 'CRM.US', 'TSLA.US'],
        'Top-Tier Businesses Across Sectors': ['MRK.US', 'ACN.US', 'AMZN.US', 'AMGN.US', 'GOOG.US', 'PFE.US', 'XOM.US', 'LLY.US', 'CMCSA.US', 'MA.US', 'DHR.US', 'ORCL.US', 'NVDA.US', 'TMO.US', 'MCD.US', 'PEP.US', 'AVGO.US', 'AMD.US', 'JPM.US', 'TXN.US', 'INTC.US', 'UNH.US', 'LIN.US', 'INTU.US', 'VZ.US', 'ADBE.US', 'V.US', 'CRM.US', 'ABT.US', 'COST.US', 'GOOGL.US'],
        'Technology Portfolio': ['MRK.US', 'CVX.US', 'AMGN.US', 'GOOG.US', 'PFE.US', 'META.US', 'DIS.US', 'CSCO.US', 'BAC.US', 'NFLX.US', 'DHR.US', 'ORCL.US', 'NVDA.US', 'COST.US', 'TMO.US', 'PEP.US', 'AVGO.US', 'AMD.US', 'GOOGL.US', 'WFC.US', 'ABBV.US', 'JPM.US', 'TXN.US', 'INTC.US', 'UNH.US', 'INTU.US', 'VZ.US', 'MSFT.US', 'ADBE.US', 'V.US', 'CRM.US', 'ABT.US', 'XOM.US', 'TSLA.US'],
        'Disruptors': ['AAPL.US', 'ACN.US', 'CVX.US', 'AMGN.US', 'PFE.US', 'JNJ.US', 'LLY.US', 'MA.US', 'CSCO.US', 'BAC.US', 'HD.US', 'ORCL.US', 'NVDA.US', 'TMO.US', 'MCD.US', 'PEP.US', 'AVGO.US', 'GOOGL.US', 'ABBV.US', 'WFC.US', 'INTC.US', 'UNH.US', 'LIN.US', 'MSFT.US', 'ADBE.US', 'CAT.US', 'CRM.US', 'PG.US', 'ABT.US', 'XOM.US', 'TSLA.US'],
        'Healthcare Giants': ['AAPL.US', 'ACN.US', 'CVX.US', 'WMT.US', 'GOOG.US', 'DIS.US', 'LLY.US', 'CSCO.US', 'MA.US', 'NFLX.US', 'HD.US', 'ORCL.US', 'NVDA.US', 'MCD.US', 'PEP.US', 'AVGO.US', 'WFC.US', 'ABBV.US', 'JPM.US', 'TXN.US', 'INTC.US', 'LIN.US', 'VZ.US', 'MSFT.US', 'V.US', 'PG.US', 'ABT.US', 'COST.US', 'GOOGL.US'],
        'Consumer Staples': ['MRK.US', 'CVX.US', 'AMZN.US', 'AMGN.US', 'WMT.US', 'JNJ.US', 'DIS.US', 'META.US', 'LLY.US', 'CSCO.US', 'CMCSA.US', 'MA.US', 'NFLX.US', 'ORCL.US', 'KO.US', 'TMO.US', 'MCD.US', 'AVGO.US', 'AMD.US', 'WFC.US', 'ABBV.US', 'JPM.US', 'TXN.US', 'INTC.US', 'UNH.US', 'LIN.US', 'QCOM.US', 'VZ.US', 'MSFT.US', 'ADBE.US', 'CRM.US', 'COST.US', 'GOOGL.US'],
        'Healthcare Giants, Top Tech Stocks,and Disruptors': ['AAPL.US', 'ACN.US', 'CVX.US', 'JNJ.US', 'META.US', 'DIS.US', 'LLY.US', 'CMCSA.US', 'MA.US', 'BAC.US', 'NFLX.US', 'HD.US', 'ORCL.US', 'KO.US', 'NVDA.US', 'COST.US', 'TMO.US', 'MCD.US', 'PEP.US', 'ABBV.US', 'WFC.US', 'JPM.US', 'INTC.US', 'UNH.US', 'LIN.US', 'INTU.US', 'CAT.US', 'V.US', 'XOM.US', 'TSLA.US'],
        'Technology Portfolio and Healthcare Giants': ['ACN.US', 'MRK.US', 'CVX.US', 'AMZN.US', 'GOOG.US', 'JNJ.US', 'META.US', 'DIS.US', 'MA.US', 'CSCO.US', 'CMCSA.US', 'NFLX.US', 'DHR.US', 'NVDA.US', 'MCD.US', 'PEP.US', 'AMD.US', 'WFC.US', 'JPM.US', 'TXN.US', 'INTC.US', 'UNH.US', 'LIN.US', 'QCOM.US', 'MSFT.US', 'TSLA.US', 'CAT.US', 'V.US', 'CRM.US', 'PG.US', 'COST.US', 'GOOGL.US'],
        'Dividend Aristocrats': ['AAPL.US', 'MRK.US', 'ACN.US', 'CVX.US', 'AMGN.US', 'GOOG.US', 'PFE.US', 'DIS.US', 'META.US', 'CMCSA.US', 'CSCO.US', 'DHR.US', 'NVDA.US', 'MCD.US', 'PEP.US', 'AVGO.US', 'WFC.US', 'ABBV.US', 'JPM.US', 'TXN.US', 'INTC.US', 'INTU.US', 'UNH.US', 'VZ.US', 'MSFT.US', 'V.US', 'CRM.US', 'ABT.US', 'XOM.US', 'TSLA.US'],
        'Blue-Chip Champions and Defensive Champions': ['AAPL.US', 'MRK.US', 'ACN.US', 'AMGN.US', 'WMT.US', 'GOOG.US', 'PFE.US', 'META.US', 'DIS.US', 'LLY.US', 'CSCO.US', 'CMCSA.US', 'MA.US', 'DHR.US', 'HD.US', 'ORCL.US', 'KO.US', 'NVDA.US', 'COST.US', 'MCD.US', 'PEP.US', 'WFC.US', 'ABBV.US', 'JPM.US', 'TXN.US', 'UNH.US', 'LIN.US', 'VZ.US', 'CAT.US', 'ADBE.US', 'V.US', 'CRM.US', 'PG.US', 'XOM.US'],
        'Income Portfolio with Global Reach': ['AAPL.US', 'ACN.US', 'AMZN.US', 'AMGN.US', 'GOOG.US', 'PFE.US', 'JNJ.US', 'META.US', 'DIS.US', 'MA.US', 'CMCSA.US', 'BAC.US', 'NFLX.US', 'DHR.US', 'HD.US', 'NVDA.US', 'PEP.US', 'AVGO.US', 'AMD.US', 'ABBV.US', 'TXN.US', 'INTC.US', 'INTU.US', 'LIN.US', 'MSFT.US', 'CAT.US', 'ADBE.US', 'CRM.US', 'PG.US', 'ABT.US', 'COST.US', 'GOOGL.US'],
        'Value Hybrid': ['AAPL.US', 'ACN.US', 'CVX.US', 'AMZN.US', 'AMGN.US', 'GOOG.US', 'JNJ.US', 'DIS.US', 'MA.US', 'CMCSA.US', 'BAC.US', 'HD.US', 'ORCL.US', 'KO.US', 'COST.US', 'PEP.US', 'AVGO.US', 'AMD.US', 'GOOGL.US', 'ABBV.US', 'JPM.US', 'TXN.US', 'UNH.US', 'LIN.US', 'INTU.US', 'MSFT.US', 'V.US', 'CRM.US', 'ABT.US', 'XOM.US', 'TSLA.US'],
        'High-Growth Technology and Top Tech Stocks': ['MRK.US', 'ACN.US', 'CVX.US', 'AMGN.US', 'WMT.US', 'GOOG.US', 'PFE.US', 'JNJ.US', 'XOM.US', 'MA.US', 'BAC.US', 'HD.US', 'ORCL.US', 'KO.US', 'MCD.US', 'PEP.US', 'WFC.US', 'ABT.US', 'JPM.US', 'TXN.US', 'INTC.US', 'LIN.US', 'QCOM.US', 'VZ.US', 'MSFT.US', 'CAT.US', 'V.US', 'PG.US', 'COST.US'],
        'Disruptors and Future-Proof Dividends': ['AAPL.US', 'ACN.US', 'CVX.US', 'AMZN.US', 'AMGN.US', 'WMT.US', 'GOOG.US', 'PFE.US', 'JNJ.US', 'DIS.US', 'LLY.US', 'MA.US', 'BAC.US', 'DHR.US', 'ORCL.US', 'KO.US', 'NVDA.US', 'TMO.US', 'AMD.US', 'WFC.US', 'TXN.US', 'INTU.US', 'UNH.US', 'QCOM.US', 'VZ.US', 'MSFT.US', 'TSLA.US', 'ADBE.US', 'CAT.US', 'V.US', 'PG.US', 'GOOGL.US'],
                 }
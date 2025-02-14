import pandas as pd

# URL of the Wikipedia page
url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

# Read HTML tables from the page
tables = pd.read_html(url)

# The first table on the page contains the S&P 500 companies
sp500_table = tables[0]

# Extract the company names (the first column)
# company_names = sp500_table['Symbol'].tolist()
df = sp500_table[['Symbol','Security','GICS Sector','GICS Sub-Industry']].values.tolist()
# Print the company names
print(df)
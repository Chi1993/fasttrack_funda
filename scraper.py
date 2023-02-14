from funda_scraper import FundaScraper

scraper = FundaScraper(area="amsterdam", want_to="rent", find_past=False)
df = scraper.run()
df.head()

print(df)

from app.ingestion.scrapper import scrape_url

url = "https://www.tn.gov.in/scheme_beneficiary_list.php?id=MTk="
text = scrape_url(url)

print(text[:1000])
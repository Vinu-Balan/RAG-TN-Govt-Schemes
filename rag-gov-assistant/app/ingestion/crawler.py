import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


def crawl_website(base_url, max_pages=600):
    visited = set()
    to_visit = [base_url]

    domain = urlparse(base_url).netloc
    pages = []

    while to_visit and len(visited) < max_pages:
        url = to_visit.pop(0)

        if url in visited:
            continue

        try:
            res = requests.get(url, timeout=5)
            soup = BeautifulSoup(res.text, "html.parser")

            visited.add(url)
            print(f"Crawled: {url}")

            # Extract useful text (only meaningful content)
            main_content = ""
            for tag in soup.find_all(["p", "li"]):
                text = tag.get_text(strip=True)
                if len(text) > 50:
                    main_content += text + "\n"

            if len(main_content) > 200:
                pages.append((url, main_content))

            # Extract links
            for link in soup.find_all("a", href=True):
                full_url = urljoin(base_url, link["href"])
                parsed = urlparse(full_url)

                if parsed.netloc != domain:
                    continue

                # Skip unwanted pages
                if any(bad in full_url.lower() for bad in [
                    "search", "login", "contact", "about", "policy"
                ]):
                    continue

                # Skip files
                if any(ext in full_url for ext in [".pdf", ".jpg", ".png", ".zip"]):
                    continue

                # Focus only relevant pages
                if any(keyword in full_url.lower() for keyword in [
                    "scheme", "service", "details", "welfare", "benefit"
                ]):
                    to_visit.append(full_url)

        except Exception as e:
            print(f"Error: {url} → {e}")

    print(f"\nTotal pages collected: {len(pages)}")
    return pages
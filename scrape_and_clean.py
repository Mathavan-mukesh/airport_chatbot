from bs4 import BeautifulSoup
import requests
import re

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    texts = [p.get_text(strip=True) for p in soup.find_all("p")]
    cleaned = clean_text(" ".join(texts))
    return cleaned

def clean_text(text):
    text = re.sub(r"[^\w\s.,!?]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def main():
    urls = [
        "https://www.changiairport.com/",
        "https://www.jewelchangiairport.com/"
    ]
    for i, url in enumerate(urls):
        content = scrape_website(url)
        with open(f"data/site_content_{i+1}.txt", "w", encoding="utf-8") as f:
            f.write(content)

if __name__ == "__main__":
    main()
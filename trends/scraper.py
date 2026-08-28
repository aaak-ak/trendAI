import requests
from bs4 import BeautifulSoup
from trends.models import TrendCandidate

def scrape_aliexpress():
    url = "https://www.aliexpress.com/..."  # тут реальний URL категорії
    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(r.text, "html.parser")

    products = []
    for item in soup.select(".product-card"):  # приклад селектора
        title = item.select_one(".product-title").get_text(strip=True)
        score = 80  # поки що тестове значення
        products.append({"title": title, "trend_score": score})

    return products

def save_candidates():
    products = scrape_aliexpress()
    for p in products:
        TrendCandidate.objects.create(
            title=p["title"],
            trend_score=p["trend_score"],
            source="aliexpress"
        )
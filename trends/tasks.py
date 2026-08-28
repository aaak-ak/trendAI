from celery import shared_task
from trends.scraper import scrape_aliexpress
from trends.models import TrendCandidate

@shared_task
def update_trends():
    products = scrape_aliexpress()
    for p in products:
        TrendCandidate.objects.create(
            title=p["title"],
            trend_score=p["trend_score"],
            source="aliexpress"
        )

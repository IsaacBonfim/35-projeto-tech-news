from datetime import datetime
from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}

    found_news = search_news(query)

    return [
        (news["title"], news["url"])
        for news in found_news
    ]


# Requisito 7
def search_by_date(date):
    try:
        query_date = datetime.fromisoformat(date).strftime("%d/%m/%Y")

        found_news = search_news({"timestamp": query_date})

        return [
            (news["title"], news["url"])
            for news in found_news
        ]

    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""

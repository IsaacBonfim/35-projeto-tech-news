from tech_news.database import find_news


# Requisito 10
def top_5_news():
    news_list = find_news()

    sorted_news = sorted(
        news_list, key=lambda news: news["comments_count"], reverse=True
    )

    return [
        (news["title"], news["url"])
        for news in sorted_news
        if sorted_news.index(news) < 5
    ]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""

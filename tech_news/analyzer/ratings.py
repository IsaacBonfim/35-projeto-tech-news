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
    news_list = find_news()

    categories_dict = {news["category"]: 0 for news in news_list}

    sorted_categories = sorted(categories_dict, key=lambda category: category)

    categories = {category: 0 for category in sorted_categories}

    for news in news_list:
        categories[news["category"]] += 1

    categories_list = sorted(
        categories.items(), key=lambda category: (category[1]), reverse=True
    )

    return [
        category
        for category, qnt in categories_list
        if categories_list.index((category, qnt)) < 5
    ]

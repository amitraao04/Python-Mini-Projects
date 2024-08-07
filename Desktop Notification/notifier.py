import time
from plyer import notification
from topnews import topStories

print("FETCHING NEWS ITEMS")

news_items = topStories()

print(f"Fetched {len(news_items)} headlines ")

for news_item in news_items:
    title = news_item.get('title')
    description = news_item.get('description')

    if isinstance(title,bytes):
        title = title.decode('utf-8')

    if isinstance(description,bytes):
        description = description.decode('utf-8')

    notification.notify(
        title=title,
        message=description,
        app_name="News - Notifier",
        timeout=10
    )

    time.sleep(15)
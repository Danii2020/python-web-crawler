from bs4 import BeautifulSoup
import requests
import pandas as pd


class Crawler:
    """    
    Crawler class use the YCombinator news URL
    to scrap the title, order number, comments,
    and points of the first 30 entries.
    """

    def __init__(self, url="https://news.ycombinator.com/"):
        self.url = url
        self._response = requests.get(url)
        self._soup = BeautifulSoup(self._response.content, 'lxml')

    def _crawl(self, tag, items_list):
        for item in self._soup.find_all('tr'):
            if item.select(tag):
                if len(item.select(tag)) == 1:
                    entrie = item.select(tag)[0].get_text()
                    try:
                        if tag == '.score':
                            entrie = entrie.split()[0]
                            entrie = int(entrie)
                        elif tag == '.rank':
                            entrie = entrie.replace('.', '').strip()
                            entrie = int(entrie)
                    except ValueError:
                        entrie = 0
                    items_list.append(entrie)
        return items_list

    def _crawl_order_number(self):
        order_numbers = []
        return self._crawl('.rank', order_numbers)

    def _crawl_title(self):
        news_titles = []
        return self._crawl('.titlelink', news_titles)

    def _crawl_points(self):
        news_points = []
        return self._crawl('.score', news_points)

    def _crawl_comments(self):
        news_comments = []
        for item in self._soup.find_all('tr'):
            if item.select('.score'):
                if len(item.select('.score')) == 1:
                    comments = item.find_all('a')[3].get_text()
                    comments = comments.split()[0]
                    try:
                        comments = int(comments)
                    except ValueError:
                        comments = 0
                    news_comments.append(comments)

        return news_comments

    def get_entries(self):
        news_orders = self._crawl_order_number()
        news_titles = self._crawl_title()
        news_points = self._crawl_points()
        news_comments = self._crawl_comments()
        entries_df = pd.DataFrame(
            {
                "Order": [order for order in news_orders],
                "Title": [title for title in news_titles],
                "Points": [point for point in news_points + [0]],
                "Comments": [int(comment) for comment in news_comments + [0]],
            }
        )
        return entries_df

    def filter_more_five_words(self, df):
        sorted_df = df.sort_values('Comments', ascending=True)
        count_words = sorted_df['Title'].str.split().str.len()
        five_words_df = sorted_df[count_words > 5]
        return five_words_df

    def filter_less_five_words(self, df):
        sorted_df = df.sort_values('Points', ascending=True)
        count_words = sorted_df['Title'].str.split().str.len()
        five_words_df = sorted_df[count_words <= 5]
        return five_words_df


if __name__ == '__main__':
    crawler = Crawler()
    entries_df = crawler .get_entries()
    print(crawler.get_entries())
    print("-----More than five words-------\n")
    print(crawler.filter_more_five_words(entries_df), "\n")
    print("-----Less equals than five words-------\n")
    print(crawler.filter_less_five_words(entries_df), "\n")

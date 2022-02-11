from bs4 import BeautifulSoup
import requests

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
                entrie = item.select(tag)[0].get_text()
                items_list.append(entrie)
        return items_list
    
    def crawl_order_number(self):
        order_numbers = []
        return self._crawl('.rank', order_numbers)    


    def crawl_title(self):
        news_titles = []
        return self._crawl('.titlelink', news_titles)

    def crawl_points(self):
        news_points = []
        return self._crawl('.score', news_points)


    def crawl_points(self):
        news_comments = []
        for item in self._soup.find_all('tr'):
            if item.select('.score'):
                comments = item.find_all('a')[3].get_text()
                news_commentst.append(comments)
        return news_comments




if __name__ == '__main__':
    news = {}
    crawler = Crawler()
    orders_numbers = crawler.crawl_order_number()
    news_titles = crawler.crawl_title()
    for (order_number, new_title) in zip(orders_numbers, news_titles):
        news[order_number] = new_title
    print(news)
    
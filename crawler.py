# This is the Web Crawler Class.
# In this class I define the constructor,
# the methods for request the YCombinator Hacker News
# site, parse the order number, title, points and comments
# from the first 30 entries.

# import BeautifulSoup to scrape the HTML elements.
from bs4 import BeautifulSoup
import requests  # import requests to make a request to the page.
# import pandas to represent the retrieve data in a better way.
import pandas as pd


class Crawler:
    """   
    Crawler class use the YCombinator news URL
    to scrap the title, order number, comments,
    and points of the first 30 entries.
    """
    # creation of the constructor class with the URL with a default value.

    def __init__(self, url="https://news.ycombinator.com/"):
        self.url = url

    # creation of the request URL method to handle the request with of the page.
    def _request_url(self):
        try:
            # make a GET request to the page and
            # return the response
            self._response = requests.get(self.url)
            # initialize the BeautifulSoup class with the
            # content response like a lxml structure (tree sctructure).
            self._soup = BeautifulSoup(
                self._response.content, 'lxml')
        # handle the request errors.
        except requests.exceptions.HTTPError:
            print("Sorry, it was an error with the request, try again.")
        return self._soup  # return the BeautifulSoup object.

    # creation of the parse method to find the needed items.
    # this method needs the tag and the items list as parameters
    # depending what it needs to find.
    def _parse(self, tag, items_list):
        # call the request_url() methos to return the
        # BeautifulSoup object (the lxml structure of the page).
        parser = self._request_url()
        # iteration all the tr tags from the page structrue
        # (tr tag defines the raws in a HTML table).
        for item in parser.find_all('tr'):
            # if the item has the desire tag inside the class parameter
            # then you can find the desire element.
            if item.select(tag):
                # this if statement is for check the length of the
                # item, due to the first item has 30 elements and
                # this could create duplicates later.
                if len(item.select(tag)) == 1:
                    # as the item is a python list, you can select
                    # the text of the desire tag located in the
                    # first index (the fist and unique element in the list).
                    entry_item = item.select(tag)[0].get_text()
                    # handle the item of entry if the points
                    # is not a integer number.
                    try:
                        # these if statements are to check the needed tags
                        if tag == '.score':  # this is the points tag.
                            # these two lines are to split the returned elements
                            # to get just the number and then cast it into an
                            # integer.
                            entry_item = entry_item.split()[0]
                            entry_item = int(entry_item)
                        elif tag == '.rank':  # this is the order number tag.
                            # these two lines are to replace the returned elements
                            # with an empty char because the element is like "1.",
                            # and I need just the number.
                            entry_item = entry_item.replace('.', '').strip()
                            entry_item = int(entry_item)
                    except ValueError:
                        # if the above items of the entries are strings
                        # put the variable in 0.
                        entry_item = 0
                    # then, append the items in the parameter list,
                    # note that the title tag is not explicitly here
                    # because this is a text type by default.
                    items_list.append(entry_item)
        return items_list  # finally return the list.

    # creation of the parse order number method.
    def _parse_order_number(self):
        # declare the order numbers list.
        order_numbers = []
        # call and return the order numbers list
        # with the parse method using the ".rank" tag
        # of the order number in the lxml structure.
        return self._parse('.rank', order_numbers)

    # creation of the parse title method.
    def _parse_title(self):
        # declare the titles list.
        news_titles = []
        # call and return the titles list
        # with the parse method using the ".titlelink" tag
        # of the title in the lxml structure.
        return self._parse('.titlelink', news_titles)

    # creation of the parse points method.
    def _parse_points(self):
        # declare the points list.
        news_points = []
        # call and return the points list
        # with the parse method using the ".score" tag
        # of the points in the lxml structure.
        return self._parse('.score', news_points)

    # creation of the parse comments method.
    # this method is similar to the parse method,
    # but this is a different method due to a different
    # structure of the comments inside the lxml structure.
    def _parse_comments(self):
        news_comments = []
        for item in self._soup.find_all('tr'):
            if item.select('.score'):
                if len(item.select('.score')) == 1:
                    # this line finds all the 'a' tags because
                    # the comments are in this tag, but the comments
                    # are in the 3rd index of the item list.
                    comments = item.find_all('a')[3].get_text()
                    # this line splits the item into a list and
                    # retrieve the first element (the number of comments).
                    comments = comments.split()[0]
                    try:
                        comments = int(comments)
                    except ValueError:
                        comments = 0
                    news_comments.append(comments)
        return news_comments

    # creation of the get entries method.
    def get_entries(self):
        # call all the above methods to return the order number,
        # title, points and comments.
        news_orders = self._parse_order_number()
        news_titles = self._parse_title()
        news_points = self._parse_points()
        news_comments = self._parse_comments()
        # create a Pandas DataFrame with the data retrieve above.
        # this df have 4 columns (the order, title, points and comments),
        # and their respective values inside the lists.
        entries_df = pd.DataFrame(
            {
                "Order": [order for order in news_orders],
                "Title": [title for title in news_titles],
                # the two final lines has a "+ [0]" because the page has
                # one entry that does not have points and comments, so the
                # data is incomplete and the easiest way that I found to
                # solve this was to fill the list with a zero.
                "Points": [point for point in news_points + [0]],
                "Comments": [int(comment) for comment in news_comments + [0]],
            },

        )
        # set the df index to the "Order" column.
        entries_df = entries_df.set_index('Order')
        # finally return the Pandas DataFrame.
        return entries_df

    # creation of the filter more than 5 words method.
    def filter_more_five_words(self, df):
        # do this with Pandas is really easy.
        # first, sort the df by the "Comments" column in
        # ascending order.
        sorted_df = df.sort_values('Comments', ascending=True)
        # then, to filter the titles, first you need to split
        # each row into a list and get the length of the list.
        count_words = sorted_df['Title'].str.split().str.len()
        # then, filter the words by a condition, if the length is
        # more than 5, retrieve a new df with the filtered data.
        five_words_df = sorted_df[count_words > 5]
        # finally return the new df.
        return five_words_df

    # creation of the filter less or equal than 5 words method.
    def filter_less_five_words(self, df):
        # first, sort the df by the "Points" column in ascending order.
        sorted_df = df.sort_values('Points', ascending=True)
        # then, you can do the same thing of the above method but
        # with a different condition.
        count_words = sorted_df['Title'].str.split().str.len()
        five_words_df = sorted_df[count_words <= 5]
        return five_words_df

# This is the crawler test file, to do this
# I use pytest, a framework to automate tests in Python.

import crawler, pytest # import the crawler "module" and pytest

# in the following functions, I test the different methods
# of the crawler class using the length of the lists and 
# data returned.
def test_request_url():
    request_crawler = crawler.Crawler()
    request_crawler = request_crawler._request_url()
    assert len(request_crawler) > 1, "test failed"

def test_parse_order_number():
    order_numbers = crawler.Crawler()
    order_numbers = order_numbers._parse_order_number()
    assert len(order_numbers) == 30, "test failed"

def test_parse_title():
    title = crawler.Crawler()
    title = title._parse_title()
    assert len(title) == 30, "test failed"

def test_parse_points():
    points = crawler.Crawler()
    points = points._parse_points()
    # in this case the lenth is 29 due to
    # in the page there is one entry that does
    # not have points.
    assert len(points) == 29, "test failed"


def test_parse_comments():
    comments = crawler.Crawler()
    comments = comments._parse_points()
    # in this case the lenth is 29 due to
    # in the page there is one entry that does
    # not have comments.
    assert len(comments) == 29, "test failed"

def get_entries():
    entries = crawler.Crawler()
    entries = entries.get_entries()
    assert len(entries) == 30, "test failed"
# Python Web Scrawler 🕷️
This is a Python Web Crawler to scrape the YCombinator Hacker News Site. (https://news.ycombinator.com/).
This Web Crawler retrieve the order number, news title, news points, and news comments of the first 30 entries in the page.
Then, the program filter the data with more than five words in the title ordered by the amount of comments first, and filter the data with less than or equal to five words in the title ordered by points.
Finally, the program saves all the data in an Excel file (if the user wants to do this).
## Project structure 🌲
The project has two principal Python files and one Python file for testing.
The first Python file is `crawler.py`, this file has the crawler class with the different methods to request the page and retrieve all the needed data.
The second Python file is `main.py`, this file has the invocations of the crawler methods inside a menu.
The third file is `test_crawler.py`, this file tests the different methods inside the crawler module.
## Requirements 👣
This project requires the following Python requirements:
```
beautifulsoup4==4.9.3
requests==2.26.0
pandas==1.3.2
pytest==7.0.1
```
## Install the Crawler 🕸️
Please, to install the Crawler follow these steps:
```
git clone https://github.com/Danii2020/python-web-crawler.git
cd /python-web-crawler
pip install requirements.txt
```
## Run the crawler 🏃
Please, to run the Crawler follow these steps in a terminal:
```
Linux: python3 main.py
Windows: py or python main.py
```
## Run the tests 📄
Please, to run the Crawler tests follow these steps in a terminal:
```
Linux: pytest test_crawler.py
Windows: py.test test_crawler.py
```
## Video demo 📺
In the following link you have a video demo of the program:
[YouTube Video Demo](https://youtu.be/bA8toajG_xs)

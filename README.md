# flask_scraper


This Flask application enables users to enter a search term and a target HTML element. It then fetches a web page using the requests library, parses it with Beautiful Soup, and extracts the selected elements using soup.find_all(tag_name). Finally, it renders the extracted content in a template (main.html).
To make this work you have to install some packets
```bash

pip install beautifulsoup4

pip install flask

pip install requests

pip install lxml

flask run

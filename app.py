from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import os, requests

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main():
    
    search_term = ""
    html_content = ""
    selected=request.form.get('options')
    
    if request.method == 'POST':
        search_term = request.form['search']

        # Sanitize search term (optional)
        # You can use libraries like `html.escape` to prevent XSS attacks

        url = f"{search_term}"

        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, "lxml")
                html_content = soup.prettify()
                if selected:
                    if selected == "div":
                        html_content=soup.find_all("div")
                        return render_template('main.html', search_term=search_term, html_content=html_content)
                    elif selected == "img":
                        html_content=soup.find_all("img")
                        return render_template('main.html', search_term=search_term, html_content=html_content)
                    elif selected == "full site":
                        return render_template('main.html', search_term=search_term, html_content=html_content)
                    elif selected == "h1":
                        html_content=soup.find_all("h1")
                        return render_template('main.html', search_term=search_term, html_content=html_content)
                    elif selected == "p":
                        html_content = soup.find_all("p")
                        return render_template('main.html', search_term=search_term, html_content=html_content)
                    elif selected == "ul":
                        html_content = soup.find_all("ul")
                        return render_template('main.html', search_term=search_term, html_content=html_content)
                    elif selected == "ol":
                        html_content = soup.find_all("ol")
                        return render_template('main.html', search_term=search_term, html_content=html_content)
                    elif selected == "a":
                        html_content = soup.find_all("a")
                        return render_template('main.html', search_term=search_term, html_content=html_content)
                    elif selected == "li":
                        html_content = soup.find_all("li")
                        return render_template('main.html', search_term=search_term, html_content=html_content)
                    elif selected == "table":
                        html_content = soup.find_all("table")
                        return render_template('main.html', search_term=search_term, html_content=html_content)
                    elif selected == "tr":
                        html_content = soup.find_all("tr")
                        return render_template('main.html', search_term=search_term, html_content=html_content)
                    elif selected == "th":
                        html_content = soup.find_all("th")
                        return render_template('main.html', search_term=search_term, html_content=html_content)
                    elif selected == "td":
                        html_content = soup.find_all("td")
                        return render_template('main.html', search_term=search_term, html_content=html_content)
                    elif selected == "span":
                        html_content = soup.find_all("span")
                        return render_template('main.html', search_term=search_term, html_content=html_content)
                    elif selected == "meta":
                        html_content = soup.find_all("meta")
                        return render_template('main.html', search_term=search_term, html_content=html_content)
                    elif selected == "form":
                        html_content = soup.find_all("form")
                        return render_template('main.html', search_term=search_term, html_content=html_content)
                    elif selected == "input":
                        html_content = soup.find_all("input")
                        return render_template('main.html', search_term=search_term, html_content=html_content)
                    elif selected == "button":
                        html_content = soup.find_all("button")
                        return render_template('main.html', search_term=search_term, html_content=html_content)
            else:
                print(f"Error: Failed to download page. Status code: {response.status_code}")
                return render_template('error.html')
        except requests.exceptions.RequestException as e:
            print(f"Error: An error occurred during scraping: {e}")
            return render_template('error.html')

    return render_template('main.html',search_term=search_term, html_content=html_content)
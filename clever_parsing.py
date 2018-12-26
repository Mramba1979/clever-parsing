import requests
import csv
import time
from bs4 import BeautifulSoup

start_time = time.time()

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'}


def get_html(url):
    r = requests.get(url, headers=headers)
    time.sleep(2)
    if r.ok:
        return r.text
    print(r.status_code)


def write_csv(data):
    with open("clever.csv", "a", newline="") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow([data["title"],
                         data["price"],
                         data["author"],
                         data["url"]])


def get_page_data(html):
    soup = BeautifulSoup(html, "lxml")
    books = soup.find_all("div", class_="book-content")

    for book in books:
        # Название книги
        try:
            title = book.find("div", class_="title").find("p").text
        except:
            title = "none"

        # URL книги
        try:
            url = "https://www.clever-media.ru" + book.find("a", class_="description").get("href")
        except:
            url = "none"

        # Цена книги
        try:
            price = book.find("div", class_="with-discount").find("p", class_="new").find("span").text
        except:
            price = "none"

        # Автор книги
        try:
            author = book.find("div", class_="name").find("p").text
        except:
            author = "none"

        data = {"title": title,
                "price": price,
                "author": author,
                "url": url}

        write_csv(data)


def main():

    pattern = "https://www.clever-media.ru/shop/?srt=30&page={}"

    for i in range(1, 35):
        url = pattern.format(str(i))
        get_page_data(get_html(url))

    print("Парсинг завершен за %s секунд" % (time.time() - start_time))


if __name__ == "__main__":
    main()

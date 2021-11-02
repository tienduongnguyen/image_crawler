from selenium import webdriver
from time import sleep
import random

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# init browser
browser = webdriver.Chrome(executable_path="chromedriver.exe", options=options)

# open browser
browser.get("https://tiki.vn/search?q=s%C3%A1ch&ref=searchBar")

# delay web
sleep(random.randint(4, 8))

# find data
book_list = browser.find_elements_by_class_name("product-item")

index = 1
# choose data and write to csv
for book in book_list:
    # ----------------
    name = book.find_element_by_class_name("name")
    name = name.text.replace("Ad", "")
    name = name.replace(",", "/")
    # ----------------
    price = book.find_element_by_class_name("price-discount__price")
    price = price.text.replace("₫", "")
    price = price.replace(".", "")
    # -----------------
    src = book.find_element_by_tag_name("img")
    src = src.get_attribute("src")
    # ----------------
    info = str(index) + ";" + name + ";" + price + ";" + src + "\n"
    # ----------------
    with open("data.csv", 'a', encoding="utf-8") as file:
        file.write(info)
    index += 1

# close browser
browser.close()

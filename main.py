import requests
from bs4 import BeautifulSoup

# 마지막 페이지 가져오기
def get_last_page(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination_numbers = soup.find("div", {"class": "paginationNumbers"})
    last_page = int(pagination_numbers.find_all("div", {"class": "paginationNo-navi"})[-1].string)
    return last_page

# 제품 리스트 가져오기
def get_products(url, last_page):
    products = [];
    for page in range(last_page):
        result = requests.get(f"{url}?productListPage={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        product_list_page = soup.find("div", {"class": "productListPage"})
        results = product_list_page.find_all("div", {"class": "shopProductWrapper"})
        for result in results:
            products.append(get_product(result))
    return products


# 제품 가져오기
def get_product(product_html):
    name = product_html.find("div", {"class": "productName"}).string
    link_img = product_html.find("div", {"class": "thumb"})["style"][32:-1]
    a_href = product_html.find("a")["href"]
    link_detail = f"https://jase.kr{a_href}"
    return {
        "name": name,               # 이름
        "link_img": link_img,       # 이미지 링크
        "link_detail": link_detail  # 상세 페이지 링크
    }

url = "https://jase.kr/all"

last_page = get_last_page(url)
get_products(url, last_page)





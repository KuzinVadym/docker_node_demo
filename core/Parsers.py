#! /usr/bin/env python3

from urllib.request import urlopen
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import json
import re

URL5 = "http://www.mediamarkt.de/de/search.html?query=xiaomi&searchProfile=onlineshop&channel=mmdede"
URL4 = "https://www.quelle.de/s/schwarz+sofa/"
URL3 = "https://www.otto.de/suche/schwarz%20sofa/"
URL2 = "http://www.ikea.com/de/de/catalog/categories/departments/living_room/10696/"
URL1 = "https://www.neckermann.de/moebel/sessel?q=sessel/"
URL = "http://www.ikea.com/de/de/search/?query=sessel"


class Ikea:
    def __init__(self):
        self.search_url = "http://www.ikea.com/de/de/search/?query={}"
        self.query_divider = "+"

    def __search(self, query):
        url = self.search_url.format(self.query_divider.join(query.split()))
        response = urlopen(url).read()
        return response

    def parse_search_results(self, query):
        parse_result = {}
        raw_html = self.__search(query)
        soup = BeautifulSoup(raw_html, "html.parser")
        # prods = soup.find_all(class_="productContainer")
        table = soup.find("table", class_="productsContainer")
        if not table:
            return "no results"
        prods = table.find_all(class_="productContainer")
        for elem in prods:
            raw_item_id = elem.get("id")
            if not raw_item_id:
                continue
            item_id = re.search("(?<=_).+(?=_)", raw_item_id).group(0)
            # print(item_id)
            item_dict = {
                "price": elem.find(class_="prodPrice").text.strip(),
                "title": elem.find(class_="prodName").text.strip(),
                "link": urljoin(URL, elem.find(class_="productPadding").a["href"]),
                "img_src": urljoin(URL, elem.find(class_="prodImg")["src"]),
                "desc": elem.find(class_="prodDesc").text.strip(),
                "info": "\n".join([i.text.strip() for i in elem.find_all(class_="prodDimension")]),  # .text.strip()),
                "options": elem.find_all(class_="prodOptions") if len(elem.find_all(class_="prodOptions")) > 0 else "",
            }
            # print(item_dict)
            parse_result[item_id] = item_dict
        # print(parse_result)
        return parse_result  # json.dumps(parse_result, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    result = {}
    ikea_search = Ikea()
    result["ikea_results"] = ikea_search.parse_search_results("sessel")
    print(result)
    result["ikea_results"] = ikea_search.parse_search_results("weis sofa")
    print(result)

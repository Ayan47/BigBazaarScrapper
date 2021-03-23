import time
import json
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path = r"C:\{"YOUR\PATH\HERE"}\chromedriver.exe")
categories=["Fruits--Vegetables-279","Bakery--Dairy-283","Home-Fashion-1093","Kitchen-&-Dining-291","Meat-&-Non-Veg-1003","Grocery-&-Staples-281","Snacks-&-Packaged-Food-287","Spreads-&-Sauces-285"]

for category in categories:
    url = "https://shop.bigbazaar.com/catalog/category/"+category
    driver.get(url)
    data = {}
    data['product'] = []
    # Scroller
    last_height = driver.execute_script("return document.body.scrollHeight")
    print(last_height)
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        print(new_height)
        if new_height == last_height:
            break
        last_height = new_height
    # parser
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # products tag catcher
    products=soup.find_all(class_="col-xs-4 col-sm-4 similar")
    for product in products:
        # Product Name
        name= product.find('div',class_="product-name").text
        #  List Price
        list_price=product.find('div',class_="list-price")
        # Member Price
        result = product.find('div',attrs={"class":"member-prices"}).get_text(strip=True, separator=" ").split()
        member_price=result[0]+result[1]
        # Quantity
        result1 = product.find('div',attrs={"class":"size-cart"}).get_text(strip=True, separator=" ").split()
        quantity= result1[0]+result1[1]

        if list_price is not None:
            data['product'].append({
                'Product Name': name,
                'List Price': list_price.text,
                'Member Price': member_price,
                'Quantity': quantity})
        else:
            data['product'].append({
                'Product Name': name,
                'Member Price': member_price,
                'Quantity': quantity})

    json_object = json.dumps(data, indent = 4)
    with open(f"{category}.json", "w") as outfile:
        outfile.write(json_object)
driver.quit()

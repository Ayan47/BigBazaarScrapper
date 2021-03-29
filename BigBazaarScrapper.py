import time
import json
from bs4 import BeautifulSoup
from selenium import webdriver

def page_scroller(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def product_tag_catcher(soup):
    data = {}
    data['product'] = []
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
    return (data)

def jsondump(data,soup):
    json_object = json.dumps(data, indent = 4)
    with open(f"{soup.find('title').text}.json", "w") as outfile:
        outfile.write(json_object)


if __name__=="__main__":
    url_list=[]
    try:
        number_of_url=int(input("Enter the number of url's: "))
        if(number_of_url>0):
            print("Enter the URL/URL's you want to scrape")
            for i in range(number_of_url):
                url_list.append(input(f"url { i+1}:"))
        elif(number_of_url<0):
            print("Enter a positive number, Please!")
            exit()

    except ValueError:
        print("You gotta enter something here buddy!!")
        exit()
    driver = webdriver.Chrome(executable_path = r"YOUR\PATH\HERE\chromedriver.exe")
    for category in url_list:
        driver.get(category)
        page_scroller(driver)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        data=product_tag_catcher(soup)
        jsondump(data,soup)
    driver.quit()





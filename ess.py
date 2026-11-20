from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

driver = webdriver.Chrome()
driver.maximize_window()

all_products = []

for pages in range (1,9):
    driver.get(f"https://ecc-alex.com/en/laptop.html?p={pages}")
    print('page :' , pages)

    container = driver.find_elements(By.XPATH , '//div[contains(@class , "product-info") and contains(@class , "product-item-info")]')
    # print(container)

    for item in container:
        try:
            description = item.find_element(By.XPATH , './/h3[@class="product-name"]').text
            print("description :" , description)
        except:
            description = 'no description found'
            print("description :" , description)

        price = item.find_element(By.XPATH , './/span[@class="price"]').text
        print("price :" , price)

        try:
            price_befor_discount = item.find_element(By.XPATH , './/span[@data-price-type="oldPrice"]').text
            print("price befor discount :" , price_befor_discount)
        except:
            price_befor_discount = "no discount"
            print("price befor discount :" , price_befor_discount)

        try:
            stock = item.find_element(By.XPATH , './/div[@class="stock unavailable"]').text
            print("stock :" , stock)
        except:
            stock = "available"
            print("stock :" , stock)
        try:
            product_image = item.find_element(By.XPATH , './/img[contains(@class , "lazyOwl") and contains(@class , "product-image-photo")]').get_attribute("data-src")
            print("product image :" , product_image)
        except:
            product_image = "no image found"
            print("product image :" , product_image)

        try:
            product_link = item.find_element(By.XPATH, './/div[@class="product-photo"]/a').get_attribute("href")
            print("product_link :" , product_link)
        except:
            product_link = "no product link found"
            print("product_link :" , product_link)

        print("="*20)

        dict_products = {
            "description" : description ,
            "price" : price ,
            "stock" : stock ,
            "price_befor_discount" : price_befor_discount ,
            "product_image" : product_image ,
            "product_link" : product_link ,
        }

        all_products.append(dict_products)

header = all_products[0].keys()
path = "all products.csv"

with open(path ,"w", encoding='utf-8-sig' , newline="") as file :
    writer = csv.DictWriter(file , header)
    writer.writeheader()
    writer.writerows(all_products)

input("press enter to close : ")
driver.quit()

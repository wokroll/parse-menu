import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service


def parse(link):

    s = Service("C:/Users/User/Downloads/chromedriver_win32/chromedriver.exe")
    driver = webdriver.Chrome(service=s)

    driver.get(link)

    time.sleep(5)

    restaurantName = driver.find_element(By.CSS_SELECTOR, "head > title").get_attribute("innerText")
    restaurantName = restaurantName.replace(" - self-service in your device by ORTY", "")

    windowHeight = driver.execute_script("return document.body.scrollHeight")

    jsGetProductsData = """
    products = document.querySelectorAll('[id^="product"]')
    
    allIds = []
    
    for (var i = 0, n = products.length; i < n; ++i) {
      var el = products[i];
      if (el.id) { allIds.push(el.id); }
    }
    
    return allIds
    """

    allIds = driver.execute_script(jsGetProductsData)
    iterator = 0
    productsData = {}

    body = driver.find_element(By.CSS_SELECTOR, 'body')
    for i in range(int(windowHeight / 40) + 1):
        body.send_keys(Keys.ARROW_DOWN)
        time.sleep(0.03)

    # counter of not successful elements
    notSuccessful = 0

    for productId in allIds:

        try:
            productNameXPath = "//*[@id='" + productId + "']/div[2]/div[1]/span/h3"
            productName = driver.find_element(By.XPATH, productNameXPath).text

            productPriceXPath = "//*[@id='" + productId + "']/div[2]/div[2]/div/p/span"
            productPrice = driver.find_element(By.XPATH, productPriceXPath).get_attribute("innerHTML")

            productsData[iterator] = {'name': productName,
                                      'price': productPrice
                                      }
        except NoSuchElementException:
            notSuccessful += 1
            print("No such element")

        iterator += 1

    driver.quit()



    # print("Successful elements:" + str(len(productsData)))
    # print("Not found elements:" + str(notSuccessful))

    return restaurantName, productsData

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep, time

# driver = webdriver.Firefox()

# driver.get('https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS/?th=1')
# finder = driver.find_element(By.CLASS_NAME, value='a-price-whole')
# print(finder.text)

# driver.quit()



# I cheated from solution in section contant

driver = webdriver.Firefox()
driver.get("https://ozh.github.io/cookieclicker/")
sleep(3)
lang_btn = driver.find_element(by=By.ID, value="langSelect-EN")
lang_btn.click()
sleep(3) 
cookie = driver.find_element(by=By.ID, value="bigCookie")
wait_time = 5
timeout = time() + wait_time
five_min = time() + 60 * 5  
while True:
    cookie.click()
    if time() > timeout:
            cookies_element = driver.find_element(by=By.ID, value="cookies")
            cookie_text = cookies_element.text
            cookie_count = int(cookie_text.split()[0].replace(",", ""))
            products = driver.find_elements(by=By.CSS_SELECTOR, value="div[id^='product']")
            best_item = None
            for product in reversed(products):
                if "enabled" in product.get_attribute("class"):
                    best_item = product
                    break
            if best_item:
                best_item.click()
            timeout = time() + wait_time

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# chrome_driver_path = Service("C:\Development\chromedriver.exe")
# driver = webdriver.Chrome(service=chrome_driver_path)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://orteil.dashnet.org/experiments/cookie/")


def store_check():
    money = get_money()
    print(f"Money: {money}")
    store = driver.find_elements(By.CSS_SELECTOR, '#store b')
    cost_dict = {}
    n = 0
    for item in store:
        try:
            strip = item.text.replace(" - ", "_").replace(" ", "-").replace("_", " ")
            cost = strip.split()
            cost[0] = cost[0].replace("-", " ")
            cost[0] = cost[0].split()[0]
            cost[1] = cost[1].replace(",", "")
            cost_dict[n] = {
                'item': cost[0],
                'cost': int(cost[1])
            }
        except IndexError:
            print("List End")
        finally:
            n += 1

    for item in reversed(cost_dict):
        if money > cost_dict[item]['cost']:
            store_buy(cost_dict[item]['item'])
            break


def store_buy(item):
    print(item)
    button = driver.find_element(By.CSS_SELECTOR, f"#buy{item}")
    button.click()


def get_money():
    money = driver.find_element(By.XPATH, '//*[@id="money"]')

    return int(money.text.replace(",", ""))


game_end = time.time() + 60 * 5
playing = True
while playing:
    timeout = time.time() + 5
    while True:
        cookie_btn = driver.find_element(By.XPATH, '//*[@id="cookie"]')
        cookie_btn.click()
        if time.time() > timeout:
            break
    store_check()
    if time.time() > game_end:
        playing = False

cookies_per_sec = driver.find_element(By.XPATH, '//*[@id="cps"]')
print(cookies_per_sec.text)

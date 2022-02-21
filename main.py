from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:/Users/drorlotan/PycharmProjects/development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

form_link = "https://docs.google.com/forms/d/e/1FAIpQLSemkWmjl4zRsGpZPSH7Ui-SmSevBYMAGFFnNCan8Q0ES0r6jg/viewform?usp=sf_link"
yad2_link = "https://www.yad2.co.il/realestate/rent/map?city=8600&rooms=2.5--1&price=2000-5500&z=12"
headers = {
    'User-Agent': "Mozilla/5.0",
}

driver.get(yad2_link)
sleep(2)
soup = BeautifulSoup(driver.page_source, "html.parser")
def make_list(setting):
    tags = soup.find_all("div", class_=setting)
    settings = [item.getText() for item in tags]
    return settings

address_list = make_list("address")

prices_list = make_list("price")
prices_list_exact = [price[17:23] for price in prices_list]
# links_tags = soup.find_all("div", class_="feeditem")
# links_list = [link. for link in links_tags]
print(prices_list_exact)
print(address_list)


driver.get(url=form_link)
sleep(2)
for apartment in range(len(address_list)):
    address_fill = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    address_fill.send_keys(address_list[apartment])
    price_fill = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    price_fill.send_keys(prices_list[apartment])
    send = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span")
    send.click()
    submit_another = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
    submit_another.click()
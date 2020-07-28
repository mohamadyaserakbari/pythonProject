from selenium import webdriver as we
from time import sleep

driver = we.Chrome()
username = "lex_orginal"
password = "yaser@1376"
driver.get("https://www.instagram.com")
sleep(1)
driver.find_element_by_xpath(
    "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input").send_keys(username)
sleep(1)
driver.find_element_by_xpath(
    "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input").send_keys(password)
sleep(1)
driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button").click()
sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/section/div/button").click()
sleep(2)
driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
sleep(2)
driver.get(f"https://www.instagram.com/p/CCl8C3Fhpxi/")
sleep(3)
driver.execute_script("document.getElementsByTagName('button')[2].click()")
sleep(2)
driver.execute_script("document.getElementsByTagName('textarea')[0].click()")
sleep(1)
comment = input("write your comment: ")
driver.find_elements_by_tag_name("textarea")[0].send_keys(comment)
sleep(1)
driver.find_element_by_xpath(
    "/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button").click()
sleep(2)

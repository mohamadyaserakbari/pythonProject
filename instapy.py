from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

mobile_emulation = {
    "deviceMetrics": {"width": 420, "height": 600, "pixelRatio": 3.0},
    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP400) Applewebkit/535.19 (KHTML, Like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
}

chrome_options = Options()

chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

driver = webdriver.Chrome(options=chrome_options)

username = "lex_orginal"
password = "yaser@1376"


def trytosave():
    try:
        driver.execute_script("""
        var input = document.getElementsByTagName("button")
        for(i=0 ; i<input.length ; i++){
            if(input[i].textContent == "Save Info"){
                input[i].click();
                break;
                }
            }
        """)
    except:
        print("not now!!")


def trytocancel():
    try:
        driver.execute_script("""
        var input = document.getElementsByTagName("button")
        for(i=0 ; i<input.length ; i++){
            if(input[i].textContent == "Not Now"){
                input[i].click();
                break;
            }
        }
        """)
    except:
        print("Not now !!")


# driver = webdriver.Chrome()
driver.get("https://www.instagram.com/accounts/login/")
sleep(3)
driver.find_element_by_name("username").send_keys(username)
sleep(0.5)
driver.find_element_by_name("password").send_keys(password)
sleep(2)
driver.execute_script("""
var input = document.getElementsByTagName("button")
for(i=0 ; i<input.length ; i++){
    if(input[i].textContent == "Log In"){
        input[i].click();
        break;
    }
}
""")
sleep(2)
trytosave()
sleep(1)
trytocancel()
sleep(2)
driver.execute_script("""
        var input = document.getElementsByTagName("button")
        for(i=0 ; i<input.length ; i++){
            if(input[i].textContent == "Cancel"){
                input[i].click();
                break;
            }
        }
""")
sleep(2)
# driver.get("https://www.instagram.com/___rira_/")
driver.execute_script("""
        var input = document.getElementsByTagName("button")
        for(i=0 ; i<input.length ; i++){
            if(input[i].textContent == "Log In"){
                input[i].click();
                break;
            }
        }
""")
sleep(3)
driver.execute_script("""
var input = document.getElementsByTagName('div')
        for(i=0 ; i<input.length ; i++){
            try{
                if(input[i].getAttribute('data-testid') == 'new-post-button')
                    { input[i].click(); break;}
                }
            catch{alert("Erorr!")}}
""")
sleep(3)
#driver.find_element_by_xpath("/html/body/div[1]/section/nav[2]/div/div/div[2]/div/div/div[3]").click()
driver.execute_script("""
var input = document.getElementsByTagName("div")
for (i = 0; i < input.length; i++) {
    try {
        if (input[i].getAttribute("data-testid") == "new-post-button") {
            input[i].click();
            break;
        }
    } catch {
        var a = 58;
    }
}
""")
sleep(3)
#driver.find_element_by_xpath("/html/body/div[1]/section/nav[2]/div/div/div[2]/div/div/div[3]").click()
#sleep(1)
driver.find_element_by_xpath("/html/body/div[1]/section/nav[2]/div/div/div[2]/div/div/div[3]").send_keys(r"/home/yaser/Desktop/1.jpeg")
sleep(3)
# var
# input = document.getElementsByTagName("button")
# for (i=0; i < input.length; i++){
#     try{
#     if (input[i].children[0].getAttribute("aria-label") == "Options"){
#     input[i].click();
# break;
# }}
# catch
# {var
# n = 56}
# }

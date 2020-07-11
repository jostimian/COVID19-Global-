from selenium import webdriver
from colorama import Fore, Back, Style
from colorama import init
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#imports all necesary library

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
start_url = "https://www.coronatracker.com/"
driver.get(start_url)
driver.implicitly_wait(10)

init(autoreset=True)
print(Style.BRIGHT + Fore.GREEN + "CSP ERROR MIGHT APPEAR JUST IGNORORE")
loop = True

while loop == True:

    def latest():
        latest_xpath = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/span')
        latest_list = latest_xpath.text
        return latest_list 
        
    def recovered():
        recovered_xpath = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/span')
        recovered_list =  recovered_xpath.text
        return recovered_list

    def deaths():
        deaths_xpath = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/span')
        deaths_list =  deaths_xpath.text
        return deaths_list 

    def seeall():
        latest()
        recovered()
        deaths()
        print(Style.BRIGHT + Back.GREEN + "Recovered", recovered_list)
        print(Style.BRIGHT + Back.YELLOW + "Cases", latest_list)
        print(Style.BRIGHT + Back.RED + "Deaths", deaths_list)

    latest_list = latest()
    recovered_list = recovered()
    deaths_list = deaths()
    for i in range (2):
        print("\n")

    user_input = input("use /help to see all of the commands: ")
    if user_input == "/help":
        print(Fore.CYAN + Style.BRIGHT + """
        /all = view all confirmed cases recoveries and deaths
        /deaths = view all confirmed deaths
        /recover = view all confirmed recoveries
        /cases = view all confirmed cases
        /quit = quit the aplication
        """)
        print(Back.MAGENTA + "I am planing to add support to firefox")

    if user_input == "/deaths":
        print(Style.BRIGHT + Back.RED + "Deaths", deaths_list)

    if user_input == "/recover":
        print(Style.BRIGHT + Back.GREEN + "Recovered", recovered_list)

    if user_input == "/cases":
        print(Style.BRIGHT + Back.YELLOW + "Cases", latest_list)

    if user_input == "/all":
        seeall()
        
    if user_input == "/quit":
        driver.quit()
        loop = False

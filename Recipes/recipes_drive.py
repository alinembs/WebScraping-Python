# imports


from selenium import webdriver
import chromedriver_autoinstaller as chromedriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import getpass

# other imports

chromedriver.install(cwd=True)


username = getpass.getuser()
options = Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)

def category_link(link):
    driver.get("https://myfoodbook.com.au{link}")
    time.sleep(5)
    inspect = '//*[@id="block-views-recipes-categories-allrec"]/div/div/div/div[3]/div/div'
    element1 = driver.find_element("xpath", f"{inspect}")
    element = element1.get_attribute("outerHTML")
    soup = BeautifulSoup(element, "html.parser")
    recipe_link = []
    for div in soup.find_all("a"):
        link = div.get("href")
        if ("/recipes/show/" in link):
            recipe_link.append(link)
        
    for links in range(12):
        recipe_link.pop(links)

    return recipe_link
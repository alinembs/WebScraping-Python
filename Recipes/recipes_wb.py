# other imports
import pandas as pd
from tqdm import tqdm
import requests
from recipes_drive import*

recipes = {'title':[],'prep':[],'serves':[],'descrip':[],'prep_steps':[]}

url = "https://myfoodbook.com.au/categories"

payload = ""
response = requests.request("GET", url, data=payload)
soup = BeautifulSoup(response.text, 'html.parser')
list_link = []
llink_ant = ""

for  div in soup.find_all('a'):
        link = div.get('href')
        if ("/categories/" in link) and (link_ant == link):
            list_link.append(link)

        link_ant = link

for link in tqdm(range(len(list_link))):
  
    recipe_link = category_link(list_link[link])
    print(recipe_link)
    """ for range_recipes in range(2):
             
            url = (f'https://myfoodbook.com.au{recipe_link[range_recipes]}')
            response = requests.request("GET", url, data=payload)
            soup2 = BeautifulSoup(response.text, 'html.parser')

            title = soup2.find("a", {"class": "magnify fancybox tme"})
            recipes['title'].append(title.get('title'))
            prep = soup2.find("div", {"class": "recipe-prop-item prep-time"})
            recipes["prep"].append(prep.text.split("Prep:")[1].replace("\xa0\xa0",""))
            serves = soup2.find("div", {"class": "recipe-prop-item serves"})
            recipes["serves"].append(serves.text.split("Serves:")[1].replace("\xa0\xa0",""))
            descrip = soup2.find("div", {"class": "rec-desc"})
            recipes['descrip'].append(descrip.text)
            ingredients = "Ingredients: "
            for indice in soup2.find_all("div",{"class":"ingredients"}):
                ingredients = ingredients + indice.text + "-"


            method = soup.find("div",{"class":"method"})

            recipes["prep_steps"].append(ingredients + "--" + method.text)  """
           
df = pd.DataFrame(list(zip(recipes["title"],recipes["descrip"],recipes["prep"],recipes["serves"],recipes["prep_steps"])), columns=["title", "descrip", "prep", "serves", "prep_steps"])
df.to_csv("/home/aline/Downloads/webscraping/WebScraping-Python/Recipes/receitas_salvas_site.csv", index=False)
print("Receitas Salvas")
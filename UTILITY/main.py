# import re
import requests
from bs4 import BeautifulSoup

# html = requests.get("https://www.worldometers.info/coronavirus/")
# soup = BeautifulSoup(html.text,'html.parser')
# update = soup.title.string
# # print(update)
# update = str(update)
#this is can be used as well, but first import re , regularexpression
# test_string = update
# temp = re.findall(r'\d+', test_string)
# res = list(map(int, temp))
# print(res)
class Coronameter():
    def __init__(self):
        self.html =  requests.get("https://www.worldometers.info/coronavirus/")
        self.soup = BeautifulSoup(self.html.text,'html.parser')
        self.update = str(self.soup.title.string)
    # total death in world
    def total_death(self):    
        """Calculate the number of death around the world

        Returns:
            int: The number of Death
        """
        new_death = ''
        for c in self.update.split(':')[1].split('Cases')[1]:
            if c.isdigit():
                new_death+=c

        # print(new_death)
        return int(new_death)

    # total new cases in world
    def total_case(self):
        """Calculate the Number of Cases around the world

        Returns:
            int: The number of Cases
        """
        new_case = ''
        for c in self.update.split(':')[1].split('Cases')[0]:
            if c.isdigit():
                new_case+=c
        
        # print(new_case)
        return int(new_case)
    
        
        
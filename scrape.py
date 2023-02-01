from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import re
  
URL = "https://www.purposedriven.com/day24"
REGEX = "POINT\sTO\sPONDER:\n(.*)\nVERSE\sTO\sREMEMBER:\n(.*)\n(.*)\nQUESTION\sTO\sCONSIDER:\n(.*)"

req = Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
  
soup = BeautifulSoup(webpage, 'html5lib')

contents = []

soup = soup.find('div', attrs = {'id':'page'}) 
soup = soup.main.find('section', attrs ={'class':'message--section'})
soup = soup.div.findAll('div')[8] # found by brute force lmao

result = re.findall(REGEX, soup.text)

print(result)

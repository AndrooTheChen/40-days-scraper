from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import re
  
REGEX = "POINT\sTO\sPONDER:\n(.*)\nVERSE\sTO\sREMEMBER:\n(.*)\n(.*)\nQUESTION\sTO\sCONSIDER:\n(.*)"

def scrape_40_days():
    contents = []
    
    # Stop at 43 because the website is 1-indexed and there are actually 42 days.
    for day in range(1, 43):
        # Build the URL to correspond with the day and scrape the page.
        req = Request(f"https://www.purposedriven.com/day{day}", headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        
        # Parse the HTML.
        soup = BeautifulSoup(webpage, 'html5lib')

        # Traverse the DOM to find the relevant content.
        soup = soup.find('div', attrs = {'id':'page'}) 
        soup = soup.main.find('section', attrs ={'class':'message--section'})
        soup = soup.div.findAll('div')[8] # found by brute force lmao

        # Extract the relevant content via regex and some jank list manipulation.
        capture = re.findall(REGEX, soup.text)
        row = list(capture[0])
        row[1] = f"{row[1]} {row[2]}"
        row[2] = row[3]
        row.pop()

        contents.append(row)

    print(contents)
    return contents

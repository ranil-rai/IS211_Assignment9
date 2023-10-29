import requests
from bs4 import BeautifulSoup

def fetch_football_stats():
    URL = "https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/qualifiers/"
    page = requests.get(URL)
    
    soup = BeautifulSoup(page.content, 'html.parser')
    
    players = soup.find_all('tr', class_='TableBase-bodyTr')
    
    print("Player, Team, TDs")
    for player in players[:20]:
        details = player.find_all('td')
        name = details[0].get_text(strip=True)
        team = details[1].get_text(strip=True)
        tds = details[6].get_text(strip=True)
        
        print(f"{name}, {team}, {tds}")

if __name__ == "__main__":
    fetch_football_stats()

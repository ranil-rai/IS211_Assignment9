import requests
from bs4 import BeautifulSoup

def fetch_apple_stock():
    URL = "https://finance.yahoo.com/quote/AAPL/history?p=AAPL"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    page = requests.get(URL, headers=headers)
    
    soup = BeautifulSoup(page.content, 'html.parser')
    
    rows = soup.find_all('tr', class_='BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)')
    
    print("Date, Close Price")
    for row in rows:
        details = row.find_all('td')
        if len(details) >= 5:  # Check if the row contains enough data
            date = details[0].get_text(strip=True)
            close_price = details[4].get_text(strip=True)
            print(f"{date}, {close_price}")

if __name__ == "__main__":
    fetch_apple_stock()

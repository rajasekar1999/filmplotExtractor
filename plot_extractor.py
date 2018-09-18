import requests
import bs4
film = input("Enter the name of the film: ")
address = "https://en.wikipedia.org/wiki/"+film
req = requests.get(address)
soup = bs4.BeautifulSoup(req.text, 'lxml')
print()
print("Plot/Description of the film:\n")
plot = soup.select('p')
print(plot[2].getText())
import requests
from bs4 import BeautifulSoup

url = "https://www.gov.br/compras/pt-br/compras-e-licitacoes/editais-de-licitacao/ministerio-da-saude"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
editais = soup.find_all("a", class_="tileDocument")

for edital in editais:
    edital_url = edital["href"]
    edital_file = requests.get(edital_url)
    with open(edital_url.split("/")[-1], "wb") as f:
        f.write(edital_file.content)

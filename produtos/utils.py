import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "pt-BR,pt;q=0.9"
}

def pegar_dados(url):
    """Recebe a URL de um produto e retorna o preço atual."""
    resposta = requests.get(url, headers=HEADERS)
    sopa = BeautifulSoup(resposta.text, "lxml")

    preco_texto = sopa.find("span", {"class": "a-price-whole"})
    titulo = sopa.find("span", {"class": "a-size-large"})
    imagem = sopa.find("img", {"id": "landingImage"})
    
    
    if preco_texto and titulo:
        preco = float(preco_texto.get_text().replace(".", "").replace(",", "."))
        return {
            "preco": preco,
            "titulo": titulo.get_text(),
            "imagem": imagem["src"] if imagem else None,
        }
    return None

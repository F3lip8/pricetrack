import requests
from bs4 import BeautifulSoup
import time

# URL do produto
URL = "https://www.amazon.com.br/gp/product/8575225634/ref=ox_sc_act_image_10?smid=A1ZZFT5FULY4LN&psc=1"  # Exemplo
HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "pt-BR,pt;q=0.9"
}

# Preço alvo
PRECO_ALVO = 3500

def verificar_preco():
    resposta = requests.get(URL, headers=HEADERS)
    sopa = BeautifulSoup(resposta.text, "lxml")

    # Aqui você precisa identificar o seletor certo no HTML do site
    preco_texto = sopa.find("span", {"class": "a-price-whole"})
    titulo = sopa.find("span", {"class": "a-size-large"})
    if preco_texto:
        preco = float(preco_texto.get_text().replace(".", "").replace(",", "."))
        print(f"Preço atual: R${preco}")

        if preco <= PRECO_ALVO:
            print(titulo.get_text())
            print("💰 Preço abaixo do alvo! Compre agora!")
    else:
        print("Não consegui encontrar o preço.")

# Loop para verificar a cada 1 hora
while True:
    verificar_preco()
    time.sleep(10)

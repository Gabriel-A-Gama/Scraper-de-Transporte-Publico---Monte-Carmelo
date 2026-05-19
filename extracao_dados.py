import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# Fazendo a requisição para a página de transporte público
url = 'https://www.montecarmelo.mg.gov.br/transporte-publico'
response = requests.get(url)
html = response.text

# Criando o objeto Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')

# Criando o arquivo Excel
workbook = Workbook()
sheet = workbook.active
sheet.title = "Rotas Intercampi"
sheet.append(["Horário", "Parada"])  # Cabeçalho

# Buscando todos os elementos que contêm as informações das partidas
titulos = soup.find_all('div', class_='linha50')

# Extraindo os horários e paradas
for titulo in titulos:
    linhas = titulo.text.strip().splitlines()
    
    for linha in linhas:
        linha = linha.strip()
        if '»' in linha:
            horario, parada = linha.split(' » ', 1)  # Divide em horário e parada
            # Adiciona a informação no Excel
            sheet.append([horario.strip(), parada.strip()])

# Salvando o arquivo Excel
workbook.save("rotas_intercampi.xlsx")
print("Dados salvos em rotas_intercampi.xlsx.")
# Scraper-de-Transporte-P-blico---Monte-Carmelo
Esse é um script feito pra matéria de Projeto e  Desenvolvimento de  Sistemas de Informação I, onde faz um scraper de transporte público


##  Funcionalidades

- Faz scraping da página oficial de transporte público
- Extrai horários e paradas automaticamente
- Organiza os dados em uma planilha `.xlsx`
- Gera arquivo Excel pronto para uso

---

## Tecnologias Utilizadas

- Python 
- Requests
- BeautifulSoup4
- OpenPyXL


##  Estrutura

```bash
.
├── main.py
├── requirements.txt
└── rotas_intercampi.xlsx

```

## Instale as dependências:

pip install -r requirements.txt

## Ou instale manualmente:

pip install requests beautifulsoup4 openpyxl


## Como Usar

Execute o script:

python main.py

Após a execução, será gerado o arquivo:

rotas_intercampi.xlsx

## Como Funciona

O script:

Acessa a página de transporte público da prefeitura
Captura os elementos HTML contendo os horários
Separa horário e parada
Salva tudo automaticamente em uma planilha Excel
Fonte dos Dados

Portal oficial da Prefeitura de Monte Carmelo:

https://www.montecarmelo.mg.gov.br/transporte-publico

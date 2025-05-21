import pandas as pd 
from faker import Faker
import random
import os
from typing import List, Dict

fake = Faker('pt_BR')  # Usando a localidade para gerar dados em português

def gerar_lead() -> Dict[str, str]:
    return {
        "RazaoSocial": fake.company(),
        "CNPJ": fake.cnpj(),
        "Setor": random.choice(["Varejo", "Saúde", "Tecnologia", "Educação", "Finanças"]),
        "FaixaFuncionarios": random.choice(["1-10", "11-50", "51-200", "201-500", "501-1000"]),
        "Cidade": fake.city(),
        "UF": fake.state_abbr(),
        "TelefoneValidado": fake.phone_number(),
        "TelefoneGeral": fake.phone_number(),
        "EnderecoWeb": fake.url(),
        "EmailValidado": fake.email(),
        "NomeTomador": fake.name(),
        "PosicaoTomador": random.choice(["CEO", "Gerente", "Diretor", "Coordenador", "Analista"]),
        "DepartamentoTomador": random.choice(["TI", "Marketing", "Vendas", "Recursos Humanos"]),
        "EmailTomador": fake.email(),
        "TecnologiaWebsite": random.choice(["Shopify", "WordPress", "Wix", "Magento", "Squarespace"]),
        "ServidorEmail": random.choice(["Gmail", "Outlook", "Zoho", "Yahoo"]),
        "ServidorHospedagem": random.choice(["AWS", "GoDaddy", "HostGator", "BlueHost"]),
        "MaturidadeDigital": random.choice(["Iniciante", "Intermediário", "Avançado"]),
        "DataCadastro": fake.date_this_decade(),
        "OrigemLead": random.choice(["Manual", "CRM", "Upload"]),
        "StatusLead": random.choice(["Novo", "Qualificado", "Descartado"]),
        "FonteScraping": fake.url(),
        "DataScraping": fake.date_this_year()
    }

def gerar_leads(num_leads: int) -> List[Dict[str, str]]:
    return [gerar_lead() for _ in range(num_leads)]

def salvar_arquivo(df: pd.DataFrame, nome_arquivo: str) -> None:
    diretório = os.path.dirname(nome_arquivo)
    if not os.path.exists(diretório) and diretório != "":
        os.makedirs(diretório)
    
    df.to_excel(nome_arquivo, index=False, engine='openpyxl')
    print(f"Arquivo Excel gerado com sucesso: {nome_arquivo}")

def main(num_leads: int, nome_arquivo: str) -> None:
    dados_leads = gerar_leads(num_leads)
    df = pd.DataFrame(dados_leads)
    print(df.head())
    salvar_arquivo(df, nome_arquivo)

if __name__ == "__main__":
    NUM_LEADS = 100
    NOME_ARQUIVO = "data/leads_falsos_com_scraping.xlsx"
    main(NUM_LEADS, NOME_ARQUIVO)

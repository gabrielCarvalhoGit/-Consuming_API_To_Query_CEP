import requests
import json

def find_cep():
    print('---------------------------------------------')
    cep_number = input('Inform CEP to Consult: ')
    print('---------------------------------------------')

    api_cep_url = requests.get(f'https://viacep.com.br/ws/{cep_number}/json/')
    adress = json.loads(api_cep_url.text)

    list_adress = {
        "CEP": adress['cep'],
        "Endereço": adress['logradouro'],
        "Bairro": adress['bairro'],
        "Município": adress['localidade'],
        "Estado": adress['uf']
    }

    print(list_adress)

find_cep()
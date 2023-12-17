# arquivos.py
import os
import requests



#arquivos = {f'arquivo{i}': base_url.format(i) for i in range(1, 13)}
#print(arquivos)

def baixar_arquivo(url, endereco):
    # faz requisição ao servidor
    resposta = requests.get(url)
    if resposta.status_code == requests.codes.OK:
        with open(endereco, 'wb') as novo_arquivo:
            novo_arquivo.write(resposta.content)
        print("Donwload finalizado. Salvo em: {}".format(endereco))
    else:
        resposta.raise_for_status()


        
if __name__ == "__main__":
    
    
    
    BASE_URL = base_url = 'https://www.gov.br/anac/pt-br/assuntos/dados-e-estatisticas/percentuais-de-atrasos-e-cancelamentos-2/2018/vra-{:02d}_2018.csv'
    OUTPUT_DIR = r'C:\Users\tonho\OneDrive\Documentos\portifoliodedados\webscaping\PortifolioDeDados\caseGOL'
    for i in range(1, 13):
        nome_arquivo = os.path.join(OUTPUT_DIR, 'vra-{:02d}_2018.csv'.format(i))
        baixar_arquivo(BASE_URL.format(i), nome_arquivo)



import fitz  # Biblioteca PyMuPDF usada para manipular arquivos PDF

#Primeiro realizaremos a leitura do PDF e extrairemos os destinos por sessão.
#Para isso, utilizaremos a biblioteca PyMuPDF (fitz) para manipular o PDF, lembre-se de realizar o pip install PyMuPDF caso ainda não tenha feito.
#A função extrair_destinos_por_sessao irá ler o PDF e organizar os destinos em um dicionário, onde as chaves são as categorias e os valores são listas de destinos.


def extrair_destinos_por_sessao(pdf_path):
    doc = fitz.open(pdf_path)
    categorias = {
        "Praianas": [],
        "Capitais": [],
        "Interior": [],
        "Avião": [],
        "Ônibus": [],
        "Navio": []
    }

    sessao_atual = None
    proxima_eh_cidade = False
# Lê o PDF e extrai os destinos por sessão de cada página do documento.
# A função percorre cada página do PDF, identifica as seções e extrai os destinos correspondentes.
#criei o último elif para retirar o "•" que estava no começo de cada cidade, onde, antes disso, o código estava pegando o "•" como uma cidade.
    for page in doc:
        texto = page.get_text()
        linhas = texto.split('\n')
        for linha in linhas:
            linha = linha.strip()
            if "Destinos para Cidades Praianas" in linha:
                sessao_atual = "Praianas"
            elif "Destinos para Cidades Capitais" in linha:
                sessao_atual = "Capitais"
            elif "Destinos para Cidades Interiorana" in linha:
                sessao_atual = "Interior"
            elif "Pacotes de Avião" in linha:
                sessao_atual = "Avião"
            elif "Pacotes de Ônibus" in linha:
                sessao_atual = "Ônibus"
            elif "Pacotes de Navio" in linha:
                sessao_atual = "Navio"
            elif linha == '•':
                proxima_eh_cidade = True
            elif proxima_eh_cidade and linha and sessao_atual:
                categorias[sessao_atual].append(linha)
                proxima_eh_cidade = False
    doc.close()
    return categorias

#print(extrair_destinos_por_sessao("Prova NP2 - Catálogo de Destinos - PyTravel.pdf"))

#Agora que temos os destinos organizados por categorias, iremos realizar o cruzamento de dados conforme solicitado.
#A função cruzar_destinos irá receber o dicionário de destinos e realizar o cruzamento conforme as regras especificadas.

def cruzar_destinos(destinos):
    cruzamentos = {
        "Capitais Praianas": list(set(destinos["Capitais"]) & set(destinos["Praianas"])),
        "Capitais com Vôos": list(set(destinos["Capitais"]) & set(destinos["Avião"])),
        "Capitais com Ônibus": list(set(destinos["Capitais"]) & set(destinos["Ônibus"])),
        "Capitais com Navio": list(set(destinos["Capitais"]) & set(destinos["Navio"])),
        "Praianas com Vôos": list(set(destinos["Praianas"]) & set(destinos["Avião"])),
        "Praianas com Ônibus": list(set(destinos["Praianas"]) & set(destinos["Ônibus"])),
        "Praianas com Navio": list(set(destinos["Praianas"]) & set(destinos["Navio"])),
        "Interior com Vôos": list(set(destinos["Interior"]) & set(destinos["Avião"])),
        "Interior com Ônibus": list(set(destinos["Interior"]) & set(destinos["Ônibus"])),
        "Interior com Navio": list(set(destinos["Interior"]) & set(destinos["Navio"])),
        "Capitais com TODOS transportes": list(set(destinos["Capitais"]) & set(destinos["Avião"]) & set(destinos["Ônibus"]) & set(destinos["Navio"])),
        "Praianas com Avião e ônibus": list(set(destinos["Praianas"]) & set(destinos["Avião"]) & set(destinos["Ônibus"]))
    }
    return cruzamentos

#Para deixar a saída irei apresentar em markdown, o resultado dos cruzamentos de dados.

# Gerar markdown
def gerar_markdown(cruzamentos):
    markdown = "# Cruzamento de Destinos\n\n"
    for titulo, destinos in cruzamentos.items():
        markdown += f"## {titulo}\n"
        if destinos:
            markdown += "- " + "\n- ".join(destinos) + "\n\n"
        else:
            markdown += "- Nenhum destino encontrado.\n\n"
    return markdown

print(gerar_markdown(cruzar_destinos(extrair_destinos_por_sessao("Prova NP2 - Catálogo de Destinos - PyTravel.pdf"))))

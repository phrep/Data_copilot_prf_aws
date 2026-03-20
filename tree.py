import os

def mostrar_estrutura(pasta, prefixo=""):
    arquivos = sorted(os.listdir(pasta))
    
    for i, nome in enumerate(arquivos):
        caminho = os.path.join(pasta, nome)
        ultimo = i == len(arquivos) - 1
        
        if ultimo:
            print(prefixo + "└── " + nome)
            novo_prefixo = prefixo + "    "
        else:
            print(prefixo + "├── " + nome)
            novo_prefixo = prefixo + "│   "

        if os.path.isdir(caminho):
            mostrar_estrutura(caminho, novo_prefixo)


if __name__ == "__main__":
    pasta_raiz = "."  # diretório atual
    print("\n📂 Estrutura do Projeto:\n")
    mostrar_estrutura(pasta_raiz)
from langchain_qdrant import QdrantVectorStore
#from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings

from dotenv import load_dotenv
load_dotenv() # carrega sua API KEY da Open AI ou de outro fornecedor que você declarou no .env


def indexar_pdf(nome_colecao: str, docs: list):
    QdrantVectorStore.from_documents(
        documents=docs,
        embedding=HuggingFaceEmbeddings(model_name="BAAI/bge-base-en-v1.5"),
        url="http://localhost:6333",
        collection_name=nome_colecao,)

# CONEXAO COM A COLLECTION QDRANT 
def banco_qdrant(nome_colecao: str):
    db = QdrantVectorStore.from_existing_collection(
        collection_name=nome_colecao,
        url="http://localhost:6333",
        embedding=HuggingFaceEmbeddings(model_name="BAAI/bge-base-en-v1.5"),
    )
    return db


if __name__ == '__main__':
    from langchain_community.document_loaders import PyPDFLoader
    from langchain_text_splitters import RecursiveCharacterTextSplitter

    ## Exemplo de indexação usando o Qdrant Local.
    loader = PyPDFLoader(r"./databot.pdf")  # mudar aqui para o caminho do seu computador
    lista_documento_entrada = loader.load()

    ## Criando os Chunks
    text_splitter = RecursiveCharacterTextSplitter(separators=[""], chunk_size=1000, chunk_overlap=200)
    documentos = text_splitter.split_documents(lista_documento_entrada)

    ## Indexando os chunks no Qdrant:
    indexar_pdf("databot_collections", documentos)




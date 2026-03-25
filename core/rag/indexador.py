from langchain_qdrant import QdrantVectorStore
from langchain_huggingface import HuggingFaceEmbeddings

from dotenv import load_dotenv
load_dotenv()

# 🔥 IMPORTANTE: importar do seu loader
from core.rag.loader import criar_documentos_schema



# =========================
# EMBEDDING PADRÃO
# =========================
def get_embedding():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    )


# =========================
# INDEXAÇÃO GENÉRICA
# =========================
def indexar_documentos(nome_colecao: str, docs: list):

    QdrantVectorStore.from_documents(
        documents=docs,
        embedding=get_embedding(),
        url="http://13.222.175.92:6333",
        collection_name=nome_colecao,
    )


# =========================
# CONEXÃO COM QDRANT
# =========================
def banco_qdrant(nome_colecao: str):

    db = QdrantVectorStore.from_existing_collection(
        collection_name=nome_colecao,
        url="http://13.222.175.92:6333",
        embedding=get_embedding(),
    )

    return db


# =========================
# EXECUÇÃO
# =========================
if __name__ == '__main__':

    # 🔥 agora vem do loader
    documentos = criar_documentos_schema()

    indexar_documentos("prf_acidentes_schema", documentos)

    print("✅ Schema indexado no Qdrant com sucesso!")
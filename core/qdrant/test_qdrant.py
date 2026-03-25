from langchain_qdrant import QdrantVectorStore
from langchain_community.embeddings import HuggingFaceEmbeddings

db = QdrantVectorStore.from_existing_collection(
    collection_name="prf_acidentes_schema",
    url="http://13.222.175.92:6333",
    embedding=HuggingFaceEmbeddings(
        model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    )
)

resultado = db.similarity_search("quantidade de acidentes por estado")

for doc in resultado:
    print(doc.page_content)


if __name__ == "__main__":
    from qdrant_client import QdrantClient

    client = QdrantClient(url="http://13.222.175.92:6333")

    points = client.scroll(
        collection_name="prf_acidentes_schema",
        limit=5
    )

    print(points)
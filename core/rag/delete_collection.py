from qdrant_client import QdrantClient

client = QdrantClient(url="http://13.222.175.92:6333")

client.delete_collection("prf_acidentes_schema")

print("Collection deletada com sucesso!")
#

1. Indexador - 
    1.1 load do arquivo
    1.2 Cria os Chunks
    1.3 Indexa no banco Qdrant
2. Retriever
    2.1 ## Função auxiliar que formata o retorno do banco vetorial em uma string estruturada.
    2.2 ## Inicializando o Qdrant como banco vetorial:
    2.3

# RAG com Qdrant Local

Projeto de RAG usando:
- Qdrant (vector database local)
- LangChain
- Embeddings gratuitos (HuggingFace)
- PDFs como fonte de dados

## Setup

```bash
git clone https://github.com/phrep/rag_qdrant.git
cd rag_qdrant
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

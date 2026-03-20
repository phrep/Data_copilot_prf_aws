from dotenv import load_dotenv
load_dotenv()

from operator import itemgetter
import re
import pandas as pd
from functools import lru_cache

from langchain_groq.chat_models import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel
from langchain_core.output_parsers import StrOutputParser

from indexador import banco_qdrant
from connection import conn


# =========================
# LIMPAR SQL
# =========================
def limpar_sql(resposta: str) -> str:
    resposta = resposta.strip()
    resposta = re.sub(r"```sql|```", "", resposta)
    return resposta.strip()


# =========================
# VALIDAR SQL (SEGURANÇA)
# =========================
def validar_sql(sql: str):

    sql_upper = sql.upper()

    palavras_proibidas = [
        "DROP", "DELETE", "UPDATE", "INSERT",
        "ALTER", "TRUNCATE", "CREATE"
    ]

    for palavra in palavras_proibidas:
        if palavra in sql_upper:
            raise ValueError(f"❌ Query não permitida: contém '{palavra}'")

    if "SELECT" not in sql_upper:
        raise ValueError("❌ Apenas queries SELECT são permitidas")

    return True


# =========================
# EXECUTAR ATHENA
# =========================
@lru_cache(maxsize=50)
def executar_sql_cache(sql: str):
    print("⚡ Executando no Athena...")
    df = pd.read_sql(sql, conn)
    return df


# =========================
# FORMATAR CONTEXTO
# =========================
def cria_texto(documentos):
    return "\n\n".join(doc.page_content for doc in documentos)


# =========================
# QDRANT
# =========================
db = banco_qdrant("prf_acidentes_schema")
retriever = db.as_retriever(search_kwargs={"k": 6})


# =========================
# PROMPT
# =========================
prompt = """
Você é especialista em SQL para AWS Athena.

Tabela:
tabela_prf_all_acidentes_db

Contexto:
{contexto}

Regras:
- Use nomes exatos das colunas
- Use COUNT(*) para contagem
- Use CAST para mortos/feridos
- Filtre por ano e uf quando possível
- Retorne APENAS SQL
- Não explique nada
"""


prompt_template = ChatPromptTemplate([
    ("system", prompt),
    ("human", "{pergunta}")
])


model = ChatGroq(model="llama-3.3-70b-versatile")


# =========================
# CHAIN
# =========================
chain = (
    RunnableParallel({
        "pergunta": itemgetter("pergunta"),
        "contexto": itemgetter("pergunta") | retriever | cria_texto
    })
    | prompt_template
    | model
    | StrOutputParser()
)


# =========================
# FUNÇÃO PRINCIPAL
# =========================
def gerar_sql_e_consultar(pergunta: str):

    resposta_llm = chain.invoke({"pergunta": pergunta})

    sql = limpar_sql(resposta_llm)

    # 🔥 validação
    validar_sql(sql)

    # 🔥 cache
    df = executar_sql_cache(sql)

    return sql, df
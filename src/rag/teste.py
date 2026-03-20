from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import json

load_dotenv()

# =========================
# LLM
# =========================
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

# =========================
# SCHEMA
# =========================
schema = [
    {"Name": "id", "Type": "string"},
    {"Name": "pesid", "Type": "string"},
    {"Name": "data_inversa", "Type": "date"},
    {"Name": "municipio", "Type": "string"},
    {"Name": "causa_acidente", "Type": "string"},
    {"Name": "br", "Type": "string"},
    {"Name": "km", "Type": "double"},
    {"Name": "uf", "Type": "string"}
]

schema_str = json.dumps(schema, indent=2)

# =========================
# PROMPT (SEM f-string)
# =========================
prompt = ChatPromptTemplate.from_messages([
    ("system", """
Você é um assistente especialista em gerar consultas SQL para ATHENA AWS.

Tabela: ano_2025

Schema:
{schema}

Regras:
- Gere apenas SQL compatível com Athena (Presto/Trino)
- Use nomes de colunas exatamente como definidos
- Use aspas simples para strings
- Evite SELECT *
- Para rankings use COUNT(*) como métrica de acidentes
- Sempre use ORDER BY + LIMIT


Caso não saiba, responda:
"Não tenho informações suficientes para gerar essa consulta."

Retorne apenas a query SQL.
"""),
    ("human", "{pergunta}")
])

# =========================
# CHAIN
# =========================
chain = prompt | llm | StrOutputParser()

# =========================
# TESTE
# =========================
pergunta = "Top 10 trechos em SAO JOSE DOS CAMPOS com mais acidentes em 2025"

resposta = chain.invoke({
    "pergunta": pergunta,
    "schema": schema_str
})

print("Pergunta:", pergunta)
print("\nSQL gerado:\n")
print(resposta)
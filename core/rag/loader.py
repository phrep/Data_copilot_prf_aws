from langchain_core.documents import Document

TABLE_NAME = '"tabela_prf_all_acidentes_db"."acidentes"'

def criar_documentos_schema():
    documentos = []

    # =========================
    # CONTEXTO DA TABELA
    # =========================
    documentos.append(Document(
        page_content=f"""
Tabela: {TABLE_NAME}

Descrição:
Tabela contendo registros de acidentes em rodovias federais do Brasil.

Use esta tabela para análises de:
- quantidade de acidentes
- análises por estado (uf)
- análises temporais (ano, mês, dia)
- causas e tipos de acidentes
""",
        metadata={"type": "table_context"}
    ))

    # =========================
    # COLUNAS
    # =========================
    for col in schema_docs:
        texto = f"""
Coluna: {col['column']}
Descrição: {col['desc']}
Tabela: {TABLE_NAME}

Instruções:
- Use exatamente o nome da coluna: {col['column']}
- Esta coluna pertence à tabela {TABLE_NAME}
"""

        documentos.append(
            Document(
                page_content=texto,
                metadata={
                    "type": "column",
                    "column_name": col["column"],
                    "table": TABLE_NAME
                }
            )
        )

    # =========================
    # MÉTRICAS IMPORTANTES
    # =========================
    documentos.append(Document(
        page_content=f"""
Para calcular número de acidentes:

Use:
SELECT COUNT(*) FROM {TABLE_NAME}

Para agrupamentos:
SELECT coluna, COUNT(*) 
FROM {TABLE_NAME}
GROUP BY coluna
""",
        metadata={"type": "metric"}
    ))

    # =========================
    # REGRAS DE NEGÓCIO
    # =========================
    documentos.append(Document(
        page_content="""
As colunas mortos, feridos_leves e feridos_graves são do tipo string.

Sempre converter usando:
CAST(coluna AS INTEGER)

Exemplo:
SUM(CAST(mortos AS INTEGER))
""",
        metadata={"type": "rule"}
    ))

    documentos.append(Document(
        page_content="""
Sempre que possível, aplicar filtros para melhorar performance no Athena.

Priorizar:
- filtro por ano
- filtro por uf

Exemplo:
WHERE ano = 2023 AND uf = 'SP'
""",
        metadata={"type": "rule"}
    ))

    # =========================
    # EXEMPLOS DE SQL (🔥 MUITO IMPORTANTE)
    # =========================
    documentos.append(Document(
        page_content=f"""
Exemplo: quantidade de acidentes por estado

SELECT uf, COUNT(*) as total_acidentes
FROM {TABLE_NAME}
GROUP BY uf
""",
        metadata={"type": "sql_example"}
    ))

    documentos.append(Document(
        page_content=f"""
Exemplo: acidentes por ano

SELECT ano, COUNT(*) as total
FROM {TABLE_NAME}
GROUP BY ano
""",
        metadata={"type": "sql_example"}
    ))

    documentos.append(Document(
        page_content=f"""
Exemplo: total de mortos por estado

SELECT uf, SUM(CAST(mortos AS INTEGER)) as total_mortos
FROM {TABLE_NAME}
GROUP BY uf
""",
        metadata={"type": "sql_example"}
    ))

    return documentos


# =========================
# SCHEMA
# =========================
schema_docs = [
    {"column": "id", "desc": "Identificador único do acidente"},
    {"column": "data_inversa", "desc": "Data do acidente"},
    {"column": "dia_semana", "desc": "Dia da semana do acidente"},
    {"column": "horario", "desc": "Horário do acidente"},
    {"column": "br", "desc": "Rodovia BR onde ocorreu o acidente"},
    {"column": "km", "desc": "Quilômetro da rodovia onde ocorreu o acidente"},
    {"column": "municipio", "desc": "Município onde ocorreu o acidente"},
    {"column": "causa_acidente", "desc": "Descrição da causa do acidente"},
    {"column": "tipo_acidente", "desc": "Tipo do acidente"},
    {"column": "classificacao_acidente", "desc": "Gravidade do acidente"},
    {"column": "fase_dia", "desc": "Período do dia"},
    {"column": "condicao_metereologica", "desc": "Condição climática"},
    {"column": "tipo_pista", "desc": "Tipo da pista"},
    {"column": "uso_solo", "desc": "Uso do solo"},
    {"column": "tipo_veiculo", "desc": "Tipo de veículo"},
    {"column": "marca", "desc": "Marca do veículo"},
    {"column": "idade", "desc": "Idade da pessoa"},
    {"column": "sexo", "desc": "Sexo da pessoa"},
    {"column": "ilesos", "desc": "Quantidade de ilesos (string numérica)"},
    {"column": "feridos_leves", "desc": "Feridos leves (string numérica)"},
    {"column": "feridos_graves", "desc": "Feridos graves (string numérica)"},
    {"column": "mortos", "desc": "Mortos (string numérica)"},
    {"column": "latitude", "desc": "Latitude"},
    {"column": "longitude", "desc": "Longitude"},
    {"column": "regional", "desc": "Regional da PRF"},
    {"column": "delegacia", "desc": "Delegacia"},
    {"column": "uop", "desc": "Unidade operacional"},
    {"column": "mes", "desc": "Mês"},
    {"column": "ano", "desc": "Ano (partição)"},
    {"column": "uf", "desc": "Estado (UF)"}
]
from langchain_core.documents import Document

def criar_documentos_schema():
    documentos = []

    for col in schema_docs:
        texto = f"""
Coluna: {col['column']}
Descrição: {col['desc']}
Tabela: tabela_prf_all_acidentes_db

Observações:
- Use exatamente o nome da coluna: {col['column']}
"""

        documentos.append(
            Document(
                page_content=texto,
                metadata={
                    "type": "column",
                    "column_name": col["column"],
                    "table": "tabela_prf_all_acidentes_db"
                }
            )
        )

    # =========================
    # MÉTRICAS IMPORTANTES
    # =========================
    documentos.append(Document(
        page_content="Número de acidentes é calculado como COUNT(*)",
        metadata={"type": "metric"}
    ))

    documentos.append(Document(
        page_content="Campos mortos, feridos_leves e feridos_graves são string e devem ser convertidos usando CAST(... AS INTEGER)",
        metadata={"type": "rule"}
    ))

    documentos.append(Document(
        page_content="Sempre filtrar por ano e uf quando possível para melhorar performance no Athena",
        metadata={"type": "rule"}
    ))

    return documentos

schema_docs = [
    {"column": "id", "desc": "Identificador único do acidente"},
    {"column": "data_inversa", "desc": "Data do acidente"},
    {"column": "dia_semana", "desc": "Dia da semana do acidente"},
    {"column": "horario", "desc": "Horário do acidente"},
    {"column": "br", "desc": "Rodovia BR onde ocorreu o acidente"},
    {"column": "km", "desc": "Quilômetro da rodovia onde ocorreu o acidente"},
    {"column": "municipio", "desc": "Município onde ocorreu o acidente"},
    {"column": "causa_acidente", "desc": "Descrição da causa do acidente"},
    {"column": "tipo_acidente", "desc": "Tipo do acidente (colisão, saída de pista, etc)"},
    {"column": "classificacao_acidente", "desc": "Gravidade do acidente"},
    {"column": "fase_dia", "desc": "Período do dia (dia, noite, amanhecer, etc)"},
    {"column": "condicao_metereologica", "desc": "Condição climática no momento do acidente"},
    {"column": "tipo_pista", "desc": "Tipo da pista (simples, dupla, etc)"},
    {"column": "uso_solo", "desc": "Tipo de uso do solo na região (urbano, rural)"},
    {"column": "tipo_veiculo", "desc": "Tipo de veículo envolvido"},
    {"column": "marca", "desc": "Marca do veículo"},
    {"column": "idade", "desc": "Idade da pessoa envolvida"},
    {"column": "sexo", "desc": "Sexo da pessoa envolvida"},
    {"column": "ilesos", "desc": "Quantidade de pessoas ilesas (string numérica)"},
    {"column": "feridos_leves", "desc": "Quantidade de feridos leves (string numérica)"},
    {"column": "feridos_graves", "desc": "Quantidade de feridos graves (string numérica)"},
    {"column": "mortos", "desc": "Quantidade de mortos (string numérica, precisa CAST para int)"},
    {"column": "latitude", "desc": "Latitude do acidente"},
    {"column": "longitude", "desc": "Longitude do acidente"},
    {"column": "regional", "desc": "Regional da PRF"},
    {"column": "delegacia", "desc": "Delegacia responsável"},
    {"column": "uop", "desc": "Unidade operacional da PRF"},
    {"column": "mes", "desc": "Mês do acidente"},
    {"column": "ano", "desc": "Ano do acidente (partição)"},
    {"column": "uf", "desc": "Estado (UF) do acidente (partição)"}
]


if __name__ == '__main__':
    
    documentos = criar_documentos_schema()

    indexar_pdf("prf_acidentes_schema", documentos)

    print("Schema indexado no Qdrant com sucesso!")
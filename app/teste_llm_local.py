from core.rag.retriever import gerar_sql_e_consultar

pergunta = "quantos acidentes por estado em 2023?"

sql, df = gerar_sql_e_consultar(pergunta)

print("\nSQL GERADO:")
print(sql)

print("\nRESULTADO:")
print(df.head())
def top_km_acidentes(cidade, ano):
    query = f"""
    SELECT 
        km,
        COUNT(*) as total_acidentes
    FROM "2025_geral_db"."ano_2025"
    WHERE municipio = '{cidade}'
    AND year(data_inversa) = {ano}
    GROUP BY km
    ORDER BY total_acidentes DESC
    LIMIT 10
    """
    return query

def Consulta_bd(ano, uf, cidade):
    
    # deve selecionar o banco de dados de acordo com ano, uf e cidade e n'ao o 2025 fixo...
    # db2025_geral_db
    if ano == "2025":
        ano == 
    
    
    cidade 

    query = f"""
    SELECT 
        km,
        COUNT(*) as total_acidentes
    FROM "db{ano}_geral_db"."ano_2025"
    WHERE municipio = '{cidade}'
    AND year(data_inversa) = {ano}
    GROUP BY km
    ORDER BY total_acidentes DESC
    LIMIT 10
    """
    return query


import sys
from unittest.mock import MagicMock

# 🔥 MOCK DE TODAS DEPENDÊNCIAS EXTERNAS
sys.modules["langchain_groq"] = MagicMock()
sys.modules["langchain_groq.chat_models"] = MagicMock()

sys.modules["langchain_core"] = MagicMock()
sys.modules["langchain_core.prompts"] = MagicMock()
sys.modules["langchain_core.runnables"] = MagicMock()
sys.modules["langchain_core.output_parsers"] = MagicMock()

from unittest.mock import patch
from core.rag.retriever import gerar_sql_e_consultar


@patch("core.rag.retriever.chain.invoke")
@patch("core.rag.retriever.executar_sql_cache")
def test_gerar_sql_com_sucesso(mock_exec_sql, mock_chain):
    
    mock_chain.return_value = "SELECT * FROM tabela"
    
    mock_exec_sql.return_value = "fake_dataframe"

    sql, df = gerar_sql_e_consultar("quantos acidentes ocorreram por estado?")

    assert "SELECT" in sql
    assert df == "fake_dataframe"


@patch("core.rag.retriever.chain.invoke")
def test_sql_invalido(mock_chain):

    mock_chain.return_value = "DROP TABLE usuarios"

    sql, df = gerar_sql_e_consultar("pergunta perigosa")

    assert sql is None
    assert df is None
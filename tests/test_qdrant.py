import sys
from unittest.mock import MagicMock

sys.modules["langchain_groq"] = MagicMock()
sys.modules["langchain_groq.chat_models"] = MagicMock()
sys.modules["langchain_core"] = MagicMock()
sys.modules["langchain_core.prompts"] = MagicMock()
sys.modules["langchain_core.runnables"] = MagicMock()
sys.modules["langchain_core.output_parsers"] = MagicMock()

from core.rag.retriever import buscar_contexto

def test_buscar_contexto_tipo():

    contexto = buscar_contexto("acidentes por estado")

    assert isinstance(contexto, str)


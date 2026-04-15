import sys
from unittest.mock import MagicMock

# 🔥 LLM
sys.modules["langchain_groq"] = MagicMock()
sys.modules["langchain_groq.chat_models"] = MagicMock()

# 🔥 LANGCHAIN CORE
sys.modules["langchain_core"] = MagicMock()
sys.modules["langchain_core.prompts"] = MagicMock()
sys.modules["langchain_core.runnables"] = MagicMock()
sys.modules["langchain_core.output_parsers"] = MagicMock()
sys.modules["langchain_core.documents"] = MagicMock()

# 🔥 QDRANT
sys.modules["langchain_qdrant"] = MagicMock()
sys.modules["qdrant_client"] = MagicMock()

# 🔥 EMBEDDINGS
sys.modules["langchain_huggingface"] = MagicMock()

# 🔥 ATHENA (NOVO)
sys.modules["pyathena"] = MagicMock()

# -------------------------
# FIXTURES
# -------------------------
import os
import pytest
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture
def pergunta_exemplo():
    return "quantos acidentes ocorreram por estado?"

@pytest.fixture
def sql_exemplo():
    return "SELECT * FROM tabela LIMIT 10"
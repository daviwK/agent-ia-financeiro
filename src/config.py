"""Configurações do Nexus Din."""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
PROMPT_DIR = BASE_DIR / "prompts"

# Modelo local usado pelo Ollama.
OLLAMA_MODEL = "gpt-oss:20b"

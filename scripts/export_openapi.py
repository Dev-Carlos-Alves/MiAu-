# Script para exportar o schema OpenAPI para docs/openapi.json - [Carlos Eduardo]
import json
import os
import sys

# Garante o path raiz
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from backend.app_api import app

def main():
    print("Gerando docs/openapi.json a partir do FastAPI...")
    openapi_schema = app.openapi()
    docs_dir = os.path.join(ROOT, "docs")
    os.makedirs(docs_dir, exist_ok=True)
    json_path = os.path.join(docs_dir, "openapi.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(openapi_schema, f, indent=2, ensure_ascii=False)
    print(f"Salvo em {json_path}")

if __name__ == "__main__":
    main()

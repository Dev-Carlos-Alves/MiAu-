# Ponto de entrada principal para iniciar o Uvicorn com FastAPI local - [Carlos Eduardo]
import uvicorn
from dotenv import load_dotenv

load_dotenv()
import sys
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)



if __name__ == "__main__":
    print("="*50)
    print("INICIANDO SISTEMA COMPLETO MIAU (FULLSTACK)")
    print("="*50)
    print("Servidor Frontend e Backend unificados na mesma porta.")
    print("Acesse no navegador: http://127.0.0.1:8000")
    print("Docs / Swagger: http://127.0.0.1:8000/docs")
    print("="*50)
    
    # Inicia o FastAPI (que agora carrega tudo) na porta 8000 sem auto-reload
    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=False)

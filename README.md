[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE) ![Status](https://img.shields.io/badge/status-stable-brightgreen) ![Language](https://img.shields.io/badge/lang-PT-BR-brightgreen)

# 🐾 MiAu - Pet Shop & Bem-Estar

## 📌 Sobre o Projeto
O **MiAu** é um sistema de gestão para clínicas veterinárias e pet shops, desenvolvido como projeto acadêmico para a disciplina do professor Henning (Semestre 2026.1).

O projeto atual está implementado como um backend em **FastAPI** com autenticação JWT e uma interface frontend estática em **HTML/CSS/JavaScript**, servida pelo mesmo servidor.

## 🎯 Objetivos
- Digitalizar e centralizar o controle de clientes, pets, serviços, produtos e agendamentos.
- Oferecer uma API REST com documentação Swagger/OpenAPI.
- Permitir execução local simples via Python e MariaDB/MySQL.

## 🛠️ Tecnologias Utilizadas
- Python 3
- FastAPI
- Uvicorn
- PyMySQL
- Pydantic
- python-jose
- passlib[bcrypt]
- python-dotenv
- MariaDB / MySQL
- HTML/CSS/JavaScript estático para frontend

### Frontend (`frontend/`)
- **HTML5, CSS3 e JavaScript Vanilla** — Single Page Application (SPA) levíssima e rápida.
- **Arco Design System** — Referência de design para botões, inputs, modais e responsividade.
- **FontAwesome** — Ícones modernos e vetoriais para a interface.
- **UI Avatars** — Geração de avatares automáticos baseados no nome do usuário e tutores.

### Backend (`backend/`)
- **FastAPI** — Framework web moderno e de altíssimo desempenho para Python.
- **Pydantic** — Validação rigorosa de dados.
- **Uvicorn** — Servidor ASGI ultrarrápido para rodar a aplicação unificada.
- **PyMySQL** — Driver oficial para conexão direta com o banco de dados.
- **python-jose & passlib** — Autenticação segura via JWT (JSON Web Tokens) e hash de senhas (bcrypt).
- **python-dotenv** — Configuração do projeto orientada a variáveis de ambiente (`.env`).
- **MariaDB / MySQL** — Banco de dados relacional para persistência (esquema `miau_db`).

## 📦 Estrutura de Módulos (Features)
- 👤 **Autenticação e Perfil**: Login JWT, gestão de perfil e avatar.
- 🔔 **Sistema de Notificações**: Mural de avisos com badge numérico.
- 🏠 **Home / Mural**: Painel de avisos do sistema.
- 👥 **Tutores & Pets**: CRUD unificado com foto do tutor e accordion de pets.
- 🛍️ **Produtos**: Catálogo e controle de estoque de produtos (ração, brinquedos, medicamentos) com CRUD completo.
- 🏷️ **Serviços**: Catálogo comercial de banho, tosa, etc.
- 📅 **Agendamentos**: Cruzamento de tutores, pets e serviços.
- 📖 **API Docs**: Swagger UI gerado e integrado nativamente pelo FastAPI em `/docs`.

## 🚀 Como Executar o Projeto Localmente

### Estrutura do Projeto

```text
MiAu/
├── app.py                # Ponto de entrada unificado (inicia Uvicorn + Frontend estático)
├── backend/              # Lógica de negócio, Rotas da API, Schemas e Auth
├── frontend/             # Arquivos estáticos (HTML, CSS, JS, Imagens)
├── database/             # Schema SQL e script de reset do banco (setup_db.py)
├── docs/                 # Documentação complementar
└── venv/                 # Ambiente virtual Python
```

### 1. Pré-requisitos
- **Python 3.8+**
- Servidor **MariaDB/MySQL** local (porta 3306).

### 2. Configurar o Banco de Dados e Variáveis de Ambiente
Certifique-se de que o banco de dados está rodando. Opcionalmente, crie um arquivo `.env` na raiz do projeto com as seguintes chaves:
```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=root
DB_NAME=miau_db
DB_PORT=3306
JWT_SECRET_KEY=aumiau_super_secret_key_change_in_production
JWT_EXPIRE_MINUTES=120
```

Para inicializar as tabelas e o usuário administrador padrão, rode:
```bash
python database/setup_db.py
```

### 3. Instalar Dependências
Recomenda-se o uso de um ambiente virtual:
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate
pip install -r backend/requirements.txt
```

### 4. Executar a Aplicação
Inicie a aplicação utilizando o script principal que unifica o Backend (FastAPI) e o Frontend estático:
```bash
python app.py
```

### 5. Acessar o Sistema
| Recurso | URL |
|---------|-----|
| App Completa | http://127.0.0.1:8000 |
| Documentação da API (Swagger) | http://127.0.0.1:8000/docs |
| OpenAPI JSON | http://127.0.0.1:8000/openapi.json |

A documentação interativa Swagger é gerada automaticamente pelo FastAPI com base nas rotas e esquemas Pydantic configurados na pasta `backend/`.

**Autenticação no Swagger:**
1. Clique no botão **Authorize**.
2. Faça login com as credenciais padrão (`ShardCadu` / `cadu123`).
3. O token JWT será injetado automaticamente em todas as requisições subsequentes testadas pela interface.

---
## 🗄️ Banco de Dados
O script `database/setup_db.py` cria o banco `miau_db` e as tabelas:
- `usuarios`, `tutores`, `pets`, `servicos`, `produtos`, `agendamentos`, `avisos`

Também insere o usuário padrão:
- `username`: `ShardCadu`
- `email`: `cadu.sport@miau.com`
- `senha`: `cadu123`

## 📌 API e Swagger
A API tem rotas de autenticação em `/auth` e rotas CRUD sob `/api`.
Gerar documentação OpenAPI estática:
```bash
python scripts/export_openapi.py
```

## 👨‍💻 Contribuidores do MiAu
Desenvolvido, arquitetado e testado por: 
- **Bruno Souza**
- **Carlos Eduardo Alves**
- **Geraldo de Albuquerque**
- **João Paulo Paz**

**Recife - 2026**

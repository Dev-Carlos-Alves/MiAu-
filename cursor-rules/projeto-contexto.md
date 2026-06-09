# MiAu — Contexto do Projeto para Agentes

> Documento de contextualização para qualquer agente de IA trabalhando neste repositório.
> Leia este arquivo antes de implementar features, corrigir bugs ou fazer deploy.

## Visão Geral

**MiAu** é um sistema fullstack de gestão para clínicas veterinárias e pet shops. Projeto acadêmico da disciplina do professor Henning (Semestre 2026.1), desenvolvido por Carlos Eduardo (Cadu).

**Propósito:** substituir planilhas e processos manuais por um fluxo digital unificado para gestão de tutores, pets, serviços e agendamentos.

**Links:**
- Repositório: https://github.com/Dev-Carlos-Alves/MiAu-
- Deploy: https://mi-au.vercel.app

## Arquitetura

```
Browser (SPA vanilla)
    │ JWT Bearer
    ▼
FastAPI (porta 8000 local / serverless na Vercel)
    │ PyMySQL
    ▼
MariaDB / MySQL (miau_db)
```

**Modo local:** servidor unificado — FastAPI serve API + arquivos estáticos do frontend na mesma porta.

**Modo Vercel:** frontend estático na CDN + API Python serverless (`api/index.py`) + banco MySQL hospedado.

## Mapa de Pastas

| Caminho | Status | Descrição |
|---------|--------|-----------|
| `app.py` | **Ativo** | Entry point local — inicia Uvicorn na porta 8000 |
| `backend/main.py` | **Ativo** | FastAPI app completo (API + StaticFiles) para dev local |
| `backend/app_api.py` | **Ativo** | FastAPI app só API (sem static) para Vercel |
| `backend/routers/` | **Ativo** | Rotas auth e CRUD |
| `backend/auth.py` | **Ativo** | JWT, OAuth2, get_current_user |
| `backend/database.py` | **Ativo** | Conexão PyMySQL via env vars |
| `backend/schemas.py` | **Ativo** | Modelos Pydantic |
| `database/` | **Ativo** | schema.sql, setup_db.py, popular_teste.py |
| `frontend/` | **Ativo** | SPA (index.html, css/, js/, imagens/) |
| `api/index.py` | **Ativo** | Entry point serverless Vercel |
| `cursor-rules/` | **Ativo** | Documentação para agentes |
| `backend/app.js`, `backend/bin/` | Legado | Express.js — não usado no fluxo principal |
| `frontend/app.js`, `frontend/views/` | Legado | Express/EJS — não usado no fluxo principal |
| `script_cores.py` | Utilitário | Extrai paleta de cores da identidade visual |

## Módulos / Features

| Módulo | Status | Arquivos principais |
|--------|--------|---------------------|
| Autenticação JWT | Funcional | `auth_routes.py`, `frontend/js/api.js` |
| Perfil + Avatar | Funcional | `modal-perfil`, localStorage `aumiau_avatar` |
| Home / Mural | Parcial | Mural é HTML estático; tabela `avisos` sem API |
| Notificações | Mock | Array `mockNotifications` em `app.js` |
| Tutores CRUD | Parcial | List + delete OK; create modal não wired |
| Pets CRUD | Parcial | List + delete OK; create modal não wired; sem PUT backend |
| Serviços CRUD | Parcial | List + delete OK; falta create no frontend |
| Agendamentos CRUD | Parcial | List + delete OK; falta create no frontend |
| Produtos/Estoque | Não existe | Mencionado no README, não implementado |

## Fluxo de Autenticação

1. Login via `POST /auth/login` (form-urlencoded OAuth2)
2. Resposta: `{ access_token, token_type: "bearer" }`
3. Token salvo em `localStorage['aumiau_token']`
4. Todas as chamadas API usam `apiFetch()` com header `Authorization: Bearer {token}`
5. Em 401: token removido e página recarregada

**Credenciais padrão (dev):** `ShardCadu` / `cadu123`

## Endpoints da API

### Auth (`/auth`)

| Método | Path | Auth | Descrição |
|--------|------|------|-----------|
| POST | `/auth/register` | Não | Criar usuário |
| POST | `/auth/login` | Não | Login OAuth2 form |
| GET | `/auth/me` | Sim | Perfil atual |
| PUT | `/auth/me` | Sim | Atualizar perfil |

### CRUD (`/api` — todas exigem JWT)

| Recurso | GET | POST | PUT | DELETE |
|---------|-----|------|-----|--------|
| `/api/tutores` | Sim | Sim | Sim (`/{id}`) | Sim |
| `/api/pets` | Sim | Sim | **Não** | Sim |
| `/api/servicos` | Sim | Sim | **Não** | Sim |
| `/api/agendamentos` | Sim | Sim | **Não** | Sim |
| `/api/avisos` | **Não existe** | — | — | — |

Documentação interativa: `/docs` (Swagger), `/redoc`

## Convenções de Código

### Frontend

- **Views:** `#login-view`, `#app-view` (toggle com `.hidden`)
- **Sections:** `#sec-{nome}` + nav link `data-target="{nome}"`
- **Modals:** `#modal-{nome}`, forms `#form-{nome}`
- **Tables:** `#tbody-{modulo}`
- **Form fields:** `{entity}-{field}` (ex: `tutor-nome`, `agen-data_hora`)
- **API client:** objeto global `API` com métodos camelCase em `frontend/js/api.js`
- **localStorage keys:** `aumiau_token`, `aumiau_avatar`

### Backend

- Routers em `backend/routers/` com `APIRouter`
- Dependency injection: `Depends(get_db)`, `Depends(get_current_user)`
- SQL raw com PyMySQL (`%s` placeholders)
- Schemas Pydantic em `backend/schemas.py`

## Como Executar Localmente

```bash
pip install -r backend/requirements.txt
python database/setup_db.py
python app.py
# Acesse http://127.0.0.1:8000
```

## Variáveis de Ambiente

Ver `.env.example` na raiz. Defaults permitem rodar local sem `.env`.

| Variável | Default local | Descrição |
|----------|---------------|-----------|
| `DB_HOST` | `localhost` | Host do MySQL |
| `DB_USER` | `root` | Usuário do banco |
| `DB_PASSWORD` | `root` | Senha do banco |
| `DB_NAME` | `miau_db` | Nome do database |
| `JWT_SECRET_KEY` | (dev key) | Secret para JWT — **obrigatório trocar em produção** |

## Dívidas Técnicas / Backlog

Prioridade para agentes futuros:

1. **CRUD frontend incompleto** — wire submit dos modais em `app.js`; adicionar `createServico`/`createAgendamento` em `api.js`
2. **PUT pets** — backend não tem rota; frontend tem `updatePet` unused
3. **API avisos** — tabela existe, mural estático, notificações mock
4. **Senhas texto puro** — `passlib[bcrypt]` listado mas não usado
5. **Logo ausente** — `index.html` referencia `logo_aumiau.png`; só existe `logo_completo_miau.png`
6. **Módulo produtos/estoque** — mencionado no README, não implementado
7. **Hash de senhas** — implementar bcrypt em produção

## Deploy

Ver [`deploy-vercel.md`](deploy-vercel.md) para instruções completas de deploy na Vercel.

## Documentação Relacionada

- [`design-system.md`](design-system.md) — guia visual do frontend
- [`conversas-cadu-cursor.md`](conversas-cadu-cursor.md) — histórico de conversas com agentes

# Dashboard Clima

Dashboard de previsão do tempo com busca de cidade, temperatura atual e gráfico de máximas/mínimas da semana.

## Stack

- **Backend:** Python (Flask), consumindo a [OpenWeatherMap API](https://openweathermap.org/api)
- **Frontend:** HTML, CSS e JavaScript puro, com [Chart.js](https://www.chartjs.org/) para os gráficos

## Funcionalidades

- Temperatura atual, máxima e mínima do dia
- Previsão dos próximos dias em cards
- Gráfico de máximas e mínimas da semana
- Busca de cidade com lista de sugestões (geocoding)

## Estrutura do projeto

```
dashboard-clima/
├── backend/
│   ├── app.py
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── .env
└── .gitignore
```

## Rotas do backend

| Rota | Parâmetros | Descrição |
|---|---|---|
| `GET /geo` | `q` | Busca cidades pelo nome (geocoding) |
| `GET /clima/atual` | `lat`, `lon` | Clima atual de uma coordenada |
| `GET /clima/previsao` | `lat`, `lon` | Previsão de 5 dias (blocos de 3h) |
| `GET /clima` | `cidade`, `estado`, `pais` | Rota simples de teste: busca cidade + clima em uma chamada só |

## Como rodar

### Backend

```bash
cd backend
pip install -r requirements.txt
python app.py
```

Crie um arquivo `.env` na raiz do projeto (mesmo nível de `backend/` e `frontend/`) com sua chave da OpenWeatherMap:

```
API_KEY=sua_chave_aqui
```

A chave gratuita pode ser gerada em [openweathermap.org/api](https://openweathermap.org/api).

### Frontend

Abra `frontend/index.html` diretamente no navegador, com o backend rodando em `http://localhost:5000`.

## Autores

- [Enzo Biagiotti](https://github.com/enzobiagiotti) — frontend
- [Leonardo Novaes](https://github.com/leonardonovaes) — backend

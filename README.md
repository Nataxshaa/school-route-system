# School Route System 🚍

Sistema web para monitoramento inteligente de rotas de transporte escolar, desenvolvido em Python utilizando Bottle.

## 📌 Objetivo

O projeto tem como objetivo auxiliar empresas de transporte escolar no acompanhamento das rotas em tempo real, ajudando a reduzir atrasos causados por trânsito, acidentes e mudanças no trajeto.

Além disso, o sistema busca melhorar a comunicação entre empresa, motoristas e responsáveis pelos alunos.

---

## 💡 Problema

Atualmente, um dos maiores desafios no transporte escolar é:

- atrasos inesperados;
- dificuldade em acompanhar as vans;
- excesso de mensagens dos responsáveis;
- falta de visualização centralizada das rotas.

O sistema surge como uma solução para monitoramento e organização logística.

---

## 🚀 Funcionalidades planejadas

- [x] Estrutura inicial da aplicação web
- [x] Configuração do Bottle
- [x] Sistema de rotas
- [x] Renderização de templates (`.tpl`)
- [ ] Dashboard principal
- [ ] Sistema de login
- [ ] Cadastro de vans
- [ ] Cadastro de motoristas
- [ ] Cadastro de alunos
- [ ] Banco de dados
- [ ] Integração com mapas/API
- [ ] Estimativa de chegada
- [ ] Monitoramento em tempo real
- [ ] Alertas de trânsito e atrasos

---

## 🛠️ Tecnologias utilizadas

- Python
- Bottle
- HTML5
- CSS3
- JavaScript
- Git/GitHub

---

## 📂 Estrutura do projeto

  ```text
school-route-system/
│
├── main.py
├── views/
│   └── page.tpl
│
├── static/
│   ├── css/
│   ├── js/
│   └── img/
│
├── venv/
├── .gitignore
└── README.md
```

## ▶️ Como executar o projeto

### 1. Clonar o repositório

```bash
git clone <url-do-repositorio>
```

### 2. Entrar na pasta do projeto

```bash
cd school-route-system
```

### 3. Criar ambiente virtual

```bash
python -m venv venv
```

### 4. Ativar ambiente virtual

Linux/macOS:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### 5. Instalar dependências

```bash
pip install -r requirements.txt
```

### 6. Executar aplicação

```bash
python main.py
```

### 7. Abrir no navegador

```text
http://localhost:8080
```

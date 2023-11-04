# API Leitor de Cupons Fiscais

API RESTful desenvolvida em Flask para processamento e gerenciamento de notas fiscais através de OCR.

## Descrição

A aplicação é uma API que permite que vendedores capturem notas fiscais através de uma foto. A API utiliza um serviço de OCR (ainda em desenvolvimento) para extrair os dados da nota e atualizá-los no banco de dados. A aplicação utiliza jobs com Redis e utiliza Docker para conteinerizar apenas os serviços de Redis e PostgreSQL, facilitando o desenvolvimento e a implantação.

![Arquitetura CuponsFiscais](https://i.imgur.com/0dCUlk9.png)

## Tecnologias Utilizadas

- **Flask**: Framework web para construir a API.
- **Flask-Cors**: Para permitir o acesso à API através de diferentes domínios.
- **Flask-JWT-Extended**: Para autenticação via JSON Web Tokens.
- **Flask-Restx**: Para uma organização melhor da API e documentação automática.
- **Celery**: Para gerenciamento de tarefas assíncronas com Redis.
- **Docker**: Utilizado para conteinerizar os serviços de PostgreSQL e Redis.
- **PostgreSQL**: Como sistema de gerenciamento de banco de dados.
- **Redis**: Como broker de mensagens para tarefas assíncronas.


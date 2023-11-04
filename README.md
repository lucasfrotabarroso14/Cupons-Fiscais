# API Leitor de Cupons Fiscais

API RESTful desenvolvida em Flask para processamento e gerenciamento de notas fiscais através de OCR.

## Descrição

CuponsFiscais é uma API que permite que vendedores capturem notas fiscais através de uma foto. A API utiliza um serviço de OCR (ainda em desenvolvimento) para extrair os dados da nota e atualizá-los no banco de dados. A aplicação utiliza jobs com Redis e é conteinerizada com Docker para facilitar o desenvolvimento e a implantação.

## Tecnologias Utilizadas

- **Flask**: Framework web para construir a API.
- **Flask-Cors**: Para permitir o acesso à API através de diferentes domínios.
- **Flask-JWT-Extended**: Para autenticação via JSON Web Tokens.
- **Flask-Restx**: Para uma organização melhor da API e documentação automática.
- **Celery**: Para gerenciamento de tarefas assíncronas com Redis.
- **Docker**: Para conteinerização dos serviços da aplicação.
- **PostgreSQL**: Como sistema de gerenciamento de banco de dados.
- **Redis**: Como broker de mensagens para tarefas assíncronas.


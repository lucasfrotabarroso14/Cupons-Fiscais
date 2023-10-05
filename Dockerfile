# Use uma imagem base do PostgreSQL
FROM postgres:latest

# Defina variáveis de ambiente para o PostgreSQL (altere conforme necessário)
ENV POSTGRES_DB projeto-cupons-Jsleiman
ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD 051415

# Copie um script SQL para ser executado quando o contêiner for iniciado (opcional)
COPY init.sql /docker-entrypoint-initdb.d/

# Exponha a porta padrão do PostgreSQL (opcional, mas pode ser útil para acesso externo)
EXPOSE 5432

# Inicialize o PostgreSQL
CMD ["postgres"]

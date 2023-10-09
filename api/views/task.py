from celery import Celery

# Crie uma instância do Celery
celery = Celery(
    'myapp',  # Nome do aplicativo Celery
    broker='redis://localhost:6379/0',  # URL do broker (pode ser Redis, RabbitMQ, etc.)
    backend='redis://localhost:6379/1'  # URL do backend para resultados
)

# Defina a tarefa Celery
@celery.task
def add_numbers(a, b):
    return a + b

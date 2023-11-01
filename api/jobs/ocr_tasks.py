from celery import Celery
import time
from celery.result import AsyncResult
# Crie uma instância do Celery
from config import execute_query

celery = Celery(
    'myapp',  # Nome do aplicativo Celery
    broker='redis://localhost:6379/0',  # URL do broker (pode ser Redis, RabbitMQ, etc)
    backend='redis://localhost:6379/1'  # URL do backend para resultados
)

status_cr_dict = {}
def realizar_ocr(cupom_id):
    try:
        time.sleep(10)
        # Retorna um resultado fictício após o atraso
        return
    except Exception as e:
        atualizar_status_ocr(cupom_id, "Falhou", str(e))
        raise

@celery.task
def processar_ocr(cupom_id):

    try:
        atualizar_status_ocr(cupom_id,"Em processamento","mudou")
        atualizar_status_ocr(cupom_id,"Concluido","mudou")
        return

    except Exception as e:
        atualizar_status_ocr(cupom_id,"Falhou",str(e))
        return


def atualizar_status_ocr(cupom_id, status_ocr, resultado_ocr):
    query = """
    UPDATE cupons
    SET 
    status_ocr = %s,
    resultado_ocr = %s
    WHERE id = %s
    """
    params = (status_ocr, resultado_ocr, cupom_id)
    execute_query(query, params)



# @celery.task
# def check_task_status(task_id):
#     result = AsyncResult(task_id)
#     if result.ready():
#         return {
#             'status': 'completed',
#             'result': result.result
#         }
#     elif result.failed():
#         return {
#             'status': 'failed',
#             'error_message': result.traceback
#         }
#     else:
#         return {
#             'status': 'pending'
#         }
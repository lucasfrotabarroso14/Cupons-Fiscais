import base64
from api.jobs.ocr_tasks import processar_ocr
from config import execute_query


def get_cupom_sem_foto():
    query = """
    SELECT 
    *
    FROM 
    cupons
    WHERE
    imagem IS NULL

    """
    result, status = execute_query(query, {})
    if status:
        return result, 200
    else:
        return [], 404
import base64


from api.jobs.ocr_tasks import processar_ocr
from config import execute_query


def get_cupons_pendentes_ocr():
    query = """
    SELECT * FROM CUPONS
    WHERE
    status_ocr = 'Pendente'
    """
    result, status = execute_query(query, {})
    if status:
        return result, 200
    else:
        return [], 404


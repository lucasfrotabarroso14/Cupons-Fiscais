import base64


from api.jobs.ocr_tasks import processar_ocr
from config import execute_query

def get_all():
    query = """
    SELECT
    *
    FROM
    
    cupons
    """
    result, status = execute_query(query,{})
    if status:
        return result, 200

    else:
        return [], 404






def base64_to_blob(base_64_string):
    try:
        binary_data = base64.b64decode(base_64_string)
        blob = bytes(binary_data)
        return blob

    except Exception as e:
        print(e)
        return None




def deletar_cupom(id):
    query = """
    DELETE FROM
    cupons
    WHERE
    id = %(id)s
    """

    params = {"id": id}
    result,status = execute_query(query,params)

    if status:
        return "Usuário removido com sucesso.", 200
    else:
        return [], 404

def get_by_id(id):
    query = """
    SELECT
    *
    FROM
    cupons
    WHERE
    id = %(id)s
    """
    params={"id": id}
    result, status = execute_query(query, params)

    if status:
        return result, 200
    else:
        return [], 404

def update(id, obj):
    query = """
    UPDATE 
    cupons
    SET
            bandeira_do_cartao = %s,
            imagem = %s,
            forma_de_pagamento = %s,
            codigo_pedido_interno = %s,
            status = %s,
            nsu = %s,
            autorizacao = %s,
            codigo_filial = %s,
            codigo_gerente = %s,
            codigo_vendedor = %s,
            data_hora_upload = %s ,
            data_hora_aceite = %s
            
        WHERE
        id = %s
    """
    params = (
    obj["bandeira_do_cartao"],
    obj["imagem"],
    obj["forma_de_pagamento"],
    obj['codigo_pedido_interno'],
    obj['status'],
    obj['nsu'],
    obj['autorizacao'],
    obj['codigo_filial'],
    obj['codigo_gerente'],
    obj['codigo_vendedor'],
    obj['data_hora_upload'],
    obj['data_hora_aceite'],
    id
    )



    result, status = execute_query(query, params)

    if status:
        query = """
        SELECT
         * 
         FROM
        cupons 
        WHERE 
        id = %s
        """

        params = (id,)
        result , status = execute_query(query, params)
        return result[0], 200
    else:
        return 'Erro ao ao atualizar o registro.', 404












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


def post_ocr(cupom_obj):
    # cupom_obj['imagem'] = base64_to_blob(cupom_obj['imagem'])
    # Query para inserir um novo cupom, excluindo a coluna "id" que é autoincrementada
    query_insert = """
    INSERT INTO cupons
    (bandeira_do_cartao, imagem, forma_de_pagamento, codigo_pedido_interno, status, nsu, autorizacao, codigo_filial, codigo_gerente, codigo_vendedor, data_hora_upload, data_hora_aceite, status_ocr, resultado_ocr)
    VALUES
    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    RETURNING id;

    """


    params = (
        cupom_obj["bandeira_do_cartao"],
        cupom_obj["imagem"],
        cupom_obj["forma_de_pagamento"],
        cupom_obj["codigo_pedido_interno"],
        cupom_obj["status"],
        cupom_obj["nsu"],
        cupom_obj["autorizacao"],
        cupom_obj["codigo_filial"],
        cupom_obj["codigo_gerente"],
        cupom_obj["codigo_vendedor"],
        cupom_obj["data_hora_upload"],
        cupom_obj["data_hora_aceite"],
        cupom_obj["status_ocr"],
        cupom_obj["resultado_ocr"]
    )

    result, status = execute_query(query_insert, params)



    if status:
        cupom_id = result
        # processar_ocr.apply_async(args=[cupom_id], countdown=10)
        processar_ocr(cupom_id)


        # Recupere o dado inserido com base em algum critério exclusivo, como o horário de inserção
        query = """
           SELECT
           *
           FROM
           cupons
           WHERE
           id = %(id)s
           """
        params = {"id": cupom_id}


        result, status = execute_query(query, params)

        if status:
            return result[0], 201
        else:
            return "Erro: Falha ao inserir o dado.", 404





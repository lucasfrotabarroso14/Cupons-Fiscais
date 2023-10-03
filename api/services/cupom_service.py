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
    result, status = execute_query(query,{})
    if status:
        return result, 200
    else:
        return [], 404


def registrar_cupom(cupom_obj):
    # Query para inserir um novo cupom, excluindo a coluna "id" que é autoincrementada
    query_insert = """
    INSERT INTO cupons
    (bandeira_do_cartao, imagem, forma_de_pagamento, codigo_pedido_interno, status, nsu, autorizacao, codigo_filial, codigo_gerente, codigo_vendedor, data_hora_upload, data_hora_aceite)
    VALUES
    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);

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
        cupom_obj["data_hora_aceite"]
    )

    result, status = execute_query(query_insert, params)

    if status:
        # Recupere o dado inserido com base em algum critério exclusivo, como o horário de inserção
        query_select = """
        SELECT * FROM cupons WHERE data_hora_upload = %s;
        """
        select_params = (cupom_obj["data_hora_upload"],)

        result, status = execute_query(query_select, select_params)

        if status:
            return result[0], 201
        else:
            return "Erro: Falha ao inserir o dado.", 404

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












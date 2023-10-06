-- Exemplo de init.sql
CREATE TABLE cupons (
    codigo_filial TEXT,
    codigo_gerente TEXT,
    codigo_vendedor TEXT,
    codigo_pedido_interno TEXT,
    data_hora_upload TIMESTAMP,
    status CHAR(1),
    imagem BYTEA,
    data_hora_aceite TIMESTAMP,
    nsu TEXT,
    autorizacao TEXT,
    bandeira_do_cartao TEXT,
    forma_de_pagamento TEXT
);

create table cotacao_dolar (
 id serial primary key,
 data date,
 hora time,
 cotacao decimal(10,2)
)

CREATE OR REPLACE PROCEDURE inserir_valores(data_atual date, hora_atual time, dolar_atual decimal)
LANGUAGE 'plpgsql' AS
$$
BEGIN
    INSERT INTO cotacao_dolar (data, hora, cotacao)
    VALUES (data_atual, hora_atual, dolar_atual);
END;
$$
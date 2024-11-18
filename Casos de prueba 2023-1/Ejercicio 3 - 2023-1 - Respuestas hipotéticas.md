# Contexto ejercicio 3

### Enunciado
```
Retornar una tabla con los nombres de los clientes que han comprado la
mayor cantidad de tickets.
```

### Respuesta correcta
```
select t3.nombre
from ( select max(nro_tickets) as max_tickets
       from ( select cliente.id, count(ticket.id) as nro_tickets 
              from cliente, ticket
              where ticket.refcliente = cliente.id 
              group by cliente.id) as t1) as t2,
     ( select cliente.id, cliente.nombre, count(ticket.id) as nro_tickets 
       from cliente, ticket
       where ticket.refcliente = cliente.id
       group by cliente.id, cliente.nombre) as t3
where t3.nro_tickets = t2.max_tickets
```

### Tabla esperada
```
|nombre|
|------|
|Alex  |
|Juan  |
```





# Respuestas hipotéticas (Casos de prueba)

# Correcta o incorrecta

Correcta
```
SELECT cliente.nombre
FROM cliente
INNER JOIN ticket ON ticket.refcliente = cliente.id
GROUP BY cliente.id, cliente.nombre
HAVING COUNT(ticket.id) = (
    SELECT MAX(nro_tickets)
    FROM (
        SELECT COUNT(ticket.id) AS nro_tickets
        FROM cliente
        INNER JOIN ticket ON ticket.refcliente = cliente.id
        GROUP BY cliente.id
    ) AS t
);
```

Tabla
```
|nombre|
|------|
|Alex  |
|Juan  |
```


Incorrecta
```
SELECT cliente.nombre, count(ticket.id) as ticket
FROM cliente
INNER JOIN ticket ON ticket.refcliente = cliente.id
group by cliente.nombre
Order by ticket DESC
Limit 1;
```

Tabla
```
|nombre|ticket|
|------|------|
|Alex  |6     |
```

### Resultado esperado
Para correcta
```
El modelo fue capaz de reconoser que la respuesta del alumno fue correcta
```

Para incorrecta
```
El modelo fue capaz de reconoser que la respuesta del alumno fue incorrecta
```






# Respuesta incorrecta con errores específicos

Respuesta
```
SELECT cliente.nombre
FROM cliente
INNER JOIN ticket ON ticket.refcliente = cliente.id
GROUP BY cliente.id, cliente.nombre
HAVING COUNT(ticket.id) <> (
    SELECT MIN(nro_tickets)
    FROM (
        SELECT COUNT(ticket.id) AS nro_tickets
        FROM cliente
        INNER JOIN ticket ON ticket.refcliente = cliente.id
        GROUP BY cliente.id
    ) AS t
);
```

Tabla
```
|nombre|
|------|
|Ivan  |
|Alex  |
|Aldo  |
|Oscar |
|Welton|
|Juan  |
```

#### Errores:
-  uso de <>, para buscar diferentes a el minimo de tiquets 
-  uso de min para buscar minimo en vez de maximo
### Resultado esperado
```
El modelo fue capaz de identificar todos los errores correctamente
```





#  Respuesta con errores de sintaxis

```
SELECT cliente.nombre
FROM cliente
INNER JOIN ticket ON ticket.refcliente == cliente.id
GROUP BY cliente.id, cliente.nombre;
WHERE COUNT(ticket.id) == (
    SELECT MAX(nro_tickets)
    FROM (
        SELECT COUNT(ticket.id) AS nro_tickets
        FROM cliente
        INNER JOIN ticket ON ticket.refcliente = cliente.id
        GROUP BY cliente.id
    ) AS t
)
```

### Errores:
- Where en vez de having
- Doble igual
- Punto y coma mal puesto

### Resultado esperado
```
El modelo fue capaz de identificar el error y proporcionar la solucion para ejecutar la consulta
```







# Sugerir respuesta a consulta incorrecta

```
SELECT cliente.nombre
FROM cliente
INNER JOIN ticket ON ticket.refcliente = cliente.id
GROUP BY cliente.id, cliente.nombre
HAVING COUNT(ticket.id) <> (
    SELECT MIN(nro_tickets)
    FROM (
        SELECT COUNT(ticket.id) AS nro_tickets
        FROM cliente
        INNER JOIN ticket ON ticket.refcliente = cliente.id
        GROUP BY cliente.id
    ) AS t
);
```
### Respuesta esperada
```
El modelo fue capaz de sugerir consulta que resuelve el ejercicio
```





# Respuesta correcta, pero con elementos Innecesarios

Correcta
```
SELECT cliente.nombre
FROM cliente
INNER JOIN ticket ON ticket.refcliente = cliente.id
GROUP BY cliente.id, cliente.nombre
HAVING COUNT(ticket.id) = (
    SELECT MAX(nro_tickets)
    FROM (
        SELECT COUNT(ticket.id) AS nro_tickets
        FROM cliente
        INNER JOIN ticket ON ticket.refcliente = cliente.id
        GROUP BY cliente.id
    ) AS t
)
ORDER BY cliente.nombre DESC
LIMIT 100000;
```

Tabla
```
|nombre|
|------|
|Alex  |
|Juan  |
```
#### Elementos:
-  Order by inesesario
-  Limit 10000 sin sentido
### Resultado esperado
```
El modelo fue capaz de identificar todos los elementos innecesarios
```




# Extras

## Explicar paso a paso con palabras simple la manera de abordar el problema
```
El modelo fue capaz de explicar correctamente el problema paso a paso
```

## Generar consulta SQL para solucionar el problema
```
El modelo fue capaz de generar una consulta sql para solucionar el problema
```

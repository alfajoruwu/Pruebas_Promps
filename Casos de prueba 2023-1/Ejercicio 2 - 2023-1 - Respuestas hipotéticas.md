# Contexto ejercicio 2

### Enunciado
```
Retornar una tabla con los atributos “nombre_cliente” y “nro_destinos”, la cual muestra, para cada cliente, el número de destinos (distintos) a los
cuales ha viajado.
```

### Respuesta correcta
```
select cliente.nombre, count(distinct viaje.destino) 
from cliente, viaje, ticket
where 
ticket.refviaje = viaje.id and
ticket.refcliente = cliente.id
group by cliente.id, cliente.nombre
```

### Tabla esperada
```
|nombre |count|
|-------|-----|
|Juan   |3    |
|Ivan   |2    |
|Alex   |3    | 
|Oscar  |2    |
|Gerardo|2    |
|William|2    |
|Welton |3    |
|Aldo   |3    |
```






# Respuestas hipotéticas (Casos de prueba)

# Correcta o incorrecta

Correcta
```
SELECT cliente.nombre, COUNT(DISTINCT viaje.destino)
FROM cliente
INNER JOIN ticket ON ticket.refcliente = cliente.id
INNER JOIN viaje ON ticket.refviaje = viaje.id
GROUP BY cliente.id, cliente.nombre;

```

Tabla
```
|nombre  |count|
|--------|-----|
|Juan    | 3   |
|Ivan    | 2   |
|Alex    | 3   | 
|Oscar   | 2   |
|Gerardo | 2   |
|William | 2   |
|Welton  | 3   |
|Aldo    | 3   |
```


Incorrecta
```
select cliente.nombre, count(viaje.destino) 
from cliente, viaje, ticket
where 
ticket.refviaje = viaje.id and
ticket.refcliente = cliente.id
group by cliente.nombre;
```

Tabla
```
|nombre  |count|
|--------|-----|
|William |2    |
|Oscar   |4    |
|Alex    |6    |
|Gerardo |2    |
|Ivan    |4    |
|Juan    |6    |
|Aldo    |3    |
|Welton  |3    |
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






# Respuesta incorrecta con errores lógicos

Respuesta
```
select cliente.nombre, count(viaje.destino) 
from cliente, viaje, ticket
where 
ticket.refviaje = viaje.id and
ticket.refcliente = cliente.id
group by cliente.nombre;
```

Tabla
```
|nombre  |count|
|--------|-----|
|William |2    |
|Oscar   |4    |
|Alex    |6    |
|Gerardo |2    |
|Ivan    |4    |
|Juan    |6    |
|Aldo    |3    |
|Welton  |3    |
```

#### Errores:
-  No selecciona los viajes distintos
### Resultado esperado
```
El modelo fue capaz de identificar todos los errores correctamente
```



# Respuesta con errores de sintaxis

```
SELECT cliente.nombre, COUNT DISTINCT viaje.destino
FROM cliente
INNER JOIN ticket ticket.refcliente == cliente.id
INNER JOIN viaje ticket.refviaje == viaje.id
GROUP BY cliente.id, cliente.nombre;
```

### Errores:
- sin parentesis
- Doble igual
- Falta ON para JOIN
### Resultado esperado
```
El modelo fue capaz de identificar el o los errores y proporcionar la solucion para ejecutar la consulta
```





# Sugerir respuesta a consulta incorrecta

```
select cliente.nombre, count(viaje.destino) 
from cliente, viaje, ticket
where 
ticket.refviaje = viaje.id and
ticket.refcliente = cliente.id
group by cliente.nombre;
```
### Respuesta esperada
```
El modelo fue capaz de sugerir consulta que resuelve el ejercicio
```





# Respuesta correcta, pero con elementos Innecesarios

Correcta
```
SELECT cliente.nombre, COUNT(DISTINCT viaje.destino)
FROM cliente
INNER JOIN ticket ON ticket.refcliente = cliente.id
INNER JOIN viaje ON ticket.refviaje = viaje.id
WHERE cliente.edad < 100
GROUP BY cliente.id, cliente.nombre
ORDER BY cliente.nombre;

```

Tabla
```
|nombre |count|
|-------|-----|
|Aldo   |3    |
|Alex   |3    |
|Gerardo|2    |
|Ivan   |2    |
|Juan   |3    |
|Oscar  |2    |
|Welton |3    |
|William|2    |
```
#### Elementos:
-  Order By sin sentido
-  Where sin sentido
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

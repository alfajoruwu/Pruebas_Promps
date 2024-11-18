# Contexto ejercicio 1

### Enunciado
```
Retornar una tabla con los nombres de las ciudades que han sido el destino
de los viajes del cliente “Juan”. No repetir los nombres de ciudad.
```

### Respuesta correcta
```
select distinct viaje.destino 
from cliente, viaje, ticket
where 
ticket.refviaje = viaje.id and
ticket.refcliente = cliente.id and
cliente.nombre = 'Juan'
```

### Tabla esperada
```
| destino |
| ------- |
| Curicó  |
| Linares |
| Talca   |
```



# Respuestas hipotéticas (Casos de prueba)

# Correcta o incorrecta

Correcta
```
SELECT DISTINCT viaje.destino
FROM cliente
JOIN ticket ON ticket.refcliente = cliente.id
JOIN viaje ON ticket.refviaje = viaje.id
WHERE cliente.nombre = 'Juan';

```

Tabla
```
| destino |
| ------- |
| Curicó  |
| Linares |
| Talca   |
```


Incorrecta
```
SELECT viaje.destino
FROM cliente
JOIN ticket ON ticket.refcliente = cliente.id
JOIN viaje ON ticket.refviaje = viaje.id
WHERE cliente.nombre = 'Juan';

```

Tabla
```
| destino |
|---------|
| Talca   |
| Curicó  |
| Talca   |
| Curicó  |
| Linares |
| Curicó  |
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




# Respuesta incorrecta con errores (lógicos)

Respuesta
```
SELECT viaje.origen 
FROM cliente
JOIN ticket ON ticket.refcliente = cliente.id
JOIN viaje ON ticket.refviaje = viaje.id
```

Tabla
```
| origen   |
| -------- |
| Curicó   |
| Curicó   |
| Talca    |
| Talca    |
| Curicó   |
| Curicó   |
| Santiago |
| Santiago |
| Curicó   |
| Curicó   |
| Talca    |
| Talca    |
| Curicó   |
| Curicó   |
| Santiago |
| Santiago |
| Curicó   |
| Curicó   |
| Curicó   |
| Curicó   |  
| Linares  |
| Linares  |
| Linares  |
| Linares  |
| Curicó   |
| Curicó   |
| Curicó   |
| Curicó   |
| Curicó   |
| Curicó   |
```

#### Errores:
-  origen en vez de destino
-  Sin especificar a Juan
### Resultado esperado
```
El modelo fue capaz de identificar todos los errores correctamente
```




# Respuesta con errores de sintaxis

```
SELECT DISTINCT viaje.destino
FROM cliente
JOIN ticket ticket.refcliente == cliente.id
JOIN viaje ticket.refviaje == viaje.id
WHERE cliente.nombre == "Juan";
```

### Errores:
- Comillas dobles
- Doble igual
- Falta ON para JOIN
### Resultado esperado
```
El modelo fue capaz de identificar el error y proporcionar la solucion para ejecutar la consulta
```





# Sugerir respuesta a consulta incorrecta

```
SELECT viaje.origen 
FROM cliente
JOIN ticket ON ticket.refcliente = cliente.id
JOIN viaje ON ticket.refviaje = viaje.id
```
### Respuesta esperada
```
El modelo fue capaz de sugerir consulta que resuelve el ejercicio
```




# Respuesta correcta, pero con elementos Innecesarios

Correcta
```
SELECT DISTINCT viaje.destino
FROM cliente
JOIN ticket ON ticket.refcliente = cliente.id
JOIN viaje ON ticket.refviaje = viaje.id
WHERE cliente.nombre = 'Juan' AND cliente.nombre != 'Pedro'
ORDER BY viaje.destino;
```

Tabla
```
| destino |
| ------- |
| Curicó  |
| Linares |
| Talca   |
```
#### Elementos:
-  Order by inesesario
-  Condiciones adicionales sin sentido
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

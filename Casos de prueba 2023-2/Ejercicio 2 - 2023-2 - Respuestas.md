# Contexto ejercicio 2

### Enunciado
```
Retornar una tabla con los nombres de los académicos que han revisado la mayor cantidad de tesis. No se permite el uso de order-by, offset o limit.
```

### Respuesta correcta
```
select t3.rev_nombre as nombre_academico
from 
( select academico.id as rev_id, academico.nombre as rev_nombre, count(revisor.ref_tesis) as contador
  from academico, revisor
  where revisor.ref_academico = academico.id
  group by academico.id, academico.nombre
) as t3,
( select max(contador) as maximo
  from 
  ( select academico.id as revisor, count(revisor.ref_tesis) as contador
    from academico, revisor
    where revisor.ref_academico = academico.id
    group by academico.id
  ) as t1
) as t2
where t3.contador = t2.maximo
```

### Tabla esperada
```
|nombre_academico |
|-----------------|
|Academico cuatro |
|Academico cinco  |
```






# Respuestas hipotéticas (Casos de prueba)

# Correcta o incorrecta

Correcta
```
SELECT academico.nombre AS nombre_academico
FROM academico
INNER JOIN revisor ON revisor.ref_academico = academico.id
GROUP BY academico.id, academico.nombre
HAVING COUNT(revisor.ref_tesis) = (
    SELECT MAX(contador)
    FROM (
        SELECT COUNT(revisor.ref_tesis) AS contador
        FROM academico
        INNER JOIN revisor ON revisor.ref_academico = academico.id
        GROUP BY academico.id
    ) AS t
);
```

Tabla
```
|nombre_academico |
|-----------------|
|Academico cuatro |
|Academico cinco  |
```


Incorrecta
```
SELECT academico.nombre AS rev_nombre
FROM academico
JOIN revisor ON revisor.ref_academico = academico.id
GROUP BY academico.id, academico.nombre
ORDER BY COUNT(revisor.ref_tesis) DESC
LIMIT 1;
```

Tabla
```
|rev_nombre      |
|----------------|
|Academico cuatro|
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
SELECT academico.nombre AS rev_nombre
FROM academico
JOIN revisor ON revisor.ref_academico = academico.id
GROUP BY academico.id, academico.nombre
ORDER BY COUNT(revisor.ref_tesis) DESC
LIMIT 1;
```

Tabla
```
|nombre_academico|
|----------------|
|Academico cuatro|
```

#### Errores:
-  Usa operadores prohibidos
-  No muestra todos académicos
### Resultado esperado
```
El modelo fue capaz de identificar todos los errores correctamente
```





# Respuesta con errores de sintaxis

```
SELECT academicos.nombre AS nombre_academico
FROM academicos
INNER JOIN revisor ON revisor.ref_academico = academicos.id
GROUP BY academicos.id academicos.nombre
HAVING COUNT(revisor.ref_tesis) = (
    SELECT MAX(contador)
    FROM (
        SELECT COUNT(revisor.ref_tesis) AS contador
        FROM academicos
        INNER JOIN revisor ON revisor.ref_academico == academicos.id
        GROUP BY academicos.id
    ) AS t
);
```

### Errores:
- Tabla from "academicos" en vez de "academico" mal escrita
- Falta coma en linea 4
- doble igual en sub-consulta
### Resultado esperado
```
El modelo fue capaz de identificar el error y proporcionar la solucion para ejecutar la consulta
```






# Sugerir respuesta a consulta incorrecta

```
SELECT academico.nombre AS rev_nombre
FROM academico
JOIN revisor ON revisor.ref_academico = academico.id
GROUP BY academico.id, academico.nombre
ORDER BY COUNT(revisor.ref_tesis) DESC
LIMIT 1;
```
### Respuesta esperada
```
El modelo fue capaz de sugerir consulta que resuelve el ejercicio
```

## Respuesta correcta, pero con elementos Innecesarios

Correcta
```
SELECT academico.nombre AS nombre_academico
FROM (
    SELECT academico.id, academico.nombre
    FROM academico
) AS academico
INNER JOIN (
    SELECT revisor.ref_academico, revisor.ref_tesis
    FROM revisor
) AS revisor ON revisor.ref_academico = academico.id
GROUP BY academico.id, academico.nombre
HAVING COUNT(revisor.ref_tesis) = (
    SELECT MAX(contador)
    FROM (
        SELECT COUNT(revisor.ref_tesis) AS contador
        FROM academico
        INNER JOIN revisor ON revisor.ref_academico = academico.id
        GROUP BY academico.id
    ) AS subquery
);

```

Tabla
```
|nombre_academico|
|----------------|
|Academico cuatro|
|Academico cinco |
```
#### Elementos:
-  2 Subconsultas innecesarias
- Al inicio
- Al contar academicos
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

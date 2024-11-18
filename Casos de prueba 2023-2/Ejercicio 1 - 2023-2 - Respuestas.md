# Contexto ejercicio 2

### Enunciado
```
Retornar una tabla con los atributos "nombre_academico" y "nro_estudiantes", la cual muestra, para cada académico, el número de estudiantes de los cuales ha sido tutor. La consulta debe diferenciar a los académicos con el mismo nombre.
```

### Respuesta correcta
```
select academico.nombre as nombre_academico, count(ref_estudiante) as nro_estudiantes
from academico, tesis
where
tesis.ref_tutor = academico.id
group by academico.id
```

### Tabla esperada
```
|nombre_academico |nro_estudiantes|
|-----------------|---------------|
|Academico cuatro |2              |
|Academico dos    |2              |
|Academico tres   |2              |
|Academico cinco  |1              |
|Academico uno    |2              |
```






# Respuestas hipotéticas (Casos de prueba)

# Correcta o incorrecta

Correcta
```
SELECT academico.nombre AS nombre_academico, COUNT(tesis.ref_estudiante) AS nro_estudiantes
FROM academico
INNER JOIN tesis ON tesis.ref_tutor = academico.id
GROUP BY academico.id;

```

Tabla
```
|nombre_academico |nro_estudiantes|
|-----------------|---------------|
|Academico cuatro |2              |
|Academico dos    |2              |
|Academico tres   |2              |
|Academico cinco  |1              |
|Academico uno    |2              |
```


Incorrecta
```
SELECT academico.nombre, COUNT(*) 
FROM academico
INNER JOIN tesis ON tesis.ref_tutor = academico.id
GROUP BY academico.nombre, tesis.ref_estudiante
```

Tabla
```
|nombre           |estudiantes|
|-----------------|-----------|
|Academico tres   |1          |
|Academico cinco  |1          |
|Academico dos    |1          |
|Academico uno    |1          |
|Academico cuatro |1          |
|Academico cuatro |1          |
|Academico tres   |1          |
|Academico dos    |1          |
|Academico uno    |1          |
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
SELECT academico.nombre, COUNT(*) 
FROM academico
INNER JOIN tesis ON tesis.ref_tutor = academico.id
GROUP BY academico.nombre, tesis.ref_estudiante
```

Tabla
```
|nombre           |count|
|-----------------|-----|
|Academico tres   |1    |
|Academico cinco  |1    |
|Academico dos    |1    |
|Academico uno    |1    |
|Academico cuatro |1    |
|Academico cuatro |1    |
|Academico tres   |1    |
|Academico dos    |1    |
|Academico uno    |1    |
```

#### Errores:
-  Count mal aplicado
-  Tablas no renombradas
- Group By mal aplicado
### Resultado esperado
```
El modelo fue capaz de identificar todos los errores correctamente
```




# Respuesta con errores de sintaxis

```
SELECT academico.nombre AS nombre_academico COUNT(tesis.ref_estudiante) AS nro_estudiantes
FROM academico
INNER JOIN tesis ON tesis.ref_tutor = academico.id
GROUP BY academico.id, academico.nombre;
```

### Errores:
- Falta coma el select
- Doble igual
- Falta ON para JOIN
### Resultado esperado
```
El modelo fue capaz de identificar el error y proporcionar la solucion para ejecutar la consulta
```




## Sugerir respuesta a consulta incorrecta

```
SELECT academico.nombre, COUNT(*) 
FROM academico
INNER JOIN tesis ON tesis.ref_tutor = academico.id
GROUP BY academico.nombre, tesis.ref_estudiante
```
### Respuesta esperada
```
El modelo fue capaz de sugerir consulta que resuelve el ejercicio
```







# Sugerir respuesta

(incorrecta con espesificos reciclada)

# Respuesta correcta, pero con elementos Innecesarios

Correcta
```
SELECT academico.nombre AS nombre_academico, COUNT(tesis.ref_estudiante) AS nro_estudiantes
FROM academico
INNER JOIN tesis ON tesis.ref_tutor = academico.id
WHERE academico.edad > 30  
GROUP BY academico.id, academico.nombre
ORDER BY nro_estudiantes DESC;
```

Tabla
```
|nombre_academico |nro_estudiantes|
|-----------------|---------------|
|Academico cuatro |2              |
|Academico dos    |2              |
|Academico tres   |2              |
|Academico uno    |2              |
|Academico cinco  |1              |
```
#### Elementos:
-  Where sin sentido
-  Order by inesesario
- Grup by id y nombre (solo uno basta)
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


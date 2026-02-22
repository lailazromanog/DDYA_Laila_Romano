# Semana 1
Este repositorio contiene las actividades realizadas en la Semana 1, enfocadas en hacer una prueba para saber nuestro nivel en cuanto a programación, manejo de estructuras, logica de programación y validación.  
## Proyectos realizados  

### 1. Programa 1: Análisis númerico (Fibonacci, Primos y Validar el número)  
Este programa evalúa un número entero n ingresado por el usuario.  
- **Clasificación de signo:** Determina si el número es positivo (n>0), negativo (n<0) o cero.
- **Validación si es primo:** Implementa un bucle while eficiente que busca divisores hasta la raíz cuadrada del número (divisor * divisor <= n).
- **Pertenencia a Fibonacci:** Genera la secuencia partiendo de los casos base [0,1] hasta alcanzar o superar el valor ingresado para verificar su existencia en la serie.

## 2. Programa 2: Gestión de notas académicas  
Un algoritmo diseñado para procesar una cadena de texto con nombres y calificaciones de estudiantes:  
- **Procesamiento del texto:** Utiliza .split para fragmentar los datos de entrada en una lista general de datos.
- **Estructura de datos:** Organiza la información en listas independientes (nombres y notas) mediante saltos de indice de 2 en 2.
- **Filtrado de resultados:** Valida y muestra únicamente a los estudiantes cuya nota es mayor o igual a 3.0.

## Estructura del repositorio Semana 1  
- **"Prueba 1_Semana 1.py":** Código python para el Programa 1.
- **"Prueba 2_Semana 1.py":** Código python para el Programa 2.
- **"Analisis y diagrama prueba 1.pdf":** Documentación del procedimiento y diagrama de flujo del Programa 1.
- **"Analisis y diagrama prueba 2.pdf":** Documentación del procedimiento y diagrama de flujo del Programa 2.
- **"D1-P1.png" y "D2-P2.png":** Diagramas de flujo de cada una de las pruebas.

## Tecnologias y conceptos aplicados  
- **Lenguaje:** Python (Uso de input, int, float, listas, bucles)
- **Lógica:** Implementación de condicionales anidados y estructuras de control.
- **Documentación:** Creación de diagramas de flujo para representar visualmente la solución.

--- 
# Semana 2
Este repositorio contiene las actividades realizadas durante la Semana 2, enfocadas en la profundización de algoritmos de gestión de datos, análisis de requerimientos y la organización estructurada de archivos en Python.  

## Proyectos realizados

### 1. Programa: Gestión Avanzada de Estudiantes (`Estudiantes_sem2.py`)
Un algoritmo desarrollado para automatizar el procesamiento de información académica, mejorando la lógica de captura y filtrado de datos.
- **Entrada dinámica:** Permite la carga y procesamiento de registros de estudiantes.
- **Manejo de colecciones:** Uso de estructuras de datos para organizar nombres y calificaciones.
- **Validación y lógica:** Implementación de filtros para determinar estados académicos basados en las notas obtenidas.

### 2. Documentación y Análisis Técnica
Se realizó un proceso de preventa y diseño lógico antes de la codificación, asegurando que la solución cumpla con los requisitos del taller.
- **Análisis de Diseño:** Documentación detallada sobre la arquitectura del código y la lógica aplicada para resolver los problemas planteados.
- **Taller Práctico:** Resolución de ejercicios de lógica de programación y estructuras de control.

## Estructura del repositorio Semana 2
- **`Semana-2/`**: Carpeta principal que contiene los entregables de este módulo.
- **`Estudiantes_sem2.py`**: Código fuente en Python para la gestión de datos académicos.
- **`Analisis_diseño.docx`**: Documento con el análisis lógico y estructural del proyecto.
- **`Taller_Semana 2.docx`**: Documento con la resolución de los ejercicios teóricos y prácticos propuestos.

## Tecnologías y conceptos aplicados
- **Lenguaje:** Python (Optimización de listas, manejo de cadenas y estructuras de control).
- **Documentación Técnica:** Redacción de análisis de requerimientos en formato profesional.
- **Gestión de Versiones:** Uso avanzado de Git (manejo de ramas o *branches*) para organizar el flujo de trabajo.
--- 
# Semana 3  
Enfocada en el paradigma **Dividir y Conquistar (D&C)** y análisis de complejidad mediante recurrencias.  
## Proyectos realizados  
### 1. Gestión de Estudiantes con D&C (`Estudiantes_D&G_Semana 3.py`)  
Reforma total del sistema de filtrado utilizando recursividad para mejorar la escalabilidad.  
- **Estrategia:** La función `filtrar_estudiantes_DyC` descompone la lista hasta el caso base (un estudiante).
- **Lógica:** Divide el rango mediante un punto medio (`mid`), resuelve las mitades y combina los resultados.
- **Análisis:** Aunque se mantiene una complejidad de $\Theta(n)$, la estructura prepara el código para procesamiento en paralelo.

### 2. Ejercicios de Aplicación (`Ejercicios- Semana 3.pdf`)
Resolución de problemas clásicos aplicando optimización:
- **Búsqueda Binaria:** Localización del menor número en arreglos con comportamiento unimodal (decremento/incremento).
- **Exponenciación Rápida:** Algoritmo recursivo para calcular $a^n$ en tiempo logarítmico $O(\log n)$.
- **Ordenamiento Mergesort:** Seguimiento paso a paso para ordenar alfabéticamente la cadena "ALGORITMO".
- **Conteo de Bits:** Uso de búsqueda binaria para identificar números faltantes basados en sumas de bits.

## Estructura del Repositorio - Semana 3
- **`Estudiantes_D&G_Semana 3.py`**: Código fuente con la implementación de la herramienta D&C.
- **`Diseño del problema de los estudiantes con D&C.pdf`**: Documentación técnica (Historias de usuario, diagramas de flujo recursivo, secuencia y casos de uso).
- **`Ejercicios- Semana 3.pdf`**: Análisis detallado y pseudocódigos de los problemas resueltos en clase.

## Tecnologías y Conceptos Aplicados
- **Paradigma de Diseño:** Dividir, Conquistar y Combinar.
- **Análisis Matemático:** Notación Big O, Teorema Maestro y Ecuaciones de Recurrencia $T(n) = 2T(n/2) + c$.
- **Modelado UML:** Diagramas de secuencia para representar la auto-llamada (recursión) y flujo de mensajes.
---
# Semana 4: Programación Dinámica y Optimización de Algoritmos

En esta semana, el enfoque principal fue la implementación de la Programación Dinámica (Memoización) para optimizar problemas que presentan subproblemas superpuestos, además de fortalecer la robustez de las aplicaciones mediante pruebas de errores.

## Proyectos realizados

### 1. Optimización del Problema de los Amigos
Se desarrolló una solución para calcular las formas posibles en que *n* amigos pueden quedar solos o emparejados.
- **Paradigma:** Programación Dinámica (Memoización).
- **Optimización:** Uso de un diccionario (`memo`) para almacenar resultados de subproblemas ya calculados, evitando la redundancia de la recursividad simple y mejorando drásticamente el tiempo de ejecución para valores grandes de *n*.

### 2. Gestión de Estudiantes V2: Rangos Dinámicos y Robustez
Actualización del sistema de gestión académica integrando mayor dificultad técnica y control de excepciones.
- **Análisis por Rangos:** El usuario ahora define un rango específico (índice inicial y final) para calcular el promedio de referencia.
- **Memoización de Promedios:** El sistema "recuerda" promedios de rangos consultados previamente para optimizar la velocidad de respuesta.
- **Pruebas de Robustez (Tests):** Implementación de validaciones para entradas no ideales (caracteres inválidos, notas fuera de rango 0-5, índices fuera de límites o rangos invertidos).
- **Algoritmo de Filtrado:** Uso continuo de **Dividir y Conquistar** para el retorno de la lista de aprobados.

## Demostración de Pruebas (Tests)
Como parte del control de calidad del software, se realizó una explicación detallada de cómo el sistema maneja los errores de interacción del usuario.

> [!VIDEO]
> **Video explicativo de los Tests realizados:**
> [https://youtu.be/HXFeXZ_FI10]

## Estructura del Repositorio - Semana 4
- **`Semana_4_Amigos_PDinamica.py`**: Implementación del problema de emparejamiento con memoización.
- **`Semana 4_Estudiantes_PDinamica.py`**: Código optimizado con rangos dinámicos y DP.
- **`Semana 4_Estudiantes_PDinamica_Tests.py`**: Versión del código con lógica avanzada de validación y manejo de errores.
- **`Semana 4_Analisis_Taller en clase.pdf`**: Documentación técnica y análisis de complejidad del problema de los amigos.

## Tecnologías y Conceptos Aplicados
- **Memoización:** Almacenamiento de estados para optimización temporal.
- **Manejo de Excepciones:** Uso de bloques `try-except` y validaciones lógicas para prevenir cierres inesperados.
- **Complejidad:** Análisis de cómo la memoria (espacio) puede reducir el tiempo de ejecución (tiempo).



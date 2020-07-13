# MeLi-solar
Desafio MeLi

La API se puede acceder desde https://meli-solar.rj.r.appspot.com/clima?dia=567

## Como correr

Requisitos:
 * python3
 * make

`make stats` retorna las estadisticas para los proximos 10 años
`make tests` ejectura los unit tests

## Como hacer el deploy local

 * `pip3 install -r requirements.txt`
 * `make local`

## Cosas que asumo

 * Cada dia dura lo mismo en cada planeta, ya que lo medimos desde la tierra.
 * No hay años bisiestos, cada año tiene 365 dias, ya que nos importa las mediciones desde la tierra
 * Si los planetas forman un triangulo y el sol se encuentra en una arista, considero que el sol se encuentra adentro
 * Los planetas avanzan una cantidad enteras de grados por dia
 * Los planetas no tienen distancia 0 al sol, ya que este los consumiría
 * Hay otro tipo de clima, "desconocido", que se da cuando los planetas forman un triangulo que no incluye al sol adentro
 * Solo me interesa saber la predicción del clima cuando comienza un nuevo dia, es decir, no me interesa saber la posición de los planetas al mediodia.


## Primera Parte

El objetivo es poder calcular, para los proximos 10 años el comportamiento del clima en los planetas.

Los planetas se caracterizan por:
 * su distancia al sol,
 * su velocidad de movimiento, y
 * su capacidad de moversa cada dia.

Luego, caracterizamos al sistema solar como un conjunto de 3 planetas (Vulcanos, Ferengis y Betasoides) con un par de operaciones interesantes:
 * avanzar un dia, y
 * calcular el clima actual.

Además, se les agrega a los planetas la posibilidad de hacer calculos entre ellos:
 * `collinear()` permite calcular si tres planetas son colineales, se fija si forman un triangulo degenerado.

Por otro lado, el sistema solar tiene métodos para observar como interactúan los planetas con el sol:
 * `collinearWithSun()` verifica si tres planetas son colineales con el sol. Notar que se podría lograr algo parecido usando `Planet.collinear()`, pero esta operación es más segura, ya que no precisa hacer comparaciones entre floats, y más rápida, ya que utiliza menos operaciones menos costosas.
 * `includeSun()` chequea si el triangulo formado por los planetas incluye al sol. Esto se podria chequear usando trigonometria, pero utilizamos la información extra de que son planetas orbitando cirularmente alrededor de un sol para no precisar operaciones entre flotantes.

Para calcular el clima en un dia dado hace falta poder saber si los planetas están alineado y, si no lo estan, calcular el perimetro del triangulo formado y si el sol se encuentra contenido. Notar que los planetas nos ofrecen todas estas operaciones.

## REST API

El resultado esta hosteado en APPEngine. No se hizo un modelo de datos por falta de tiempo, pero si un servicio que calcula el resultado cada vez que se le pide.

Se utilizo Flask como framework para el backend por ser simple de usar, y suficiente para este ejercicio.

La API solo responde al request `clima` con un argumento `dia` que debe ser entero y cumplir 0 <= `dia` <= 3650.

## Explicación (corta) de las operaciones geométricas

### `collinear()`

Es sabido que una forma de chequear si 3 puntos en el plano son colineales viendo si forman un triangulo degenerado.

Podemos fijarnos si un triangulo es degenerado si cumple alguna de estas dos propiedades:
 * tiene área 0, o
 * la suma de las longitudes de las dos aristas más cortas es igual a la longitud de la más larga.

El método `Planet.collinear()` implementa la segunda, ya que considero que el cálculo es mucho más sencillo.

### `collinearWithSun()`

Cómo sabemos que estos son planetas con una órbita alrededor del sol, que en mi módelo es el órigen del plano, chequear que una cantidad n de planetas son colineales con el sol tienen una solución mejor que utilizar `collinear()`. Simplemente tomamos uno de los planetas, y nos fijamos la recta que forma con el sol, su ángulo va a ser un entero. Entonces, es trivial que el resto de los planetas tiene que tener el mismo ángulo, o el de dirección contraria (ie, el mismo ángulo en áritmetica modular de 180).

Considero que esta solución es mejor que usar `collinear()` ya que:
 * Las operaciones con enteros suelen ser más seguras y confiables que con punto flotante (puedo usar igualdad, y no aproximarla)
 * Por el tipo de operaciones que usa (módulo) es más rápido que `collinear()` (multiplicación y `sqrt`)

### `includeSun()`

Similarmente que en `collinearWithSun()` vamos a tomar la especificidad del módelo para mejorar la solución. Para eso, vamos ordenar nuestros planetas por ángulo, y vamos a comenzar desde el primero (el más cercano al 0° en sentido horario), si el segundo se encuentra a más de 180°, entonces el tercero también y no encierran al sol. Si el segundo se encuentra a menos o igual que 180°, entonces el tercero tiene que ubicarse a más de 180° del primero, pero a menos de 180° del segundo (hacer dibujitos para convencerse).
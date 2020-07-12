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
 * `collinear()` permite calcular si tres planetas son colineares, se fija si forman un triangulo degenerado
 * `collinearWithOrigin()` verifica si tres planetas son colineares con el origen. Notar que se podría lograr algo parecido usando `collinear()`, pero esta operación es más segura, ya que no precisa hacer comparaciones entre floats
 * `includeOrigin()` chequea si el triangulo formado por los planetas incluye al origen. Esto se podria chequear usando trigonometria, pero utilizamos la información extra de que son planetas orbitando alrededor de un sol para no precisar operaciones entre flotantes.

Para calcular el clima en un dia dado hace falta poder saber si los planetas están alineado y, si no lo estan, calcular el perimetro del triangulo formado y si el sol se encuentra contenido. Notar que los planetas nos ofrecen todas estas operaciones.

## REST API

El resultado esta hosteado en APPEngine. No se hizo un modelo de datos por falta de tiempo, pero si un servicio que calcula el resultado cada vez que se le pide.
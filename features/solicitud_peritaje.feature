#language: es
Característica: Solicitud de peritaje

Esquema del escenario: Solicitud de peritaje
Dado que el analista está en nuevo pedido
Cuando busca una <patente>
Entonces visualiza el resultado de la busqueda de patente <resultado>

Ejemplos:
|patente          |resultado                |
|patente valida   |encuentra siniestro      |
|patente invalida |no encuentra siniestro   |
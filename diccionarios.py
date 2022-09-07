##los diccionarios son variables especiales que me permiten almacenar multiples datos de diferente tipo en una sola variable##

from pickle import FALSE


empleado={
    'nombre':"Juan",
    'cedula':1036631918,
    'cargo':"Analista de datos",
    'salario':8000000,
    'harastranajadas':40,
    'aplicasubsidoptransporte':False,
    'deudas':[1500000,800000]





}
print(empleado)
print(empleado['deudas'][1])

##recorriendo un diccionario 

for observadorAtributo,observadorValor in empleado.items():

    print(observadorAtributo)
    print(observadorValor)
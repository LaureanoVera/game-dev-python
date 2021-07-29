extends Node

func _ready():
  arrays_diccionarios()

# COMENTARIO

var myName:String = "Laureano"
var myAge: int = 18
var myFloat: float = 2002.12
var myBool: bool = true

const NOMBRE = "Laureano Vera"

func arrays_diccionarios():
  var names = ['laureano', 'ivan', 'vera']
  var apellidos = {
    'uno':'vera'
  }

  print(names[0])
  print(apellidos.uno)

func operadores_matematicos():
  var numeroUno: float = 1
  var numeroDos: float = 2
  var resultado: float = numeroDos - numeroUno

  print(resultado)

func calculadora_simple(uno:float, dos:float):
  print('Resultado' + str(uno+dos))


if myName == "Laureano":
  pass
elif condition:
  pass
else:
  pass
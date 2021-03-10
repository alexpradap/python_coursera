first = {
  "name": "Uno",
  "number": 1,
  "letter": "a"
}

second = {
  "name": "Dos",
  "number": 2,
  "letter": "b"
}

third = {
  "name": "Dos",
  "number": 2,
  "letter": "c"
}

lista = [second, third, first]

def getter(element):
	return (element.get("number"), element.get("letter"))
	

lista.sort(key=getter)

print(lista)
print(lista[0].get("name"))
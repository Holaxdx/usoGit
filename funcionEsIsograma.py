
# Un isograma (también conocido como "palabra sin patrón") es una palabra
# o frase sin una letra repetida; sin embargo, se permiten espacios y guiones varias veces

def esIsograma(palabra=str):
  loEs = True
  contadorDeLetra = []
  for letra in palabra:
    if contadorDeLetra.__contains__(letra):
      loEs = False
      break
    else:
      contadorDeLetra.append(letra)
  return loEs  
  
  
print(esIsograma("gato"))

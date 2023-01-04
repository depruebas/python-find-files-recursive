# Segundo ejemplo del artículo
# con los filtros por extensiones

# Importamos el modulo de sistema
import os

# Creamos una función recursiva para buscar los ficheros
# a partir de una ruta que le pasamos en "directory"
def search_files(directory, extensiones):
  
  # Recorremos todos los ficheros del directorio
  for file in os.listdir(directory):
    
    # En directory tenemos el path y en file el nombre del fichero
    full_path = os.path.join(directory, file)
    
    # Si es un directorio lo que encontramos volvemos hacer la llamada
    # a la funcion para recorrer el nuevo directorio
    if os.path.isdir(full_path):
      search_files(full_path, extensiones)
    else:
      # So no escribimos por pantalla la ruta/fichero.
      for extension in extensiones:
        if full_path.endswith(extension):
          print(full_path)
          break

# Llamamos a la funcion con la ruta a partir de la que recorrer un directorio
# y sus subdirectorios
search_files('/home/depruebas/Imágenes', ['.jpg', '.png'])
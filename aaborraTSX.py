import os
import glob

def delete_tsx_files(directory):
    # Recorrer de forma recursiva todos los archivos .tsx en el directorio y subdirectorios
    for tsx_file in glob.glob(os.path.join(directory, '**/*.tsx'), recursive=True):
        try:
            os.remove(tsx_file)
            print(f"Archivo borrado: {tsx_file}")
        except Exception as e:
            print(f"No se pudo borrar el archivo {tsx_file}: {e}")

# Especificar el directorio desde donde empezar a borrar
directory = '.'
delete_tsx_files(directory)
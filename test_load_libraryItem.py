import unittest  # Importo unittest para definir pruebas unitarias
import csv       # Para generar y escribir el archivo CSV temporal
import os        # Para eliminar el archivo temporal después de las pruebas
from library_system import load_library_items, Book, Magazine  # Importo funciones y clases a testear

class TestLoadLibraryItemsFromCSVNoHeader(unittest.TestCase):
    # Defino una clase de prueba heredando de TestCase

    def test_load_library_items_from_csv(self):
        # Creo un CSV temporal sin encabezado
        fname = 'temp_items.csv'  # Nombre del fichero temporal
        lines = [  # Contenido: filas válidas e inválidas y línea vacía
            ['book', '1984', '1', 'George Orwell', '328', ''],            # Libro válido
            ['magazine', 'Time', '2', '', '', '42'],                      # Revista válida
            ['book', '', '-3', 'Someone', '100', ''],                     # Inválido: título vacío, id negativo
            ['magazine', 'Forbes', '4', '', '', 'notanumber'],            # Inválido: issue_number no entero
            ['unknown', 'Mystery', '5', '', '', ''],                      # Inválido: tipo desconocido
            [],                                                           # Línea vacía
            ['book', 'Brave New World', '6', 'Aldous Huxley', '311', '']  # Libro válido
        ]

        # Escribo las filas en el CSV temporal
        with open(fname, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)    # Creo el escritor CSV
            writer.writerows(lines)   # Escribo todas las filas

        # Llamo a la función que carga ítems desde el CSV
        items = load_library_items(fname)

        # 1) Compruebo que sólo se hayan cargado los 3 ítems válidos
        self.assertEqual(len(items), 3)

        # 2) Separo por tipo: libros y revistas
        books     = [i for i in items if isinstance(i, Book)]       # Filtrar instancias de Book
        magazines = [i for i in items if isinstance(i, Magazine)]   # Filtrar instancias de Magazine

        # A) Libros: deben ser "1984" y "Brave New World" (sin importar orden)
        self.assertEqual(len(books), 2)  # Dos libros
        titles = [b.title for b in books]  # Extraigo títulos
        self.assertCountEqual(titles, ["1984", "Brave New World"])  # Compruebo contenidos

        # B) Revistas: solo debe existir "Time" con issue_number=42
        self.assertEqual(len(magazines), 1)  # Una revista
        mag = magazines[0]  # Extraigo la revista
        self.assertEqual(mag.title, "Time")           # Compruebo título
        self.assertEqual(mag.issue_number, 42)         # Compruebo número de edición

        # Elimino el archivo temporal para no dejar residuos
        os.remove(fname)

# Hace que se ejecuten estas pruebas si corro este archivo directamente
if __name__ == '__main__':
    unittest.main()

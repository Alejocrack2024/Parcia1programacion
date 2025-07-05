import unittest  # Framework de testing
import csv       # Para manejar archivos CSV si fuese necesario
import os        # Módulo del sistema de archivos
from library_system import Book, Magazine, checkout_items, count_items, find_by_title

class TestLibraryItem(unittest.TestCase):
    #Clase de pruebas unitarias para la funcionalidad de LibraryItem.Se cubren Book, Magazine y funciones utilitarias.
    

    def setUp(self):
        """
        Se ejecuta antes de cada test.
        Aquí creamos una lista de ítems para reutilizar en varios tests.
        """
        self.items = [
            Book("Jurassic Park", 1, "Michael Crichton", 12),
            Magazine("Taza", 6, 12),
            Book("The Lord of the Rings", 3, "J.R.R. Tolkien", 15),
            Magazine("National Geographic", 2, 5),
            Book("The Catcher in the Rye", 4, "J.D. Salinger", 10),
            Magazine("Time", 3, 6),
            Book("1984", 5, "George Orwell", 14),
            Magazine("Forbes", 4, 9),
        ]

    def test_book_initialization(self):
        #Verifica que un Book se inicialice con los atributos correctos.
        book = Book("1984", 5, "George Orwell", 14)
        self.assertEqual(book.title, "1984")
        self.assertEqual(book.item_id, 5)

    def test_book_invalid_id(self):
        #Intenta crear un Book con ID negativo y espera un ValueError.

        with self.assertRaises(ValueError):
            Book("Invalid Book", -1, "Author", 100)

    def test_magazine_initialization(self):
        """
        Verifica que una Magazine se inicialice correctamente.
        """
        magazine = Magazine("Time", 3, 6)
        self.assertEqual(magazine.title, "Time")
        self.assertEqual(magazine.item_id, 3)

    def test_magazine_invalid_id(self):
        """
        Intenta crear una Magazine con ID negativo y espera un ValueError.
        """
        with self.assertRaises(ValueError):
            Magazine("Invalid Magazine", -1, 10)

    def test_book_checkout(self):
        """
        Comprueba el método checkout y __str__ de Book.
        """
        book = Book("Jurassic Park", 1, "Michael Crichton", 12)
        # Verifica mensaje de checkout
        self.assertEqual(book.checkout("Alice"),
                         "Book 'Jurassic Park' checked out by Alice.")
        # Verifica cadena de representación
        self.assertEqual(str(book),
                         "Book(title=Jurassic Park, item_id=1, author=Michael Crichton, pages=12)")

    def test_magazine_checkout(self):
        #Comprueba el método checkout y __str__ de Magazine.
        
        magazine = Magazine("National Geographic", 2, 5)
        # Mensaje de checkout
        self.assertEqual(magazine.checkout("Bob"),
                         "Magazine 'National Geographic' issue 5 checked out by Bob.")
        # Representación en texto
        self.assertEqual(str(magazine),
                         "Magazine(title=National Geographic, item_id=2, issue_number=5)")

    def test_checkout_items(self):
      #Ejecuta checkout_items con lista no vacía.Debe devolver 8 mensajes.
        results = checkout_items(self.items, "Charlie")
        self.assertEqual(len(results), 8)

    def test_checkout_items_empty(self):
      #Ejecuta checkout_items con lista vacía y espera ValueError.
        with self.assertRaises(ValueError):
            checkout_items([], "Charlie")

    def test_count_items(self):
      #Cuenta cuántos libros y revistas hay en self.items.
        count_result = count_items(self.items)
        expected = {"books": 4, "magazines": 4}
        self.assertEqual(count_result, expected)

    def test_count_items_empty(self):
        #count_items con lista vacía a ValueError.
        with self.assertRaises(ValueError):
            count_items([])

    def test_find_by_title(self):
       #Busca por palabra clave existente y no existente.
        found = find_by_title(self.items, "Jurassic")
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0].title, "Jurassic Park")

    def test_find_by_title_not_found(self):
       #Búsqueda sin coincidencias a lista vacía.
        found = find_by_title(self.items, "Nonexistent")
        self.assertEqual(len(found), 0)

    def test_find_by_title_empty(self):
        #find_by_title con lista vacía a ValueError.
        
        with self.assertRaises(ValueError):
            find_by_title([], "Principito")

# Si ejecutas este archivo directamente, corre todos los tests
if __name__ == '__main__':
    unittest.main()
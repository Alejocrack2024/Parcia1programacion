# library_system.py
# Importo las clases base necesarias para crear clases abstractas y definir métodos obligatorios
from abc import ABC, abstractmethod
# Importo tipos para anotaciones de tipo: List y Dict
from typing import List, Dict

# Defino la clase base abstracta para todos los ítems de la biblioteca
class LibraryItem(ABC):
    # Inicializador que recibe título e identificador único
    def __init__(self, title: str, item_id: int):
        # Valido que el título sea una cadena no vacía
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Title must be a non-empty string")
        # Valido que el ID sea un entero no negativo
        if not isinstance(item_id, int) or item_id < 0:
            raise ValueError("item_id must be a non-negative integer")
        # Asigno atributos al objeto
        self.title = title
        self.item_id = item_id

    # Defino un método abstracto que obliga a las subclases a implementarlo
    @abstractmethod
    def checkout(self, user: str) -> str:
        pass  # La implementación se deja a las clases hijas

# Subclase concreta para libros
class Book(LibraryItem):
    def __init__(self, title: str, item_id: int, author: str, pages: int):
        # Llamo al inicializador de la clase padre para title e item_id
        super().__init__(title, item_id)
        # Valido que el autor sea una cadena no vacía
        if not isinstance(author, str) or not author.strip():
            raise ValueError("Author must be a non-empty string")
        # Valido que las páginas sean un entero positivo
        if not isinstance(pages, int) or pages < 1:
            raise ValueError("pages must be a positive integer")
        # Asigno atributos específicos de Book
        self.author = author
        self.pages = pages

    # Implemento el método de checkout para libros
    def checkout(self, user: str) -> str:
        return f"Book '{self.title}' checked out by {user}."

    # String representation para debugging y logging
    def __str__(self) -> str:
        return f"Book(title={self.title}, item_id={self.item_id}, author={self.author}, pages={self.pages})"

# Subclase concreta para revistas
class Magazine(LibraryItem):
    def __init__(self, title: str, item_id: int, issue_number: int):
        # Llamo al inicializador de la clase padre
        super().__init__(title, item_id)
        # Valido que el número de edición sea entero positivo
        if not isinstance(issue_number, int) or issue_number < 1:
            raise ValueError("issue_number must be a positive integer")
        # Asigno atributo específico de Magazine
        self.issue_number = issue_number

    # Implemento el método de checkout para revistas
    def checkout(self, user: str) -> str:
        return f"Magazine '{self.title}' issue {self.issue_number} checked out by {user}."

    # String representation para debugging
    def __str__(self) -> str:
        return f"Magazine(title={self.title}, item_id={self.item_id}, issue_number={self.issue_number})"

# Función que simula el préstamo de varios ítems a un usuario
def checkout_items(items: List[LibraryItem], user: str) -> List[str]:
    # Verifico que la lista no esté vacía
    if not items:
        raise ValueError("Item list is empty")
    # Devuelvo una lista con los resultados de cada checkout
    return [item.checkout(user) for item in items]

# Cuenta cuántos libros y revistas hay en la lista
def count_items(items: List[LibraryItem]) -> Dict[str, int]:
    # Verifico lista no vacía
    if not items:
        raise ValueError("Item list is empty")
    # Inicializo el contador
    counts = {"books": 0, "magazines": 0}
    # Recorro cada ítem y actualizo el contador según su tipo
    for item in items:
        if isinstance(item, Book):
            counts["books"] += 1
        elif isinstance(item, Magazine):
            counts["magazines"] += 1
    return counts

# Busca ítems cuyo título contenga una palabra clave
def find_by_title(items: List[LibraryItem], keyword: str) -> List[LibraryItem]:
    # Verifico lista no vacía
    if not items:
        raise ValueError("Item list is empty")
    # Filtro e devuelvo los ítems que coincidan en el título
    return [item for item in items if keyword.lower() in item.title.lower()]

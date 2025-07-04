 from abc import ABC, abstractmethod
class LibraryItem(ABC):
    def __init__(self, title: str, item_id: int):
        self.title = title
        self.item_id = item_id
    if not isinstance(title,str) or not title:
        raise ValueError("Title debe ser una cadena no vacia")
    if not isinstance(item_id,int) or item_id < 0:
        raise ValueError("item_id debe ser un entero positivo")

    @abstractmethod
    def checkout(self, user: str) -> str:
        pass

class Book(LibraryItem):
    def __init__(self,title: str, item_id: int, author: str,pages: int):
        super().__init__(title,item_id)
        self.author=author
        self.pages=pages

    def chetkout(self, user: str) -> str:
        return f"Book '{self.title}' checked out by {user}."
    
    def __str__(self):
        return f"Book(title={self.title}, item_id={self.item_id}, author={self.author}, pages={self.pages})"
class Magazine(LibraryItem):
    def __init__(self,title: str, item_id: int, issue_number: int):
        super().__init__(title,item_id)
        self.issue_number=issue_number

    def checkout(self, user: str) -> str:
        return f"Magazine '{self.title}' issue {self.issue_number} checked out by {user}."

    def checkout_items(items: list[LibraryItem], user: str) -> list[str]:
        lista = []
        for i in items:
            if isinstance(i, LibraryItem):
                lista.append(i.checkout(user))
        return f"Checkout results: {lista}"

    def count_items(items: list[LibraryItem]) -> dict:
        count = {"books": 0, "magazines": 0}
        for item in items:
            if isinstance(item, Book):
                count["books"] += 1
            elif isinstance(item, Magazine):
                count["magazines"] += 1
        return count

    def find_by_title(items: list[LibraryItem], keyword: str) -> list[LibraryItem]:
        lista = []
        for item in items:
            if keyword.lower() in item.title.lower():
                lista.append(item)
        return lista
    
    def __str__(self):
        return f"Magazine(title={self.title}, item_id={self.item_id}, issue_number={self.issue_number})"
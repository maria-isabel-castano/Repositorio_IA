class RecursoBiblioteca:
    def __init__(self, titulo, autor):
      self.titulo = titulo
      self.autor = autor

    def mostrar_info(self):
      return f"Título: {self.titulo}, Autor: {self.autor}"


class Libro(RecursoBiblioteca):
    def __init__(self, titulo, autor, isbn):
      super().__init__(titulo, autor)
      self.isbn = isbn

    def mostrar_info(self):
      return f'El libro: {self.titulo},  tiene el número ISBN: {self.isbn}'

class Revista(RecursoBiblioteca):
    def __init__(self, titulo, autor, numero):
      super().__init__(titulo, autor)
      self.numero = numero

    def mostrar_info(self):
      return f'La revista : {self.titulo}, tiene el número: {self.numero}'

libro = Libro('El Código Da Vinci', 'Dan Brown', '978-0307474278')
revista = Revista('National Geographic', 'Various', '123')

lista = [libro, revista]

for doc in lista:
  print(doc.mostrar_info())

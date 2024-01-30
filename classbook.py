class Publisher:
    def __init__(self, name='nil'):
        self.name = name

    def display(self):
        print('Name:', self.name)


class Book(Publisher):
    def __init__(self, name='nil', title='nil', author='nil'):
        super().__init__(name)
        self.title = title
        self.author = author

    def display(self):
        super().display()
        print('title: ', self.title)
        print('Author: ', self.author)


class Python(Book):
    def __init__(self, name='nil', title='nil', author='nil', price=0, nop=0):
        super().__init__(name, title, author)
        self.price = price
        self.nop = nop

    def display(self):
        super().display()
        print('Price:', self.price)
        print('No. of Pages:', self.nop)


p1 = Python('Wings of fire', 'Wings', 'APJ', 120, 450)
p2 = Python('Harry Potter', 'Harry', 'JK', 800, 1400)
print("Book 1")
p1.display()
print("Book 2")
p2.display()

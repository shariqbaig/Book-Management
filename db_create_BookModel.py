from BookModel import bookDb, Book

bookDb.create_all()

Book.add_book('Do Androids Dream of Electric Sheep?', 7.99, 101)
Book.add_book('Something Wicked This Way Comes', 10.99, 102)
Book.add_book('The Unbearable Lightness of Being', 6.99, 103)

bookDb.session.commit()

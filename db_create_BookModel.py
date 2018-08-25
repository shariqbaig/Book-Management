from BookModel import db, Book

db.create_all()

Book.add_book('Do Androids Dream of Electric Sheep?', 7.99, 64543546435)
Book.add_book('Something Wicked This Way Comes', 10.99, 6451687464)
Book.add_book('The Unbearable Lightness of Being', 6.99, 6435121545)

db.session.commit()

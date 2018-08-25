from BookModel import db, Book

db.drop_all()
db.create_all()

Book.add_book('Do Androids Dream of Electric Sheep', 7.99, 101)
Book.add_book('Something Wicked This Way Comes', 10.99, 102)
Book.add_book('The Unbearable Lightness of Being', 6.99, 103)

db.session.commit()

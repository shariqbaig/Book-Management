from UserModel import db, User

db.drop_all()
db.create_all()

User.createUser('test', 'pass')
User.createUser('abc', '123')

db.session.commit()

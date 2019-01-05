from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Category, Item

engine = create_engine('sqlite:///categoryitmes.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

User1 = User(name="Shatha Khalid", email="shatha.9393@hotmail.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/' /
                     '18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()


category1 = Category(title="cat1", User_id=1)
session.add(category1)
session.commit()

item1 = Item(title="it1 1", User_id=1, Category_id=1)
session.add(item1)
session.commit()

item2 = Item(title="it2 1", User_id=1, Category_id=1)
session.add(item2)
session.commit()

item3 = Item(title="it3 1", User_id=1, Category_id=1)
session.add(item3)
session.commit()

category2 = Category(title="cat2", User_id=1)
session.add(category2)
session.commit()

item1 = Item(title="it1 2", User_id=1, Category_id=2)
session.add(item1)
session.commit()

item2 = Item(title="it2 2", User_id=1, Category_id=2)
session.add(item2)
session.commit()

item3 = Item(title="it3 2", User_id=1, Category_i=2)
session.add(item3)
session.commit()


category3 = Category(title="cat3", User_id=1)
session.add(category3)
session.commit()

item1 = Item(title="it1 3", User_id=1, Category_id=3)
session.add(item1)
session.commit()

item2 = Item(title="it2 3", User_id=1, Category_id=3)
session.add(item2)
session.commit()

item3 = Item(title="it3 3", User_id=1, Category_id=3)
session.add(item3)
session.commit()

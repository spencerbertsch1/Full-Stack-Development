# CRUD Cheat Sheet
"""
CONFIGS WITH SQL ALCHEMY

import the necessary libraries
connect to our restaurantMenu.db
and create a session to interface with the database
"""
from sqlalchemy import create_engine #<-- dependency from SQLAlchemy
from sqlalchemy.orm import sessionmaker #<-- dependency from SQLAlchemy
# We now need to import our base, and any tables which we created in our currently empty database
from database_setup import Base, Restaurant, MenuItem #<-- Import tables we already made in the database

# We now want to tell the program which database engine we want to communicate with.
# We want to interact with restaurantMenu.db, so we use the command
#     create_engine('sqlite:///restaurantMenu.db')
engine = create_engine('sqlite:///restaurantMenu.db')

# We can now bind the engine called 'engine' to the base class.
# This command simply forges a connection between our class definitions, and
# their corresponding tables within our restaruantmenu database
Base.metadata.bind=engine

# We are now ready to create a sessionmaker object.
# This object establishes a link between our code executions
# and the engine we created called 'engine'
DBSession = sessionmaker(bind = engine)

# Create instance of a DBSession - let's call it 'session'
# Whenever we want to make a change to something within our database, (CRUD),
# we simply need to call a method within the instantiated session object called 'session'!
# The DBSession object provides us with a staging zone (Similar to git!) for all of the
# object loaded into the DBSession object. Any changed in the objects which are stored in the
# DBSession object will not be persisted until we make a commit using 'session.commit()'
session = DBSession()


"""
CREATE

We created a new Restaurant and called it Pizza Palace

newEntry = ClassName(property = "value") #1. PART ONE: Create new restaurant object
session.add(newEntry)                    #2. PART TWO: Add that new object to the staging area
session.commit()                         #3. PART THREE: Commit the changes to the database
"""
myFirstRestaurant = Restaurant(name = "Pizza Palace")
session.add(myFirstRestaurant)
session.commit()
"""
We created a cheese pizza menu item and added it to the Pizza Palace Menu:
"""
cheesepizza = MenuItem(name="Cheese Pizza", description = "Made with all natural ingredients and fresh mozzarella", course="Entree", price="$8.99", restaurant=myFirstRestaurant)
session.add(cheesepizza)
session.commit()


"""
READ

We read out information in our database using the query method in SQLAlchemy:
"""
firstResult = session.query(Restaurant).first() #<-- we add the '.first()' to retuirn a single row in the database
# We can use this to extract column entries as method names!
firstResult.name #<-- we can now see the name of the restaurant object as it exists in the database!

items = session.query(MenuItem).all() #<-- returns a list of all items stored in MenuItem
for item in items:
    print item.name #<-- this for loop simply loops through the list and prints the names of all items in the list
    # This acts as a way to view all the items stored in a column.


"""
UPDATE

In order to update and existing entry in our database, we must execute the following commands

1. Find Entry
2. Reset value(s)
3. Add to session
4. Execute session.commit()

We found the veggie burger that belonged to the Urban Burger restaurant by executing the following query
"""
# we can use the 'filter_by' tag to only select the "Veggie Burger" menu items
veggieBurgers = session.query(MenuItem).filter_by(name= 'Veggie Burger')
# And similarly to the READ section, we can use a for loop to show all the information for each
# vegieburger in the menu!
for veggieBurger in veggieBurgers:
    print veggieBurger.id
    print veggieBurger.price
    print veggieBurger.restaurant.name
    print "\n"
"""
Then we updated the price of the veggie burger to $2.99:
"""
UrbanVeggieBurger = session.query(MenuItem).filter_by(id=9).one() #<-- Use 'id=8' to select the correct veggieburger
UrbanVeggieBurger.price = '$2.99' #<-- Create a new price for this burger
session.add(UrbanVeggieBurger) #<-- Stage the new object with the updated price
session.commit() #<-- commit the change

for veggieBurger in veggieBurgers:
    print veggieBurger.price

"""
DELETE

To delete an item from our database we must follow the following steps:

1. Find the entry
2. Session.delete(Entry)
3. Session.commit()

We deleted spinach Ice Cream from our Menu Items database with the following operations:
"""
# Find the item called "Spinach Ice Cream and give it a name: spinach"
spinach = session.query(MenuItem).filter_by(name = 'Spinach Ice Cream').one()
# Call the method session.delete() on the spinach object
session.delete(spinach)
# Commit the changes, and that entry is deleted!
session.commit()


#end

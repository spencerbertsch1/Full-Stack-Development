from flask import Flask
app = Flask(__name__)

# Web Page #1 - simply shows all restaurants
@app.route('/')
@app.route('/restaurants')
def showRestaurants(): #<-- method name: showRestaurants()
    return('This page will show the restaurants homepage - it will display names of all restaurants.')

# Web Page #2 - making a new restaurant
@app.route('/restaurants/new')
def newRestaurant():
    return('Users will use this page to make a new restaurant.')

# Web Page #3 - edit the name of a restaurant
@app.route('/restaurants/<int:restaurant_id>/edit')
def editRestaurant(restaurant_id): #<-- remember to pass in the correct arguments gathered from the web page URL!
    return('Users will use this page to edit the name of restaurant %s' % restaurant_id)

# Web Page #4 - delete a restaurant in the database
@app.route('/restaurants/<int:restaurant_id>/delete')
def deleteRestaurant(restaurant_id):
    return('Users will use this page to delete restaurant %s' % restaurant_id)

# Web Page #5 - show the menu for a restaurant
@app.route('/restaurants/<int:restaurant_id>')
@app.route('/restaurants/<int:restaurant_id>/menu')
def showMenu(restaurant_id):
    return('Users will use this page to view the menu for restaurant %s' % restaurant_id)

# Web Page #6 - add a new item to the menu
@app.route('/restaurants/<int:restaurant_id>/menu/new')
def newMenuItem(restaurant_id):
    return('Users will use this page to add a new item to restaurant %s' % restaurant_id)

# Web Page #7 - edit a current item on a restaurant's menu
@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/edit')
def editMenuItem(restaurant_id, menu_id):
    return('Users will use this page to edit item %s' % menu_id)

# Web Page #8 - delete a current item on a restaurant's menu
@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/delete')
def deleteMenuItem(restaurant_id, menu_id):
    return('Users will use this page to delete item %s' % menu_id)


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)

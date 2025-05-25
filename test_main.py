from main import Item, ShoppingCart

def test_item_has_name_and_price():
    apple = Item("apple", 50)
    assert apple.name == "apple"
    assert apple.price == 50

def test_shopping_cart_can_add_item():
    cart = ShoppingCart()  
    apple = Item("apple", 50) 
    cart.add(apple)
    assert cart.items == "apple "

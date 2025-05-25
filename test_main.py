from main import Item

def test_item_has_name_and_price():
    apple = Item("apple", 50)
    assert apple.name == "apple"
    assert apple.price == 50
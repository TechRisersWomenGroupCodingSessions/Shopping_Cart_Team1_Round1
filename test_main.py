def test_item_has_name_and_price():
    apple = Item("apple", 50)
    expect apple["name"] == "apple"
    expect apple["price"] == 50
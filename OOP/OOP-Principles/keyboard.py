from item import Item

class Keyboard(Item):
  pay_rate = 0.7
  def __init__(self, name: str, price: float, quantity=0):
    # Call to super function to have access to all attributes and methods from parent class Item
    super().__init__(name, price, quantity)
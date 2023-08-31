#!/usr/bin/env python3

class CashRegister:
  
  def __init__(self, discount=0):
    self.discount = discount
    self.total=0
    self.items=[]

  def add_item(self, title, price, quantity=1):
    self.total+=price*quantity
    self.title=title
    self.price=price
    self.quantity = quantity
    i=0
    while i<quantity :
      self.items.append(title)
      i+=1

  def apply_discount(self):
    if(self.total==0):
      print('There is no discount to apply.')
    else:
      self.total= self.total*0.8
      print(f'After the discount, the total comes to ${int(self.total)}.')
  
  def void_last_transaction(self):
    self.total -= self.price*self.quantity
    i=0
    while i<self.quantity :
      self.items.pop()
      i+=1


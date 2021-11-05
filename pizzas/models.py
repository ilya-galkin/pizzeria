from django.db import models

class Pizza(models.Model):
	'''A pizza that you can order.'''
	name = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		'''Return a string representation of the model.'''
		return self.name

class Topping(models.Model):
	'''Toppings of selected kind of pizza.'''
	pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
	text = models.TextField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		'''Return a string representation of the model.'''
		return self.text


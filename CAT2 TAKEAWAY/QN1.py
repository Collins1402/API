'''QUESTION ONE [10 Marks]
1. Data Relationships in Django Models:
E-Commerce
a. Create Django models for a Customer and Order, where a customer can
place multiple orders, and each order is associated with only one customer.
b. Define the relationship between the Customer and Order models, including
relevant fields (e.g., name, email for Customer, and order_date,
total_amount for Order).
c. Create the necessary migrations and commit them to your repository.
Include comments explaining the relationships defined and any choices
made regarding fields and relationships.
Create a README.md file with detailed instructions for:
• Setting up the environment and running the project.
• Upload your project, including all code and documentation, to a GitHub repository.'''

from django.db import models
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.id} by {self.customer.name}"
    
    
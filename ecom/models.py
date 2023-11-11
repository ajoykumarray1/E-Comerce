from django.db import models

# Create your models here.
category_choice=(
    ('ML','Milk'),
    ('CK','Chocklet'),
    ('BT','Butter'),
    ('CP','Chips'),
    ('BG','Burger'),
    ('PZ','Pizza'),
    ('GE','Ghee'),
    ('CD','CURD'),    
)
class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discount_price=models.FloatField()
    description=models.TextField()
    composition=models.TextField()
    product_app=models.TextField()
    category=models.CharField(choices=category_choice, max_length=2)
    product_image=models.ImageField(upload_to='product', null= True)
    def __str__(self):
        return self.title
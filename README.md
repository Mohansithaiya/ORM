# Ex03 Django ORM Web Application
## Date: 13-09-2024

## AIM
To develop a Django application to store and retrieve data from a Book database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM
![alt text](<Screenshot 2024-09-13 202807.png>)


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
models.py
from django.db import models
from django.contrib import admin
class Bankloans(models.Model):
	Loan_id=models.IntegerField(primary_key=True);
	Name=models.CharField(max_length=30);
	Loan_amt=models.IntegerField();
	Mail_id=models.CharField(max_length=30);
	Account_no=models.IntegerField();
class BankloansAdmin(admin.ModelAdmin):
	list_display=("Loan_id","Name","Loan_amt","Mail_id","Account_no");

```
```
admin.py
from django.contrib import admin
from .models import Bankloans,BankloansAdmin
admin.site.register(Bankloans,BankloansAdmin)
```

## OUTPUT
![alt text](<Screenshot 2024-09-13 195925.png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully

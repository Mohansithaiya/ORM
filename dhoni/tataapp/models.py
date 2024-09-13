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

from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User


# Create your models here.

class Registration(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    
#    username=models.CharField(max_length=30,blank=True,null=True)

    DATE=(
        ("20","20"),
        ("21","21"),
        ("22","22"),
        ("23","23"),
        ("24","24"),
        ("25","25"),
        ("26","26"),
        ("27","27"),
        ("28","28"),
        ("29","29")
    )
    #email=models.EmailField(default="",unique=True)
    DateMin=models.DateTimeField()
    DateMax=models.DateTimeField()
    
    
    
    AccountID=models.CharField(default="",max_length=128,unique=True)
    # APIPassword=""

    def __str__(self):
        return self.user.username

class TransactionTable(models.Model):
    #User=models.ForeignKey(Registration,related_name="listings")
    
    Transaction_id=models.CharField(max_length=10)
    Transaction_Type=models.CharField(max_length=5)
    Transaction_Amount=models.CharField(max_length=10)
    Transaction_weight=models.CharField(max_length=10)
    Transaction_status=models.CharField(max_length=5)
    Transaction_Description=models.CharField(max_length=500)

'''    
    _TransactionDateTime = "01/27/2017 16:34:14"
         _TransactionType = "PRINT"
         _PostmarkDate = "01/27/2017 16:34:14"
         PIC = "9400115901301245000917"
         TransactionID = 4514719002
         PieceID = "335801"
         Amount = "$2.61"
         Weight = "3 Oz."
         MailClass = "First Class;Package Service;Delivery Confirmation"
         ToAddress =
            (TransactionAddress){
               Company = None
               Name = "Laurie Thomas"
               Phone = "8772546155"
               Email = "lthomas0309@gmail.com"
               AddressLines =
                  (AddressLines){
                     AddressLine1 = "12724 NW 75th Ter"
                  }
               City = "Alachua"
               State = "FL"
               PostalCode = "32615"
               Zip4 = "6305"
               Country = None
            }
         FromAddress = ""
         CostCenter = "0"
         ReferenceID = None
         RetailAccountID = None
         RetailAmount = None
         ContractID = None
         Status =
            (TransactionStatus){
               StatusEvent = "N   "
               StatusDescription = "The tracking information for this item was received by the US Postal Service at Jan 28, but the item has not yet been scanned in the mailstream.  Please check back later."
               DeliveryDateTime = "1/28/2017 4:05:00 AM"
            }
         Zone = "5"
'''
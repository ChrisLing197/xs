from django import forms
from django.contrib.auth.forms import UserCreationForm
from ys import models
from django.contrib.auth.models import User
import datetime
from .Endicia import Endicia
from datetime import timedelta

class RegistrationForm(UserCreationForm):
    
    email=forms.EmailField(required=True)

    APIPassphrase=forms.CharField(widget=forms.PasswordInput())
    WEBPassword=forms.CharField(widget=forms.PasswordInput())
    AccountID=forms.CharField(max_length=32)

    DateMin=forms.DateTimeField(help_text='Enter date as MM/DD/YYYY')
    DateMax=forms.DateTimeField(help_text='Enter date as MM/DD/YYYY')
    
    
    class Meta:
        model=models.User
        fields=('username','email','password1','password2','APIPassphrase','WEBPassword','AccountID')#,'Passphrase')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        
        return email
    
    
    def clean_AccountID(self):
        accountID=self.cleaned_data['AccountID']
        for user in models.Registration.objects.all():
            if user.AccountID==accountID:
                raise forms.ValidationError("account id already exists")
        endicia=Endicia(self.cleaned_data['AccountID'],self.cleaned_data['APIPassphrase'])
        if endicia.get_account_status()['status']==401:
            raise forms.ValidationError("Endicia status invalid")
        
        #tempdict=endicia.get_transaction_listing(datetime.datetime.now()-timedelta(days=30),datetime.datetime.now(),'ALL')
        
        #table=models.TransactionTable()
        #for x in tempdict['response']:
        #    if x['Status']['StatusEvent'] == None:
        #        SE=''
        #    else:
        #        SE=x['Status']['StatusEvent']
        #    if x['Status']['StatusDescription'] == None:
        #        SD=''
        #    else:
        #        SD=x['Status']['StatusDescription']
           
        #    _table = models.TransactionTable(Transaction_id=x['TransactionID'],Transaction_Type=x['TransactionType'],\
        #                                Transaction_Amount=x['Ammount'],Transaction_weight=x['Weight'],\
        #                                Transaction_status=SE,Transaction_Description=SD)
        #    _table.save()
        
        return accountID
        
    #def clean(self):
    #    cleaned_data = super(RegistrationForm, self).clean()
    #    for user in models.Registration.objects.all():
    #        if user.AccountID==accountID:
    #            raise forms.ValidationError("account id already exists")
                
    #        user=super(RegistrationForm,self).save(commit=False)
    #        user.username=self.cleaned_data['username']
    #        user.save()
            
            #table.Transaction_id=x['TransactionID']
            #table.Transaction_Type=x['TransactionType']
            #table.Transaction_Amount=x['Ammount']
            #table.Transaction_weight=x['Weight']
            #table.Transaction_status=x['Status']['StatusEvent']
            #table.Transaction_Description=x['Status']['StatusDescription']
            
            #print(x['Status']['StatusDescription'])
            #table.save(self)
      #  return cleaned_data
        
    def clean_DateMax(self):
        DateMin = self.cleaned_data['DateMin']
        DateMax = self.cleaned_data['DateMax']
        past=DateMin-timedelta(days=20)
        future=DateMin+timedelta(days=29)
        if self.cleaned_data['DateMax'] <past or self.cleaned_data['DateMax'] >future or self.cleaned_data['DateMin'] <past or self.cleaned_data['DateMin'] >future:
            raise forms.ValidationError("Date out of range")
        return DateMax

    def save(self,commit=True):
        user=super(RegistrationForm,self).save(commit=False)
        user.username=self.cleaned_data['username']
        try:
            user.email=self.cleaned_data['email']
        except AttributeError as attr:
            print(str(attr))
        reg=models.Registration()
        try:
            reg.DateMin=self.cleaned_data['DateMin']
        except AttributeError as attr:
            print(str(attr))
        try:
            reg.DateMax=self.cleaned_data['DateMax']
        except AttributeError as attr:
            print(str(attr))
        try:
            reg.AccountID=self.cleaned_data['AccountID']
        except AttributeError as attr:
            print(str(attr))
        try:
            reg.WEBPassword=self.cleaned_data['WEBPassword']
        except AttributeError as attr:
            print(str(attr))
        try:
            reg.APIPassphrase=self.cleaned_data['APIPassphrase']
        except AttributeError as attr:
            print(str(attr))
            
        
        
            #self._errors["DateMin"] = ["Date out of range"]
            #del self.cleaned_data['DateMin']
        if commit:
            user.save()
            reg.user=user
            #reg.save()
            #raise forms.ValidationError("Date Min must be less than date max.")
        #except:
            #1-1
        return user
        
        

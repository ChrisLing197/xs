import suds
import urllib
from suds.client import Client
from datetime import datetime, timedelta
import logging
from suds.xsd.doctor import Import, ImportDoctor
from suds.sax.element import Element
import time

class Endicia:
	def __init__(self,AccountID,PassPhrase):
		self.WSDL = 'https://LabelServer.Endicia.com/LabelService/EwsLabelService.asmx?wsdl'
		self.AccountID = AccountID
		self.RequesterID = 'lsll'
		self.PassPhrase  = PassPhrase
		
		# imp =  Import('http://www.w3.org/2001/XMLSchema-instance', location='http://www.w3.org/2001/XMLSchema.xsd')
		# self.imp.filter.add("Test=No")
		# doctor = ImportDoctor(imp)
		self.client = Client(self.WSDL)
		

		

	def get_account_status(self):
		#logging.basicConfig(level=logging.INFO)
		#logging.getLogger('suds.client').setLevel(logging.DEBUG)
	
		AccountStatusRequest = self.client.factory.create('AccountStatusRequest')
		AccountStatusRequest.RequesterID = self.RequesterID
		AccountStatusRequest.RequestID = 'lsll'
		AccountStatusRequest.CertifiedIntermediary.AccountID = self.AccountID
		AccountStatusRequest.CertifiedIntermediary.PassPhrase = self.PassPhrase
		account_status = self.client.service.GetAccountStatus(AccountStatusRequest)
		if account_status.Status == 0:
			return {
				"status":200,
				"message":"Successful request"
			}
		else:
			return {
				"status":401,
				"message":"Invalid Credentials"
			}


	def get_transaction_listing(self,start_date,end_date,status):
		GetTransactionsListingRequest =  self.client.factory.create('GetTransactionsListingRequest')
		GetTransactionsListingRequest.RequesterID = self.RequesterID
		GetTransactionsListingRequest.RequestID = 'lsll'
		GetTransactionsListingRequest.CertifiedIntermediary.AccountID = self.AccountID
		GetTransactionsListingRequest.CertifiedIntermediary.PassPhrase =  self.PassPhrase
		# GetTransactionsListingRequest.RequestOptions._StartDateTime = past
		# GetTransactionsListingRequest.RequestOptions._EndDateTime = _now
		# GetTransactionsListingRequest.RequestOptions._RefundStatus = status
		response = []
		transaction_listing = self.client.service.GetTransactionsListing(GetTransactionsListingRequest)
		for result in transaction_listing.TransactionsResults.Transaction:
			temp = {}

			try:
				# print(result.ToAddress)
				temp.update({
					'TransactionDateTime':result._TransactionDateTime,
					'TransactionType':result._TransactionType,
					'PostmarkDate':result._PostmarkDate,
					'PIC':result.PIC,
					'TransactionID':result.TransactionID,
					'PieceID':result.PieceID,
					'Ammount':result.Amount.split('$')[1],
					'Weight':result.Weight,
					'MailClass':result.MailClass,
					'ToAddress':{
						'Company':result.ToAddress.Company,
						'Name':result.ToAddress.Name,
						'Phone':result.ToAddress.Phone,
						'Email':result.ToAddress.Email,
						'Address1':result.ToAddress.AddressLines.AddressLine1,
						'City':result.ToAddress.City,
						'State':result.ToAddress.State,
						'PostalCode':result.ToAddress.PostalCode,
						'Country':result.ToAddress.Country
					},
					'FromAddress':result.FromAddress,
					'CostCenter':result.CostCenter,
					'ReferenceID':result.ReferenceID,
					'RetailAccountID':result.RetailAccountID,
					'RetailAmount':result.RetailAmount,
					'ContractID':result.ContractID,
					'Status':{
						'StatusEvent':result.Status.StatusEvent,
						'StatusDescription':result.Status.StatusDescription,
						'DeliveryDateTime':result.Status.DeliveryDateTime
					},
					'Zone':result.Zone
				})
				
				response.append(temp)
			except AttributeError as ae:
				1+1
				
				
			

		if transaction_listing.Status != 0:
			return {
				"StatusCode":401,
				"Message":"Malformed Request"
			}
		else:
			return{
				"StatusCode":200,
				"Message":"IT worked",
				"response":response
			}

	def request_refund(self,pic_numbers):
		RequestRefund = self.client.factory.create('RefundRequest')
		RequestRefund.RequesterID =self.RequesterID
		RequestRefund.RequestID = '2'
		RequestRefund.CertifiedIntermediary.AccountID = self.AccountID
		RequestRefund.CertifiedIntermediary.PassPhrase = self.PassPhrase
		RequestRefund.PicNumbers.PicNumber = pic_numbers
		print(self.client.service.GetRefund(RequestRefund))




if __name__ == '__main__':
	endicia = Endicia('747049','Clickgoandbuy')
	past = str(datetime.now()-timedelta(20)).split(' ')[0]
	_now = str(datetime.now()).split(' ')[0]
	print(endicia.get_transaction_listing(past,_now,"ALL")['response'])
# 	print(endicia.get_transaction_listing(_now,past,"ALL"))
# 	# endicia.request_refund()
# 	# print(endicia.get_account_status())
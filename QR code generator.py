import qrcode

#taking upi id as input

upi_id=input("Enter your UPI ID: ") 

#upi://pay?pa=UPI_ID&pn=NAME&am=AMOUNT&cu=CURRENCY&tn=MESSAGE

#Defining the payment url based on the upi id and the payment app
#you can modify  these urls based on the payments apps you want to support

phonepe_url=f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
paytm_url=f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
Gpay_url=f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"

#create qr codes for each payment app

phonepe_qr=qrcode.make(phonepe_url)
paytm_qr=qrcode.make(paytm_url)
Gpay_qr=qrcode.make(Gpay_url)


#save the qr code in image file optional

# phonepe_qr.save("phonepe_qr.png")
# paytm_qr.save("paytm_qr.png")
# Gpay_qr.save("Gpay_qr.png")


#dispaly qr code

phonepe_qr.show()
paytm_qr.show()
Gpay_qr.show()  
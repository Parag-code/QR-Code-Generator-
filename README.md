# QR-Code-Generator-

A Python-based tool that generates UPI QR codes for multiple payment apps (PhonePe, Paytm, and Google Pay). This tool allows you to easily create QR codes for receiving payments via UPI by inputting your UPI ID, recipient name, and the amount to be paid.

Features
Multi-App Support: Generates QR codes for PhonePe, Paytm, and Google Pay.
Customizable Payment Information: Allows the user to specify the recipient's name, UPI ID, and payment amount.
Automatic QR Code Generation: Automatically generates UPI payment URLs and converts them into QR codes.
Save and Display: Saves generated QR codes as PNG image files and displays them for easy use.
Requirements
Python 3.x
Required Python libraries:
qrcode
Pillow (optional, for saving images)
You can install the required libraries using the following command:

bash
Copy code
pip install qrcode[pil]
How to Use
Clone or download this repository to your local machine.
Navigate to the project directory in your terminal or command prompt.
Run the script by executing the following command:
bash
Copy code
python qr_code_generator.py
The script will prompt you for:

UPI ID: Your UPI ID (e.g., yourupi@upi).
Recipient's Name: The name of the person or organization receiving the payment.
Amount: The amount to request for the payment.
After entering the details, the script will generate QR codes for each payment app (PhonePe, Paytm, and Google Pay), display them on the screen, and save the QR codes as .png files (e.g., phonepe_qr.png, paytm_qr.png, gpay_qr.png) in the current directory.

Example Input:
mathematica
Copy code
Enter your UPI ID: yourupi@upi
Enter the recipient's name: John Doe
Enter the amount: 500
Example Output:
The script will display and save the following QR codes:

PhonePe QR Code
Paytm QR Code
Google Pay QR Code
These QR codes can be scanned by users to make payments directly to the specified UPI ID.

Code Explanation
User Input:

The script asks the user for their UPI ID, recipient's name, and payment amount.
Generating UPI Payment URLs:

The UPI payment URLs are formatted for each of the three payment apps: PhonePe, Paytm, and Google Pay. The format is:
arduino
Copy code
upi://pay?pa=UPI_ID&pn=RECIPIENT_NAME&am=AMOUNT&cu=CURRENCY&tn=TRANSACTION_NOTE
pa: UPI ID of the receiver.
pn: Name of the recipient.
am: Amount to be paid.
cu: Currency code (usually INR for Indian Rupees).
tn: Transaction note (optional).
Generating QR Codes:

Using the qrcode library, the URLs are converted into QR codes.
The QR codes are saved as PNG files (phonepe_qr.png, paytm_qr.png, gpay_qr.png) and are also displayed for immediate use.

QR Code Display:

The generated QR codes are displayed in pop-up windows using the show() method of the qrcode library.

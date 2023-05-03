# Import QRCode from pyqrcode
import qrcode

url = input("Enter the website: ")
img = qrcode.make(url)
img.save('website_qr.png')

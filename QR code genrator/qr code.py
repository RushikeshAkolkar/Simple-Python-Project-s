#----------------------google qrcode genrator-----------------------------
import qrcode as qr

img = qr.make("www.google.com")
img.save("google.png")

#----------------------------My Phone pay qr code genrator----------------
import qrcode as qr

img = qr.make("8888440539@ybl")
img.save("Rushikesh_Akolkar_Phone_pay_QR_Code_genrator.png")

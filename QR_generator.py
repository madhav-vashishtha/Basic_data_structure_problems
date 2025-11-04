import qrcode


data = "https://www.youtube.com/watch?v=9T-Zbxg9X_4&list=RD9T-Zbxg9X_4&start_radio=1" 


img = qrcode.make(data)
img.save("myqr.png")

print("QR code successfully saved as myqr.png!")

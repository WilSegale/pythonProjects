import qrcode

data = "https://google.com"
filename = "QR.jpg"
img = qrcode.make(data)
img.save(filename)
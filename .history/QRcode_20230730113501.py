# Importing library
import qrcode

# Data to be encoded
data = 'https://www.youtube.com/watch?v=xm3YgoEiEDc'

# Encoding data using make() function
img = qrcode.make(data)

# Saving as an image file
img.save('MyQRCode1.png')
os.system('open MyQRCode1.png')


#import library
import qrcode
#create QR
img = qrcode.make('https://www.jw.org/es/')
type(img)
img.save("test001.png")
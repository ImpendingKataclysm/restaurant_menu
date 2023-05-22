import qrcode

APP_URL = 'https://127.0.0.1:8000'

image = qrcode.make(APP_URL)
image.save("qr.png")

import qrcode

# Create instance of QRCode
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR Code; 1 is the smallest
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # about 7% or fewer errors can be corrected
    box_size=20,  # size of each box in pixels
    border=2,  # thickness of the border (default is 4)
)

# Add data to the instance
data = "https://t.co/pKonn0ydxy"
qr.add_data(data)
qr.make(fit=True)  # fit=True adjusts the size of the QR Code to fit the data

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("qrcode_example.png")

import qrcode
from IPython.display import display

# Define the LinkedIn URL
linkedin_url = "https://www.linkedin.com/in/bugraozkan/"

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(linkedin_url)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill='black', back_color='white')

# Display the QR code
display(img)

# Save the QR code to a file
img.save("qr.png")

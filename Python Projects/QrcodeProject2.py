import qrcode
from PIL import Image
import qrcode.constants
qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=4,)
qr.add_data("https://youtu.be/ZQH-BuU8Ol8?si=GjytU3rD03_pqSNL")
qr.make(fit=True)
img=qr.make_image(fill_color="Red",back_color="Yellow")
img.save("New_Version Qrcode2.png")

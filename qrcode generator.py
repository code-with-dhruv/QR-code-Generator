import qrcode
from PIL import Image

def qrcodemake(k):
    qr=qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(k)

    qr.make(fit=True)

    img=qr.make_image(fill_color='black',back_color='white')
    img.save('Example.png')

    img=Image.open('Example.png')
    img.show()
k=input("Path to be redirected to")
qrcodemake(k)

import qrcode;
#simple qrcode
qrcode.make("text").save("1.png")
#Custom qrcode:
# qr = qrcode.QRCode(version = 1, box_size=10, border=5);
# qr.add_data("text");
# qr.make(fit=True);
# img = qr.make_image(fill_color = "red", back_color = "white");
# img.save("2.png")

#2-20mins 09/05/2022
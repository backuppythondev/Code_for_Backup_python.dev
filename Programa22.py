import qrcode as qr


# autor: backup_python.dev

qr_code = qr.make("https://chat.whatsapp.com/Bp7yF7p034n2oJiSMGiLNl") 
qr_code.save("whatsapp.png")

qr_code.show()

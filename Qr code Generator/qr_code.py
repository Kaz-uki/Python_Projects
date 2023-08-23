import qrcode as qr
img = qr.make("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
img.save("click_me.png")

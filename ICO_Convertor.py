from PIL import Image

img = Image.open("countdown_app.png")
img.save("app_icon.ico", format="ICO")
import io
from urllib.request import urlopen
from PIL import Image, ImageTk

class Helper:
    def getImage(show):
        if show.image == "": return None
        
        imgBuffer = urlopen(show.image).read()
        imgBytes = io.BytesIO(imgBuffer)
        imgFull = Image.open(imgBytes)
        imgMin = imgFull.resize((150, 150))
        photo = ImageTk.PhotoImage(imgMin)
        
        return photo
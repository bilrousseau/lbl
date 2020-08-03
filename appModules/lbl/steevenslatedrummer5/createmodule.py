import os
import ui
import tones

from ..api.ocr import LBLOCR
from ..api.mouse import Mouse

mouse = Mouse()

col1 = {
    "position": 1,
    "diagonal": [132, 50, 407, 70],
}

col2 = {
    "position": 1,
    "diagonal": [412, 50, 672, 70]
}

def resetColumns():
    col1["position"] = 1
    col1["diagonal"] = [132, 50, 407, 70]
    col2["position"] = 1
    col2["diagonal"] = [412, 50, 672, 70]

def getLibraryNumber():
    return len(os.listdir("c:/Program Files/SSD5Library/DrumKitPresets"))

def getCategoryNumber():
    lib = os.listdir("c:/Program Files/SSD5Library/DrumKitPresets")[col1["position"] - 1]
    path = "c:/Program Files/SSD5Library/DrumKitPresets/" + lib

    return len(os.listdir(path))

def getLibrary(key = None, libraryNumber = 0):
    if key == "down":
        if col1["position"] < libraryNumber:
            col1["position"] += 1
            col1["diagonal"][1] += 20
            col1["diagonal"][3] += 20
    elif key == "up":
        if col1["position"] > 1:
            col1["position"] -= 1
            col1["diagonal"][1] -= 20
            col1["diagonal"][3] -= 20
        
    mouse.moveAndLeftClick(col1["diagonal"][0] + 5, col1["diagonal"][1] + 5)

    return LBLOCR.getText(col1["diagonal"])

def getCategory(key = None, categoryNumber = 0):
    if key == "down":
        if col2["position"] < categoryNumber:
            col2["position"] += 1
            col2["diagonal"][1] += 20
            col2["diagonal"][3] += 20
    elif key == "up":
        if col2["position"] > 1:
            col2["position"] -= 1
            col2["diagonal"][1] -= 20
            col2["diagonal"][3] -= 20
        
    mouse.moveAndLeftClick(col2["diagonal"][0] + 5, col2["diagonal"][1] + 5)

    return LBLOCR.getText(col2["diagonal"])

# Dictionnaire contenant les paramètres du tableau Kits
kitsParams = {
    "name": "Kits",
    "libraryNumber": getLibraryNumber,
    "library": getLibrary,
    "categoryNumber": getCategoryNumber,
    "category": getCategory
}

# Dictionnaire contenant les paramètres du tableau Instruments
instrumentsParams = {
    "name": "Instruments",
    "libraryNumber": getLibraryNumber,
    "library": getLibrary,
}

# Liste des dictionnaires correspondant aux parties de l'onget Create
createObject = [
    kitsParams,
    instrumentsParams
]

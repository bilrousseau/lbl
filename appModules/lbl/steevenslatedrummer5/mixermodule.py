import time
import tones
import ui
from ..api.mouse import Mouse
from ..api.navobject import NavObject
from ..api.ocr import LBLOCR
from .ocrdictionnary import ocrDictionnary
from .routingmenu32 import routingMenu32
from .routingmenu36 import routingMenu36

mouse = Mouse()
menu32 = NavObject(routingMenu32)
menu36 = NavObject(routingMenu36)

def setVolume(key = None, volumeX = 0, volumeY = 0, pieceX = 0, pieceY = 0):
    if key == "up":
        mouse.moveAndScrole(volumeX, volumeY, 20)
        mouse.moveAndLeftClick(pieceX, pieceY)
    elif key == "down":
        mouse.moveAndScrole(volumeX, volumeY, -20)
        mouse.moveAndLeftClick(pieceX, pieceY)

def setPanoramic(key = None, panoramicX = 0, panoramicY = 0, pieceX = 0, pieceY = 0):
    if key == "left":
        mouse.moveAndScrole(panoramicX, panoramicY, -20)
        mouse.moveAndLeftClick(pieceX, pieceY)
    elif key == "right":
        mouse.moveAndScrole(panoramicX, panoramicY, 20)
        mouse.moveAndLeftClick(pieceX, pieceY)

def setState(diagonal = []):
    return "Changement de l'état muté, ou non muté"

def setRouting(key = None, routingButtonX = 0, routingButtonY = 0, ocrDiagonal = [], menuSize = 0):
    if menuSize == 32:
        menu = menu32
    elif menuSize == 36:
        menu = menu36

    if key == "enter":
        ocrResult = LBLOCR.getText(ocrDiagonal)
        selectedItem = LBLOCR.getCorrection(ocrResult, ocrDictionnary)
        mouse.moveAndLeftClick(routingButtonX, routingButtonY)
        menu.goToObjectByName(selectedItem)
        return selectedItem
    elif key == "up":
        return menu.getPreviousObject()
    elif key == "down":
        return menu.getNextObject()

kickInParams = {
    "name": "Kick In",
    "x": 514,
    "y": 535,
    "stateDiagonal": [],
    "volumeX": 458,
    "volumeY": 195,
    "volumeDiagonal": [478, 185, 528, 205],
    "panoramicX": 548,
    "panoramicY": 195,
    "panoramicDiagonal": [568, 185, 618, 205],
    "routingButtonX": 420,
    "routingButtonY": 195,
    "routingDiagonal": [309, 185, 444, 205],
    "menuSize": 32,
    "volume": setVolume,
    "panoramic": setPanoramic,
    "state": setState,
    "routing": setRouting
}

kickOutParams = {
    "name": "Kick Out",
    "x": 514,
    "y": 535,
    "stateDiagonal": [],
    "volumeX": 458,
    "volumeY": 225,
    "volumeDiagonal": [478, 215, 528, 235],
    "panoramicX": 548,
    "panoramicY": 235,
    "panoramicDiagonal": [568, 215, 618, 235],
    "routingButtonX": 420,
    "routingButtonY": 225,
    "routingDiagonal": [309, 215, 444, 235],
    "menuSize": 32,
    "volume": setVolume,
    "panoramic": setPanoramic,
    "state": setState,
    "routing": setRouting
}

mixerObject = [
    kickInParams,
    kickOutParams
]

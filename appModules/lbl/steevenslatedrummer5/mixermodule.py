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
    color = LBLOCR.getColor(diagonal)

    if color == "#59caf5":
        state = "Muté"
    elif color == "#143650":
        state = "Non muté"
    else:
        return "Etat Inconnu"
    mouse.moveAndLeftClick(diagonal[0], diagonal[1])
    return state

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
    "stateDiagonal": [157, 195, 158, 196],
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

snareTopParams = {
    "name": "Snare Top",
    "x": 418,
    "y": 494,
    "stateDiagonal": [157, 195, 158, 196],
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

snareBottomParams = {
    "name": "Snare Bottom",
    "x": 418,
    "y": 494,
    "stateDiagonal": [157, 195, 158, 196],
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

tom1Params = {
    "name": "Tom 1",
    "x": 437,
    "y": 433,
    "stateDiagonal": [157, 195, 158, 196],
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

tom2Params = {
    "name": "Tom 2",
    "x": 498,
    "y": 423,
    "stateDiagonal": [157, 195, 158, 196],
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

tom3Params = {
    "name": "Tom 3",
    "x": 608,
    "y": 491,
    "stateDiagonal": [157, 195, 158, 196],
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

tom4Params = {
    "name": "Tom 4",
    "x": 658,
    "y": 538,
    "stateDiagonal": [157, 195, 158, 196],
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

hihatParams = {
    "name": "Hi-Hat",
    "x": 360,
    "y": 476,
    "stateDiagonal": [157, 195, 158, 196],
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

cymbal1Params = {
    "name": "Cymbal 1",
    "x": 438,
    "y": 374,
    "stateDiagonal": [157, 195, 158, 196],
    "volumeX": 458,
    "volumeY": 195,
    "volumeDiagonal": [478, 185, 528, 205],
    "panoramicX": 548,
    "panoramicY": 195,
    "panoramicDiagonal": [568, 185, 618, 205],
    "routingButtonX": 420,
    "routingButtonY": 195,
    "routingDiagonal": [309, 185, 444, 205],
    "menuSize": 36,
    "volume": setVolume,
    "panoramic": setPanoramic,
    "state": setState,
    "routing": setRouting
}

cymbal2Params = {
    "name": "Cymbal 2",
    "x": 663,
    "y": 381,
    "stateDiagonal": [157, 195, 158, 196],
    "volumeX": 458,
    "volumeY": 195,
    "volumeDiagonal": [478, 185, 528, 205],
    "panoramicX": 548,
    "panoramicY": 195,
    "panoramicDiagonal": [568, 185, 618, 205],
    "routingButtonX": 420,
    "routingButtonY": 195,
    "routingDiagonal": [309, 185, 444, 205],
    "menuSize": 36,
    "volume": setVolume,
    "panoramic": setPanoramic,
    "state": setState,
    "routing": setRouting
}

cymbal3Params = {
    "name": "Cymbal 3",
    "x": 383,
    "y": 414,
    "stateDiagonal": [157, 195, 158, 196],
    "volumeX": 458,
    "volumeY": 195,
    "volumeDiagonal": [478, 185, 528, 205],
    "panoramicX": 548,
    "panoramicY": 195,
    "panoramicDiagonal": [568, 185, 618, 205],
    "routingButtonX": 420,
    "routingButtonY": 195,
    "routingDiagonal": [309, 185, 444, 205],
    "menuSize": 36,
    "volume": setVolume,
    "panoramic": setPanoramic,
    "state": setState,
    "routing": setRouting
}

cymbal4Params = {
    "name": "Ride",
    "x": 583,
    "y": 423,
    "stateDiagonal": [157, 195, 158, 196],
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

cymbal5Params = {
    "name": "Cymbal 5",
    "x": 717,
    "y": 457,
    "stateDiagonal": [157, 195, 158, 196],
    "volumeX": 458,
    "volumeY": 195,
    "volumeDiagonal": [478, 185, 528, 205],
    "panoramicX": 548,
    "panoramicY": 195,
    "panoramicDiagonal": [568, 185, 618, 205],
    "routingButtonX": 420,
    "routingButtonY": 195,
    "routingDiagonal": [309, 185, 444, 205],
    "menuSize": 36,
    "volume": setVolume,
    "panoramic": setPanoramic,
    "state": setState,
    "routing": setRouting
}

mixerObject = [
    kickInParams,
    kickOutParams,
    snareTopParams,
    snareBottomParams,
    tom1Params,
    tom2Params,
    tom3Params,
    tom4Params,
    hihatParams,
    cymbal1Params,
    cymbal2Params,
    cymbal3Params,
    cymbal4Params,
    cymbal5Params
]

import tones
from ..api.mouse import Mouse
from ..api.ocr import LBLOCR

mouse = Mouse()

def setVolume(arrow = None, x = 0, y = 0):
    if arrow == "up":
        return "Plus fort"
    elif arrow == "down":
        return "Moins fort"

def setPanoramic(arrow = None, x = 0, y = 0):
    if arrow == "left":
        return "Plus à gauche"
    elif arrow == "right":
        return "Plus à droite"

def setState(xLeft = 0, yLeft = 0, xRight = 0, yRight = 0):
    return "Changement de l'état muté, ou non muté"

kickInParams = {
    "name": "Kick In",
    "x": 514,
    "y": 535,
    "stateXLeft": 0,
    "stateYLeft": 0,
    "stateXRight": 0,
    "stateYRight": 0,
    "volumeX": 0,
    "volumeY": 0,
    "panoramicX": 0,
    "panoramicY": 0,
    "volume": setVolume,
    "panoramic": setPanoramic,
    "state": setState
}

kickOutParams = {
    "name": "Kick Out",
    "x": 514,
    "y": 535,
    "stateXLeft": 0,
    "stateYLeft": 0,
    "stateXRight": 0,
    "stateYRight": 0,
    "volumeX": 0,
    "volumeY": 0,
    "panoramicX": 0,
    "panoramicY": 0,
    "volume": setVolume,
    "panoramic": setPanoramic,
    "state": setState
}

mixerObject = [
    kickInParams,
    kickOutParams
]

import tones
from ..api.mouse import Mouse
from ..api.ocr import LBLOCR
import time

mouse = Mouse()

def setVolume(arrow, x = 0, y = 0):
    """
        Ajustement du volume de la pièce
    """

    if arrow == "right":
        mouse.moveAndScrole(332, 77, 50)
    elif arrow == "left":
        mouse.moveAndScrole(332, 77, -50)
    mouse.moveAndLeftClick(x, y)

def setAttack(arrow, x, y):
    """
        Ajustement de l'attaque de la pièce
    """

    if arrow == "right":
        mouse.moveAndScrole(700, 188, 34)
    elif arrow == "left":
        mouse.moveAndScrole(700, 188, -34)
    mouse.moveAndLeftClick(x, y)
    return attack

def setDecay(arrow, x, y):
    """
        Ajustement du decay de la pièce
    """

    if arrow == "right":
        mouse.moveAndScrole(760, 188, 34)
    elif arrow == "left":
        mouse.moveAndScrole(760, 188, -34)
    mouse.moveAndLeftClick(x, y)
    return decay

def setSustain(arrow, x, y):
    """
        Ajustement du sustain de la pièce
    """

    if arrow == "right":
        mouse.moveAndScrole(830, 188, 34)
    elif arrow == "left":
        mouse.moveAndScrole(830, 188, -34)
    mouse.moveAndLeftClick(x, y)
    return sustain

def setRelease(arrow, x, y):
    """
        Ajustement du release de la pièce
    """

    if arrow == "right":
        mouse.moveAndScrole(890, 188, 34)
    elif arrow == "left":
        mouse.moveAndScrole(890, 188, -34)
    mouse.moveAndLeftClick(x, y)
    return release

# Dictionnaire regroupant les paramètres de la grosse caisse
kickParams = {
    "name": "Kick",
    "x": 514,
    "y": 535,
    "volume": setVolume,
    "attack": setAttack,
    "decay": setDecay,
    "sustain": setSustain,
    "release": setRelease,
}

# Dictionnaire regroupant les paramètres de la caisse claire
snareParams = {
    "name": "Snare",
    "x": 418,
    "y": 494,
    "volume": setVolume,
    "attack": setAttack,
    "decay": setDecay,
    "sustain": setSustain,
    "release": setRelease,
}

# Dictionnaire regroupant les paramètres du tom 1
tom1Params = {
    "name": "Tom 1",
    "x": 437,
    "y": 433,
    "volume": setVolume,
    "attack": setAttack,
    "decay": setDecay,
    "sustain": setSustain,
    "release": setRelease,
}

# Dictionnaire regroupant les paramètres du tom 2
tom2Params = {
    "name": "Tom 2",
    "x": 498,
    "y": 423,
    "volume": setVolume,
    "attack": setAttack,
    "decay": setDecay,
    "sustain": setSustain,
    "release": setRelease,
}

# Dictionnaire regroupant les paramètres du tom 3
tom3Params = {
    "name": "Tom 3",
    "x": 608,
    "y": 491,
    "volume": setVolume,
    "attack": setAttack,
    "decay": setDecay,
    "sustain": setSustain,
    "release": setRelease,
}

# Dictionnaire regroupant les paramètres du tom 4
tom4Params = {
    "name": "Tom 4",
    "x": 658,
    "y": 538,
    "volume": setVolume,
    "attack": setAttack,
    "decay": setDecay,
    "sustain": setSustain,
    "release": setRelease,
}

# Dictionnaire regroupant les paramètres du charley
hihatParams = {
    "name": "Hi-Hat",
    "x": 360,
    "y": 476,
    "volume": setVolume,
    "attack": setAttack,
    "decay": setDecay,
    "sustain": setSustain,
    "release": setRelease,
}

# Dictionnaire regroupant les paramètres de la cimbale 1
cymbal1Params = {
    "name": "Cymbale 1",
    "x": 438,
    "y": 374,
    "volume": setVolume,
    "attack": setAttack,
    "decay": setDecay,
    "sustain": setSustain,
    "release": setRelease,
}

# Dictionnaire regroupant les paramètres de la cimbale 2
cymbal2Params = {
    "name": "Cymbale 2",
    "x": 663,
    "y": 381,
    "volume": setVolume,
    "attack": setAttack,
    "decay": setDecay,
    "sustain": setSustain,
    "release": setRelease,
}

# Dictionnaire regroupant les paramètres de la cimbale 3
cymbal3Params = {
    "name": "Cymbale 3",
    "x": 383,
    "y": 414,
    "volume": setVolume,
    "attack": setAttack,
    "decay": setDecay,
    "sustain": setSustain,
    "release": setRelease,
}

# Dictionnaire regroupant les paramètres de la cimbale 4
cymbal4Params = {
    "name": "Cymbale 4",
    "x": 583,
    "y": 423,
    "volume": setVolume,
    "attack": setAttack,
    "decay": setDecay,
    "sustain": setSustain,
    "release": setRelease,
}

# Dictionnaire regroupant les paramètres de la cimbale 5
cymbal5Params = {
    "name": "Cymbale 5",
    "x": 717,
    "y": 457,
    "volume": setVolume,
    "attack": setAttack,
    "decay": setDecay,
    "sustain": setSustain,
    "release": setRelease,
}

# Liste regroupant les dictionnaires correspondant aux paramètres de chaque élément de la batterie
drumObject = [
    kickParams,
    snareParams,
    tom1Params,
    tom2Params,
    tom3Params,
    tom4Params,
    hihatParams,
    cymbal1Params,
    cymbal2Params,
    cymbal3Params,
    cymbal4Params,
    cymbal5Params,
]

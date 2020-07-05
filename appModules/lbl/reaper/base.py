import ui
import tones
import api
import controlTypes

def isFXWindow():
    """
    On vérifie que la fenêtre courante est la fenêtre d'effets
    """
    
    if api.getForegroundObject().name.startswith('FX:'):
        return True
    else:
        return False

def getSelectedFXName():
    """
        On récupère le nom de l'effet sélectionné
    """

    window = api.getForegroundObject()
    selectedFXName = ""
    i = 0
    j = 0
    
    if not isFXWindow():
        return ""

    while window.children[i]:
        if window.children[i].role == controlTypes.ROLE_LIST:
            fxChain = window.children[i]
            break
        i += 1

    while fxChain.children[j]:
        if controlTypes.STATE_SELECTED in fxChain.children[j].states:
            selectedFXName = fxChain.children[j].name
            break
        j += 1
    return selectedFXName

def getSmartName():
    """
        On retourne un nom intelligible pour l'effet courant, s'il est pris en charge par LBL
    """

    window = api.getForegroundObject()
    fxName = getSelectedFXName()

    if fxName.startswith("VSTi: SSDSampler5"):
        return "Steeven Slate Drummer 5"
    elif fxName.startswith("VSTi: DSK Saxophones"):
        return "DSK Saxophones"
    return

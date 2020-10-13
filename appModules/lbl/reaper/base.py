import ui
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
        On vérifie que le plugin est pris en charge par LBL, et si tel est le cas, on retourne son nom de manière intelligible
    """

    window = api.getForegroundObject()
    fxName = getSelectedFXName()

    if "SSDSampler" in fxName:
        return "Steeven Slate Drum 5"
    elif "DSK Saxophones" in fxName:
        return "DSK Saxophones"
    elif "EZdrummer" in fxName:
        return "EZ Drummer"
    elif "GTune" in fxName:
        return "GTune"
    elif "sforzando" in fxName:
        return "Sforzando"
    elif "Guitar Rig" in fxName:
        return "Guitar Rig"
    elif "Zampler" in fxName:
        return "Zampler"
    elif "VSCO2" in fxName:
        return "VSCO2"
    elif "Addictive Drums" in fxName:
        return "Addictive Drums"
    elif "Addictive Keys" in fxName:
        return "Addictive Keys"
    return

# Import des modules NVDA
import tones
import ui
import api
import keyboardHandler
import config
from NVDAObjects.IAccessible import IAccessible
from scriptHandler import script

# Import des modules LBL
from ..api.navobject import NavObject
from ..api.ocr import LBLOCR

class DSKSaxophones(IAccessible):
    name = "DSK Saxophone"

    @script(gesture="kb:NVDA+d")
    def script_doTest(self, gesture):
        ui.message("Bonjour saxophone")




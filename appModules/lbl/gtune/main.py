# Import des modules Python
import winUser
import time
import sys

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
from ..api.menu import Menu
from ..api.mouse import Mouse

# Import des module propres à GTune
from .itemlist import itemList

class GTune(IAccessible):
    name = "LBL_GTune"
    tones.beep(440, 150)
    itemlist = NavObject(itemList)
    mouse = Mouse()
    mode = "off"
    i = 0

    @script(gesture="kb:leftarrow")
    def script_previousItem(self, gesture):
        """
            Aller à l'objet précédent de l'interface
        """

        ui.message(self.itemlist.getPreviousObject()["name"])

        if self.itemlist.getObject()['name'] == 'Reference':
            ui.message(LBLOCR.getText([230, 35, 280, 50]))
        elif self.itemlist.getObject()['name'] == 'Tune':
            ui.message(LBLOCR.getText([160, 210, 280, 250]))

    @script(gesture="kb:rightarrow")
    def script_nextItem(self, gesture):
        """
            Aller à l'objet suivant de l'interface
        """
        ui.message(self.itemlist.getNextObject()["name"])

        if self.itemlist.getObject()['name'] == 'Reference':
            ui.message(LBLOCR.getText([230, 35, 280, 50]))
        elif self.itemlist.getObject()['name'] == 'Tune':
            ui.message(LBLOCR.getText([160, 210, 280, 250]))

    @script(gesture="kb:enter")
    def script_openEditZone(self, gesture):
        """
            Ouvertu're de la zone d'édition de changement de la fréquence de référence
        """
        
        self.mouse.moveAndLeftClick(240, 40)

    @script(gesture="kb:NVDA+d")
    def script_debug(self, gesture):
        """
            Fonction générique de debug
        """

        ui.message(LBLOCR.getText([230, 35, 280, 50]))


    

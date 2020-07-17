# Import des modules Python
import winUser
import time

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

# Import des modules propres à Steeven Slate Drummer 5
from .zonelist import zoneList
from .tablist import tabList
from .createcontent import createContent
from .drummodule import drumObject
from .mixermodule import mixerObject

class SteevenSlateDrummer(IAccessible):
    name = "Steeven Slate Drum 5"
    role = "LBL_WINDOW"
    zone = NavObject(zoneList)
    tab = NavObject(tabList)
    createContent = NavObject(createContent)
    drumObject = NavObject(drumObject, 3)
    mixerObject = NavObject(mixerObject, 0)
    # menu = Menu()
    mode = "default"

    @script(gesture="kb:tab")
    def script_goToNextZone(self, gesture):
        """
            Définition du comportement de la touche tab, selon la zone
        """

        if self.mode == "default":
            ui.message(self.zone.getNextObject())
       
    @script(gesture="kb:shift+tab")
    def script_goToPreviousZone(self, gesture):
        """
            Définition du comportement des touches shift+tab, selon la zone
        """

        if self.mode == "default":
            ui.message(self.zone.getPreviousObject())

    @script(gesture="kb:rightarrow")
    def script_goToNextItem(self, gesture):
        """
            Définition du comportement de la touche flèche droite, selon la zone
        """
        
        zone = self.zone.getObject()
        tab = self.tab.getObject()

        if zone == "Tabs":
            ui.message(self.tab.getNextObject(mouse = "move_and_click")["name"])
        elif zone == "Content":
            if tab["name"] == "Create":
                ui.message(self.createContent.getNextObject()["name"])
            elif tab["name"] == "Drum":
                if self.mode == "default":
                    ui.message(self.drumObject.getNextObject(mouse = "move_and_click")["name"])
                elif self.mode == "piece_settings":
                    ui.message(self.drumObject.getSubObject()[1]("right", self.drumObject.getObject()["x"], self.drumObject.getObject()["y"]))
            elif tab["name"] == "Mixer":
                if self.mode == "default":
                    ui.message(self.mixerObject.getNextObject(mouse = "move_and_click")["name"])

    @script(gesture="kb:leftarrow")
    def script_goToPreviousItem(self, gesture):
        """
            Définition du comportement de la touche flèche gauche, selon la zone
        """

        zone = self.zone.getObject()
        tab = self.tab.getObject()

        if zone == "Tabs":
            ui.message(self.tab.getPreviousObject(mouse = "move_and_click")["name"])
        elif zone == "Content":
            if tab["name"] == "Create":
                ui.message(self.createContent.getPreviousObject()["name"])
            elif tab["name"] == "Drum":
                if self.mode == "default":
                    ui.message(self.drumObject.getPreviousObject(mouse = "move_and_click")["name"])
                elif self.mode == "piece_settings":
                    ui.message(self.drumObject.getSubObject()[1]("left", self.drumObject.getObject()["x"], self.drumObject.getObject()["y"]))
            elif tab["name"] == "Mixer":
                if self.mode == "default":
                    ui.message(self.mixerObject.getPreviousObject(mouse = "move_and_click")["name"])

    @script(gesture="kb:uparrow")
    def script_goToUpItem(self, gesture):
        """
            Définition du comportement de la touche flèche haut, selon la zone
        """

        zone = self.zone.getObject()
        tab = self.tab.getObject()
        drumObject = self.drumObject.getObject()
        obj = self.mixerObject.getObject()

        if zone == "Content":
            if tab["name"] == "Drum":
                if self.mode == "piece_settings":
                    ui.message(self.drumObject.getPreviousSubObject()[0])
            elif tab["name"] == "Mixer":
                if self.mode == "menu":
                    ui.message(obj["routing"]("up", menuSize = obj["menuSize"]))
                    keyboardHandler.KeyboardInputGesture.fromName("uparrow").send()

    @script(gesture="kb:downarrow")
    def script_goToDownItem(self, gesture):
        """
            Définition du comportement de la touche flèche bas, selon la zone
        """

        zone = self.zone.getObject()
        tab = self.tab.getObject()
        drumObject = self.drumObject.getObject()
        obj = self.mixerObject.getObject()

        if zone == "Content":
            if tab["name"] == "Drum":
                if self.mode == "default":
                    self.mode = "piece_settings"
                    ui.message(self.drumObject.getObject()["name"] + "Configuration, " + self.drumObject.getSubObject()[0])
                elif self.mode == "piece_settings":
                    ui.message(self.drumObject.getNextSubObject()[0])
            elif tab["name"] == "Mixer":
                if self.mode == "menu":
                    ui.message(obj["routing"]("down", menuSize = obj["menuSize"]))
                    keyboardHandler.KeyboardInputGesture.fromName("downarrow").send()

    @script(gesture="kb:shift+uparrow")
    def script_volumeUp(self, gesture):
        zone = self.zone.getObject()
        tab = self.tab.getObject()
        obj = self.mixerObject.getObject()

        if zone == "Content":
            if tab["name"] == "Mixer":
                obj["volume"]("up", obj["volumeX"], obj["volumeY"], obj["x"], obj["y"])

    @script(gesture="kb:shift+downarrow")
    def script_volumeDown(self, gesture):
        zone = self.zone.getObject()
        tab = self.tab.getObject()
        obj = self.mixerObject.getObject()
        
        if zone == "Content":
            if tab["name"] == "Mixer":
                obj["volume"]("down", obj["volumeX"], obj["volumeY"], obj["x"], obj["y"])

    @script(gesture="kb:shift+leftarrow")
    def script_panoramicLeft(self, gesture):
        zone = self.zone.getObject()
        tab = self.tab.getObject()
        obj = self.mixerObject.getObject()

        if zone == "Content":
            if tab["name"] == "Mixer":
                obj["panoramic"]("left", obj["panoramicX"], obj["panoramicY"], obj["x"], obj["y"])

    @script(gesture="kb:shift+rightarrow")
    def script_panoramicRight(self, gesture):
        zone = self.zone.getObject()
        tab = self.tab.getObject()
        obj = self.mixerObject.getObject()

        if zone == "Content":
            if tab["name"] == "Mixer":
                obj["panoramic"]("right", obj["panoramicX"], obj["panoramicY"], obj["x"], obj["y"])

    @script(gesture="kb:m")
    def script_changeState(self, gesture):
        zone = self.zone.getObject()
        tab = self.tab.getObject()
        obj = self.mixerObject.getObject()

        if zone == "Content":
            if tab["name"] == "Mixer":
                ui.message(obj["state"]())

    @script(gesture="kb:enter")
    def script_getTab(self, gesture):
        """
            Définition du comportement de la touche entrée
        """

        zone = self.zone.getObject()
        tab = self.tab.getObject()
        obj = self.mixerObject.getObject()

        if zone == "Content":
            if tab["name"] == "Drum":
                if self.mode == "default":
                    self.drumObject.getObject(mouse = "move_and_click")["name"]
                elif self.mode == "piece_settings":
                    ui.message(self.drumObject.getObject()["name"] + " configuration saved")
                    self.mode = "default"
            elif tab["name"] == "Mixer":
                if self.mode == "default":
                    self.mixerObject.getObject(mouse = "move_and_click")["name"]
                elif self.mode == "menu":
                    ui.message("Routing saved")
                    keyboardHandler.KeyboardInputGesture.fromName("enter").send()
                    self.mode = "default"
  
    @script(gesture="kb:escape")
    def script_closeFxWindow(self, gesture):
        """
            Définition du comportement de la touche Echape
        """

        if self.mode == "default":
            self.zone.resetObject()
            self.tab.resetObject()
            self.createContent.resetObject()
            self.drumObject.resetObject()
            self.mixerObject.resetObject()
            config.conf["mouse"]["enableMouseTracking"] = True
            keyboardHandler.KeyboardInputGesture.fromName("escape").send()
        elif self.mode == "piece_settings":
            self.drumObject.paramsPosition = self.drumObject.defaultParamsPosition
            ui.message(self.drumObject.getObject()["name"] + " configuration saved")
            self.mode = "default"
        elif self.mode == "menu":
            ui.message("Cancel")
            keyboardHandler.KeyboardInputGesture.fromName("escape").send()
            self.mode = "default"

    @script(gesture="kb:h")
    def script_getHelp(self, gesture):
        zone = self.zone.getObject()

        if zone == "Tabs":
            ui.message("Vous êtes dans la zone contenant la liste des onglets.")
        elif zone == "Content":
            ui.message("Vous êtes dans la zone de contenu")

    @script(gesture="kb:NVDA+d")
    def script_getColor(self, gesture):
        color = LBLOCR.getColor([154, 222, 156, 224])

        if color == '#59caf5':
            ui.message("Non muté")
        elif color == '#143650':
            ui.message("Muté")

    @script(gesture="kb:applications")
    def script_applicationMenu(self, gesture):
        tab = self.tab.getObject()
        zone = self.zone.getObject()
        obj = self.mixerObject.getObject()

        if zone == "Content":
            if tab["name"] == "Mixer":
                if self.mode == "default":
                    self.mode = "menu"
                    ui.message(obj["routing"]("enter", obj["routingButtonX"], obj["routingButtonY"], obj["routingDiagonal"], obj["menuSize"]))
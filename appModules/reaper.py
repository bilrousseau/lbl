import appModuleHandler
import ui
import tones
import api
from scriptHandler import script

from .lbl.reaper import base, label
from .lbl.reaper.overlay import LBLCheckBox
from .lbl.steevenslatedrummer5.main import SteevenSlateDrummer
from .lbl.dsksaxophones.main import DSKSaxophones

# Import des modules Sibiac
from .sibiac.ezdrummer import EZDrummer
from .sibiac.gtune import GTune
from .sibiac.sforzando import Sforzando

class AppModule(appModuleHandler.AppModule):
    tones.beep(440, 150)

    @script(gesture="kb:NVDA+a")
    def script_searchSelectedFX(self, gesture):
        ui.message(base.getSelectedFXName())

    @script(gesture="kb:NVDA+e")
    def script_searchPluginZone(self, gesture):
        ui.message(base.getSmartName())

    def event_gainFocus(self, obj, nextHandler):
        label.setLabels(obj)
        nextHandler()

    def chooseNVDAObjectOverlayClasses(self, obj, clsList):
        if obj.windowControlID == 1426:
            clsList.insert(0, LBLCheckBox)
        elif obj.windowClassName.startswith("JUCE") and base.getSelectedFXName().startswith("VSTi: SSDSampler"):
            clsList.insert(0, SteevenSlateDrummer)
        elif obj.windowClassName.startswith("JUCE") and base.getSelectedFXName().startswith("VSTi: DSK Saxophones"):
            clsList.insert(0, DSKSaxophones)
        elif obj.windowClassName.startswith("Plugin") and base.getSelectedFXName().startswith("VSTi: EZdrummer"):
            clsList.insert(0, EZDrummer)
        elif obj.windowClassName.startswith("GWin") and base.getSelectedFXName().startswith("VST: GTune"):
            clsList.insert(0, GTune)
        elif obj.windowClassName.startswith("Plugin") and base.getSelectedFXName().startswith("VST3i: sforzando"):
            clsList.insert(0, Sforzando)



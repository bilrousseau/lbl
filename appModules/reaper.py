import appModuleHandler
import ui
import api
from scriptHandler import script

from .lbl.reaper import base, label
from .lbl.reaper.overlay import LBLCheckBox
from .lbl.steevenslatedrummer5.main import SteevenSlateDrummer
from .lbl.dsksaxophones.main import DSKSaxophones

# Import des modules Sibiac
from NVDAObjects.window import Window
from NVDAObjects.IAccessible import IAccessible
import speech
from logHandler import log
import eventHandler
import time
import queueHandler
import core
import oleacc
import controlTypes
import winUser
import api
import ctypes

from . import sibiac
from .sibiac import MoveFocusTo, SIBI, SIBINVDA, XY, Box, TextBox, TextOutBox, ScrollV, Color2Tuple, ColorMatcherObj, ColorMatcher, FindInXRight, FindInYDown, FindRow, FindVRange, FindHRange, chooseKnownOverlay, MouseSlowLeftClick, MouseScroll, FindNearestColor, Control, VList, YRange, YBar, Container, Label, ScrollLabel, PopupLabel, PushBtn, SwitchBtn, FixedTab, FixedTabControl, Combo, Dialog, OpenBtn, PopupMenuButton, Clickable, OptionTable, Pt, FIXED, MOVE, PROPORTIONAL, gSIBI
from .sibiac import SpinLabel
from .sibiac.ezdrummer import EZDrummer
from .sibiac.gtune import GTune
from .sibiac.sforzando import Sforzando
from .sibiac.ni import GuitarRig5
from .sibiac.xln import AD2, AK
from .sibiac.zampler import Zampler

class AppModule(appModuleHandler.AppModule):
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
        elif obj.windowClassName.startswith('NIVSTChildWindow') and base.getSelectedFXName().startswith("VST: Guitar Rig"):
            clsList.insert(0, GuitarRig5)
        elif obj.windowClassName.startswith('Plugin00007FFC65EF0000') and base.getSelectedFXName().startswith("VSTi: Zampler"):
            clsList.insert(0, Zampler)
        








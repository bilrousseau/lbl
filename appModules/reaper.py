import appModuleHandler
import ui
import api
from scriptHandler import script

from .lbl.reaper import base, label
from .lbl.reaper.overlay import LBLCheckBox
from .lbl.steevenslatedrummer5.main import SteevenSlateDrummer
from .lbl.dsksaxophones.main import DSKSaxophones
from .lbl.gtune.main import GTune

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
from .sibiac.sforzando import Sforzando
from .sibiac.ni import GuitarRig5
from .sibiac.xln import AD2, AK
from .sibiac.zampler import Zampler
from .sibiac.vsco2 import VSCO2

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
        elif obj.windowClassName.startswith("JUCE") and "SSDSampler" in base.getSelectedFXName():
            clsList.insert(0, SteevenSlateDrummer)
        elif obj.windowClassName.startswith("JUCE") and "DSK Saxophones" in base.getSelectedFXName():
            clsList.insert(0, DSKSaxophones)
        elif obj.windowClassName.startswith("Plugin") and "EZdrummer" in base.getSelectedFXName():
            clsList.insert(0, EZDrummer)
        elif obj.windowClassName.startswith("GWin") and "GTune" in base.getSelectedFXName():
            clsList.insert(0, GTune)
        elif obj.windowClassName.startswith("Plugin") and "sforzando" in base.getSelectedFXName():
            clsList.insert(0, Sforzando)
        elif obj.windowClassName.startswith('NIVSTChildWindow') and "Guitar Rig" in base.getSelectedFXName():
            clsList.insert(0, GuitarRig5)
        elif obj.windowClassName.startswith('Plugin') and "Zampler" in base.getSelectedFXName():
            clsList.insert(0, Zampler)
        elif obj.windowClassName.startswith('JUCE') and "VSCO2" in base.getSelectedFXName():
            clsList.insert(0, VSCO2)
        elif obj.windowClassName.startswith('JUCE') and "Addictive Drums" in base.getSelectedFXName():
            clsList.insert(0, AD2)
        elif obj.windowClassName.startswith('JUCE') and "Addictive Keys" in base.getSelectedFXName():
            clsList.insert(0, AK)

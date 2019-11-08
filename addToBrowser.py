from anki.hooks import addHook
from aqt.qt import *


def addToBrowser(fun, text, shortcut=None):
    """fun -- function taking as argument: the browser
    text -- what to enter in the menu
    shortcut
    """
    def aux(browser):
        action = browser.form.menuEdit.addAction(text)
        action.triggered.connect(lambda: fun(browser))
        if shortcut:
            action.setShortcut(QKeySequence(shortcut))
        addHook("browser.setupMenus", aux)

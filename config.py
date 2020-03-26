import sys

from aqt import mw
from aqt.utils import showWarning

# to be configured by Dev
############################
addonName =
version =


def newVersion():


"""A string stating what could occurs with a wrong configuration file"""
otherwise = ""


# end configuration

userOption = None


def _getUserOption():
    global userOption
    if userOption is None:
        userOption = mw.addonManager.getConfig(__name__)


def getUserOption(keys=None, default=None, set_to_default_if_missing=True):
    """Get the user option if it is set. Otherwise return the default
    value and add it to the config.

    When an add-on was updated, new config keys were not added. This
    was a problem because user never discover those configs. By adding
    it to the config file, users will see the option and can configure it.

    If keys is a list of string [key1, key2, ... keyn], it means that
    config[key1], ..., config[key1]..[key n-1] are dicts and we want
    to get config[key1]..[keyn]

    """
    _getUserOption()
    if keys is None:
        return userOption
    if isinstance(keys, str):
        keys = [keys]

    # Path in the list of dict
    current = userOption
    for key in keys[:-1]:
        assert isinstance(current, dict)
        if key not in current:
            current[key] = dict()
        current = current[key]

    # last element
    key = keys[-1]
    if key not in userOption:
        return userOption[key]
    else:
        if set_to_default_if_missing:
            userOption[key] = default
            writeConfig()
        return default


def writeConfig():
    mw.addonManager.writeConfig(__name__, userOption)


lastVersion = getUserOption(version, 0)
if lastVersion < version:
    newVersion()
    pass
if lastVersion > version:
    t = f"Please update add-on {addonName}. It seems that your configuration file is made for a more recent version of the add-on."
    if otherwise:
        t += "\n" + otherwise
    showWarning(t)


def update(_):
    global userOption, fromName
    userOption = None
    fromName = None


mw.addonManager.setConfigUpdatedAction(__name__, update)

fromName = None


def getFromName(name):
    global fromName
    if fromName is None:
        fromName = dict()
        for dic in getUserOption("columns"):
            fromName[dic["name"]] = dic
    return fromName.get(name)


def setUserOption(key, value):
    _getUserOption()
    userOption[key] = value
    writeConfig()

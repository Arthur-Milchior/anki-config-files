from anki.hooks import addHook


def addActionToGear(fun, text):
    """fun -- takes an argument, the did
    text -- what's written in the gear."""
    def aux(m, did):
        a = m.addAction(text)
        a.triggered.connect(lambda b, did=did: fun(did))
    addHook("showDeckOptions", aux)

from aqt.hooks_gen import deck_browser_will_show_options_menu



def addActionToGear(fun, text):
    """ Add an entry to deck gear, in deck browser, with text calling function.

    fun -- takes an argument, the did
    text -- what's written in the gear."""
    def aux(m, did):
        """Call the function added to the gear by addActionToGear.

        m -- the menu entry
        did -- the deck whose gear is clicked."""
        a = m.addAction(text)
        a.triggered.connect(lambda b, did=did: fun(did))
    deck_browser_will_show_options_menu.append(aux)

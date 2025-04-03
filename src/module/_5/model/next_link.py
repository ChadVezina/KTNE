from tkinter import Frame
from .etape import Etape

class NextLink:
    def __init__(
        self,
        ):
        self.table_ecran = {
            0: ["ur"],
            1: ["first", "okay", "c"],
            2: ["yes", "nothing", "led", "they are"],
            3: ["blank", "read", "red", "you", "your", "you're", "their"],
            4: ["", "reed", "leed", "they're"],
            5: ["display", "says", "no", "lead", "hold on", "you are", "there", "see", "cee"],
        }
        self.table_libelle = {
            "ready": ["yes", "okay", "what", "middle", "left", "press", "right", "blank", "ready", "no", "first", "uhhh", "nothing", "wait"],
            "first": ["left", "okay", "yes", "middle", "no", "right", "nothing", "uhhh", "wait", "ready", "blank", "what", "press", "first"],
            "no": ["blank", "uhhh", "wait", "first", "what", "ready", "right", "yes", "nothing", "left", "press", "okay", "no", "middle"],
            "blank": ["wait", "right", "okay", "middle", "blank", "press", "ready", "nothing", "no", "what", "left", "uhhh", "yes", "first"],
            "nothing": ["uhhh", "right", "okay", "middle", "yes", "blank", "no", "press", "left", "what", "wait", "first", "nothing", "ready"],
            "yes": ["okay", "right", "uhhh", "middle", "first", "what", "press", "ready", "nothing", "yes", "left", "blank", "no", "wait"],
            "what": ["uhhh", "what", "left", "nothing", "ready", "blank", "middle", "no", "okay", "first", "wait", "yes", "press", "right"],
            "uhhh": ["ready", "nothing", "left", "what", "okay", "yes", "right", "no", "press", "blank", "uhhh", "middle", "wait", "first"],
            "left": ["right", "left", "first", "no", "middle", "yes", "blank", "what", "uhhh", "wait", "press", "ready", "okay", "nothing"],
            "right": ["yes", "nothing", "ready", "press", "no", "wait", "what", "right", "middle", "left", "uhhh", "blank", "okay", "first"],
            "middle": ["blank", "ready", "okay", "what", "nothing", "press", "no", "wait", "left", "middle", "right", "first", "uhhh", "yes"],
            "okay": ["middle", "no", "first", "yes", "uhhh", "nothing", "wait", "okay", "left", "ready", "blank", "press", "what", "right"],
            "wait": ["uhhh", "no", "blank", "okay", "yes", "left", "first", "press", "what", "wait", "nothing", "ready", "right", "middle"],
            "press": ["right", "middle", "yes", "ready", "press", "okay", "nothing", "uhhh", "blank", "left", "first", "what", "no", "wait"],
            "you": ["sure", "you are", "your", "you're", "next", "uh huh", "ur", "hold", "what?", "you", "uh uh", "like", "done", "u"],
            "you are": ["your", "next", "like", "uh huh", "what?", "done", "uh uh", "hold", "you", "u", "you're", "sure", "ur", "you are"],
            "your": ["uh uh", "you are", "uh huh", "your", "next", "ur", "sure", "u", "you're", "you", "what?", "hold", "like", "done"],
            "you're": ["you", "you're", "ur", "next", "uh uh", "you are", "your", "what?", "uh huh", "sure", "done", "like", "hold"],
            "ur": ["done", "u", "ur", "uh huh", "what?", "sure", "your", "hold", "you're", "like", "next", "uh uh", "you are", "you"],
            "u": ["uh huh", "sure", "next", "what?", "you're", "hold", "uh uh", "done", "u", "you", "like", "you are", "your"],
            "uh huh": ["uh huh", "your", "you are", "you", "done", "hold", "uh uh", "next", "sure", "like", "you're", "ur", "u", "what?"],
            "uh uh": ["ur", "u", "you are", "you're", "next", "uh uh", "done", "you", "uh huh", "like", "your", "sure", "hold", "what?"],
            "what?": ["you", "hold", "you're", "your", "u", "done", "uh uh", "like", "you are", "uh huh", "ur", "next", "what?", "sure"],
            "done": ["sure", "uh huh", "next", "what?", "your", "ur", "you're", "hold", "like", "you", "u", "you are", "uh uh", "done"],
            "next": ["what?", "uh huh", "uh uh", "your", "hold", "sure", "next", "like", "done", "you are", "ur", "you're", "u", "you"],
            "hold": ["you are", "u", "done", "uh uh", "you", "ur", "sure", "what?", "you're", "next", "hold", "uh huh", "your", "like"],
            "sure": ["you are", "done", "like", "you're", "you", "hold", "uh huh", "ur", "sure", "u", "what?", "next", "your", "uh uh"],
            "like": ["you're", "next", "u", "ur", "hold", "done", "uh uh", "what?", "uh huh", "you", "like", "sure", "you are", "your"],
        }
        self.textes = sorted([texte for value in self.table_ecran.values() for texte in value], key=lambda texte: texte)
        self.options = sorted([texte for texte in self.table_libelle.keys()], key=lambda texte: texte)
        self.etape: Etape | None = None

    def do(self, parent: Frame, row: int):
        self.destroy()
        self.parent = parent
        self.row = row
        self.etape = Etape(parent, row, self.textes, self.options, lambda: self.clic())

    def destroy(self):
        if(self.etape is not None):
            self.etape.destroy()
            self.etape = None
            self.parent = None
            self.row = None

    def desactiver(self):
        active_option = self.etape.options.get_active_option()
        if(active_option != -1):
            self.etape.options.desactiver(active_option)

    def scan_texte(self, texte: str):
        for scan, values in self.table_ecran.items():
            if(texte in values):
                self.etape.texte.is_exist()
                return scan
        self.etape.texte.is_not_exist()
        for scan in range(6):
            self.etape.options.is_not_exist(scan)
        self.desactiver()
        return None

    def scan_options(self, options: list[str], libelle_values: list[str] | None):
        if(libelle_values is None):
            for scan, _ in enumerate(options):
                self.etape.options.is_not_exist(scan)
        else:
            for scan, option in enumerate(options):
                if(option in libelle_values):
                    self.etape.options.is_exist(scan)
                else:
                    self.etape.options.is_not_exist(scan)
            for option in options:
                if(not option in libelle_values):
                    self.desactiver()
                    return
            for libelle_value in libelle_values:
                if(libelle_value in options):
                    self.etape.options.activer(options.index(libelle_value))
                    return
            self.desactiver()

    def clic(self):
        if(self.etape is not None):
            texte = self.etape.texte.get_texte()
            options = self.etape.options.get_options()
            scan = self.scan_texte(texte)
            if(scan is not None):
                self.scan_options(options, self.table_libelle.get(options[scan], None))

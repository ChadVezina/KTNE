from module._1.main import Module_1
from module._2.main import Module_2
from module._3.main import Module_3
from module._4.main import Module_4
from module._5.main import Module_5
from module._6.main import Module_6
from module._7.main import Module_7
from module._8.main import Module_8
from module._9.main import Module_9
from module._10.main import Module_10
from module._11.main import Module_11
from constants.fenetre import N_MODULES
from tools.functions import calculateSize
from tools.module import Module


def getModule(numero: int, fenetre, geometry: str) -> Module | None:
    match numero:
        case 2:
            return Module_2(fenetre, geometry)
        case 3:
            return Module_3(fenetre, geometry)
        case 4:
            return Module_4(fenetre, geometry)
        case 5:
            return Module_5(fenetre, geometry)
        case 6:
            return Module_6(fenetre, geometry)
        case 7:
            return Module_7(fenetre, geometry)
        case 8:
            return Module_8(fenetre, geometry)
        case 9:
            return Module_9(fenetre, geometry)
        case 10:
            return Module_10(fenetre, geometry)
        case 11:
            return Module_11(fenetre, geometry)
        case _:
            pass


fenetre = Module_1()
geometries = calculateSize(fenetre, N_MODULES)
fenetre.geometry(geometries.pop(0))
modules: list[Module] = []
is_update = False
is_show = True

def get_module(i: int) -> Module | None:
    if i in range(len(modules)):
        return modules[i]

def hide(self: Module | None):
    if self is None:
        return
    if self.winfo_exists():
        if isinstance(self, Module_1):
            self.iconify()
        else:
            self.withdraw()

def show(self: Module | None):
    if self is None:
        return
    if self.winfo_exists():
        self.deiconify()

def state_hide(self: Module | None) -> bool:
    if self is None:
        return False
    self.enter()
    if self.wm_state() != "iconic":
        return True
    return False

def state_show(self: Module | None) -> bool:
    if self is None:
        return False
    self.enter()
    if self.wm_state() == "iconic":
        return True
    return False

def hides(i: int):
    if state_hide(get_module(i)):
        return
    global is_show
    if is_show:
        global is_update
        if is_update:
            return
        is_update = True
        for scan, module in enumerate(modules):
            if scan != i:
                hide(module)
        is_update = False
        is_show = False
        if not isinstance(get_module(i), Module_1):
            get_module(i).withdraw()

def shows(i: int):
    if state_show(get_module(i)):
        return
    global is_show
    if not is_show:
        global is_update
        if is_update:
            return
        is_update = True
        for scan, module in enumerate(modules):
            if scan != i:
                show(module)
        is_update = False
        is_show = True

modules.append(fenetre)
for scan in range(1, N_MODULES):
    modules_i = getModule(scan+1, fenetre, geometries.pop(0))
    if modules_i is not None:
        modules.append(modules_i)
        module = get_module(scan)
        if module is not None:
            module.bind("<Map>", lambda e, scan=scan: shows(scan))
            module.bind("<Unmap>", lambda e, scan=scan: hides(scan))

fenetre.bind("<Map>", lambda e: shows(0))
fenetre.bind("<Unmap>", lambda e: hides(0))

fenetre.mainloop()

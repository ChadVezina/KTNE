from tkinter import Tk, Event, messagebox, Frame, Canvas, BOTH, LEFT, TOP

from tools.functions import make_menu


class Root(Tk):
    def __init__(self):
        super().__init__()
        min_width = 800
        min_height = 1000

        self.geometry(f"{min_width}x{min_height}+0+0")
        self.minsize(width=min_width, height=min_height)
        self.title("Keep Talking and Nobody Explodes")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.init()
        make_menu(self, self.nouvelle_partie, self.quitter)

    def init(self) -> None:
        container = Frame(self)
        container.pack(fill = BOTH, expand = True)
        self.canvas = Canvas(container, bd = 0, highlightthickness = 0)

        self.outer_frame = Frame(self.canvas)
        self.cadre = Frame(self.outer_frame)
        self.cadre.pack(side = TOP)

        self.canvas.create_window((0, 0), window = self.outer_frame, anchor = "n", tags = "frame")
        self.canvas.pack(side = LEFT, fill = BOTH, expand = True)

        self.outer_frame.bind("<Configure>", self.update_scroll)
        self.canvas.bind("<Configure>", self.center_content)
        self.cadre.bind("<Configure>", self.on_inner_frame_change)

        self.scroll_active = False

        self.bind("<Enter>", lambda e: self.bind_mouse_scroll())
        self.bind("<Button-2>", lambda e: self.redessiner())
        self.bind("<Button-3>", lambda e: self.clic())

    def clic(self) -> None:
        if self.state() == "zoomed":
            self.state("normal")
        else:
            self.state("zoomed")

    def enter(self) -> None:
        self.on_inner_frame_change()

    def on_inner_frame_change(self, event = None) -> None:
        self.outer_frame.event_generate("<Configure>")
        self.canvas.event_generate("<Configure>")

    def center_content(self, event = None) -> None:
        canvas_width = self.canvas.winfo_width()
        self.canvas.itemconfig("frame", width = canvas_width)

    def update_scroll(self, event = None) -> None:
        self.canvas.configure(scrollregion = self.canvas.bbox("all"))

        content_height = self.outer_frame.winfo_height()
        canvas_height = self.canvas.winfo_height()

        if content_height > canvas_height:
            if not self.scroll_active:
                self.scroll_active = True
                self.bind_mouse_scroll()
        else:
            if self.scroll_active:
                self.scroll_active = False
                self.bind_mouse_scroll()

    def bind_mouse_scroll(self) -> None:
        if self.scroll_active:
            self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)
        else:
            self.canvas.unbind_all("<MouseWheel>")

    def on_mousewheel(self, event: Event) -> None:
        if self.scroll_active:
            self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def ouvrir_partie(self) -> None:
        self.redessiner()

    def nouvelle_partie(self) -> None:
        self.ouvrir_partie()

    def quitter(self) -> None:
        if messagebox.askyesno("Quitter", "Êtes-vous sûr de vouloir quitter?"):
            self.quit()


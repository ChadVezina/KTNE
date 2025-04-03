MULTI_PAD = 1
MULTI_SIZE = 1

MULTI_HINT_CASE = 2
TAILLE_HINT_CASE = 9

class FenetrePad:
    PADDING_X = 10 * MULTI_PAD
    PADDING_Y = 10 * MULTI_PAD


class GridPad:
    PADDING_X = 5 * MULTI_PAD
    PADDING_Y = 10 * MULTI_PAD


class TextPad:
    PADDING_X = 10 * MULTI_PAD
    PADDING_Y = 10 * MULTI_PAD


class ButtonPad:
    PADDING_X = 0 * MULTI_PAD
    PADDING_Y = 10 * MULTI_PAD


class EntrySize:
    WIDTH = 25 * MULTI_SIZE


class BoutonCaseRect:
    WIDTH = 4 * MULTI_SIZE
    HEIGHT = 1 * MULTI_SIZE
    PADDING_X = 1 * MULTI_PAD
    PADDING_Y = 3 * MULTI_PAD
    WRAP_LENGTH = 100 * MULTI_PAD


class HintCaseWidth:
    WIDTH = (BoutonCaseRect.WIDTH+BoutonCaseRect.PADDING_X*2)*MULTI_HINT_CASE


class HintCaseRect:
    WIDTH = HintCaseWidth.WIDTH
    WRAP_LENGTH = HintCaseWidth.WIDTH * TAILLE_HINT_CASE


class Font:
    BODY_SYMBOLE = ('Times New Roman', 32)
    BODY = ('Times New Roman', 16)
    BODY_HINT = ('Times New Roman', 12)


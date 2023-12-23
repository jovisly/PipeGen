PIPE_CHARS = ["═", "║", "╗", "╝", "╔", "╚", "╬", " "]

SET_R_CON = {"═", "╬", "╗", "╝"}
SET_R_END = {" ", "║", "╔", "╚"}
SET_L_CON = {"═", "╬", "╔", "╚"}
SET_L_END = {" ", "║", "╗", "╝"}
SET_U_CON = {"║", "╬", "╗", "╔"}
SET_U_END = {" ", "═", "╝", "╚"}
SET_D_CON = {"║", "╬", "╝", "╚"}
SET_D_END = {" ", "═", "╗", "╔"}

ALLOWED_CONFIG = {
    "═": {
        "u": SET_U_END,
        "d": SET_D_END,
        "l": SET_L_CON,
        "r": SET_R_CON,
    },
    "║": {
        "u": SET_U_CON,
        "d": SET_D_CON,
        "l": SET_L_END,
        "r": SET_R_END,
    },
    "╗": {
        "u": SET_U_END,
        "d": SET_D_CON,
        "l": SET_L_CON,
        "r": SET_R_END,
    },
    "╝": {
        "u": SET_U_CON,
        "d": SET_D_END,
        "l": SET_L_CON,
        "r": SET_R_END,
    },
    "╔": {
        "u": SET_U_END,
        "d": SET_D_CON,
        "l": SET_L_END,
        "r": SET_R_CON,
    },
    "╚": {
        "u": SET_U_CON,
        "d": SET_D_END,
        "l": SET_L_END,
        "r": SET_R_CON,
    },
    "╬": {
        "u": SET_U_CON,
        "d": SET_D_CON,
        "l": SET_L_CON,
        "r": SET_R_CON,
    },
    " ": {
        "u": SET_U_END,
        "d": SET_D_END,
        "l": SET_L_END,
        "r": SET_R_END,
    },
}


PIPE_CHARS_WEIGHTS = {
    "═": 4,
    "║": 4,
    "╗": 4,
    "╝": 4,
    "╔": 4,
    "╚": 4,
    "╬": 3,
    " ": 8,
}

import Defs.ThemeManager.theme as theme
default_palette = theme.default_palette

hidden_eye_logo = """
 {1} ██   ██ ██ ██████   ██████   ███████ ███   ██  {2}███████ ██    ██ ███████ {0}
 {1} ██   ██ ██ ██    ██ ██    ██ ██      ████  ██  {2}██       ██  ██  ██      {0}
 {1} ███████ ██ ██    ██ ██    ██ ███████ ██ ██ ██  {2}███████   ████   ███████ {0}
 {1} ██   ██ ██ ██    ██ ██    ██ ██      ██  ████  {2}██         ██    ██      {0}
 {1} ██   ██ ██ ██████   ██████   ███████ ██   ███  {2}███████    ██    ███████ {0}""".format(default_palette[4], default_palette[2], default_palette[0])

input_line = "\n{0}HiddenEye >>>  {1}".format(default_palette[0], default_palette[2])
from lang import LANG
from enums import ENUMS

from config.gui import GUIConfig
from config.cmd import CMDConfig
from config.lang import LANGConfig

CONFIG = {
  "CMD": CMDConfig,
  "GUI": GUIConfig,
  "lang": LANG[LANGConfig["default"]] if LANGConfig["default"] in LANG else LANG["en"],
  "output": ENUMS["ui_type"].CONSOLE # You can change this to ENUMS["ui_type"].CONSOLE or ENUMS["ui_type"].GUI
}

from lang import LANG
from enums import ENUMS

from config.gui import GUIConfig
from config.cmd import CMDConfig
from config.lang import LANGConfig

CONFIG = {
  "CMD": CMDConfig,
  "GUI": GUIConfig,
  "lang": LANG[LANGConfig["default"]] if LANGConfig["default"] in LANG else LANG["en"],
  "output": ENUMS["ui_type"].GUI # You can change this to ENUMS["ui_type"].CONSOLE or ENUMS["ui_type"].GUI
}

def update_config(config):
  """
  Updates the configuration
  :param config: Dictionary
  :return: None
  """
  for key, value in config.items():
    if key in CONFIG:
      if isinstance(value, dict) and isinstance(CONFIG[key], dict):
        update_config(value)
      else:
        CONFIG[key] = value

def change_lang(lang):
  """
  Changes the language
  :param lang: String
  :return: None
  """
  CONFIG["lang"] = LANG[lang] if lang in LANG else LANG["en"]

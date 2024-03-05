from handler.converter import Base

class Main:
  def __init__(self):
    """
    Base constructor
    :return: None
    """

    self.__override()

  def __override(self):
    """
    Override the base constructor
    :return: None
    """

    # Make sure you update logic in converter handler
    # bB default we only support override lang config
    config = {
      "lang": {
        "default": "en"
      }
    }

    Base(config)

if __name__ == "__main__": Main()
else: print("This is a module, not a standalone script.")

from src import App
from src import core
from src.database import Database
import sys

if __name__ == "__main__":
    application = App(sys.argv)
    sys.exit(application.run())

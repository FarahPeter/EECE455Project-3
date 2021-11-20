from FrontToBackConnector import FrontToBackConnector
from GUI import GUI
import threading

gui = []
guiThread = threading.Thread(target=GUI, args=(gui,))
guiThread.start()
gui = gui[0]

connector = []
connectorThread = threading.Thread(target=FrontToBackConnector, args=(connector,))
connectorThread.start()
connector = connector[0]

gui.myConnector = connector
connector.myGUI = gui

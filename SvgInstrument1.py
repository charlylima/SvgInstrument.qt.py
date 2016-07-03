import sys
import time
from PyQt4 import QtGui, QtSvg, QtCore
from PyQt4.QtCore import pyqtSignal
#from PyQt4.QtCore import QObject, pyqtSlot

def updateInstrument():
  itemz.rotate(6)

app = QtGui.QApplication(sys.argv) 

scene = QtGui.QGraphicsScene()
view = QtGui.QGraphicsView()
view.setScene(scene)

renderer = QtSvg.QSvgRenderer('instrument.svg')

itembg = QtSvg.QGraphicsSvgItem()
itembg.setSharedRenderer(renderer)
itembg.setElementId("background")
scene.addItem(itembg)
itembg.setFlags(QtGui.QGraphicsItem.ItemClipsChildrenToShape | QtGui.QGraphicsItem.ItemClipsToShape)

itemz = QtSvg.QGraphicsSvgItem()
itemz.setSharedRenderer(renderer)
itemz.setElementId("zeiger")
scene.addItem(itemz)
itemz.setFlags(QtGui.QGraphicsItem.ItemClipsChildrenToShape | QtGui.QGraphicsItem.ItemClipsToShape)

# move item to its location
m = renderer.matrixForElement("background")
print(m)
r = m.mapRect(renderer.boundsOnElement("background"))
print(r)
itembg.setPos(r.x(), r.y())

# move item to its location
m = renderer.matrixForElement("zeiger")
print(m)
r = m.mapRect(renderer.boundsOnElement("zeiger"))
print(r)
itemz.setPos(r.x(), r.y())

print(renderer.defaultSize())
view.resize(renderer.defaultSize())
view.show()

timer = QtCore.QTimer();
timer.pyqtConfigure(timeout=updateInstrument)
timer.start(1000);

sys.exit(app.exec_())

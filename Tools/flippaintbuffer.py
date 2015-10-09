import mari
import PythonQt

gui = PythonQt.QtGui 
core = PythonQt.QtCore 

def paintBufferFlip( scaleFactor ):
    paintBuffer = mari.canvases.paintBuffer()
    scale = paintBuffer.scale()
    scale = core.QSizeF( scale.width() * scaleFactor[0], scale.height() * scaleFactor[1] )
    paintBuffer.setScale( scale )

actionFlipX = mari.actions.create( 'Flip X', 'paintBufferFlip((-1,1))' )
actionFlipY = mari.actions.create( 'Flip Y', 'paintBufferFlip((1,-1))' )

actionFlipX.setShortcut("Shift+F")
actionFlipY.setShortcut("Alt+F")

mari.menus.addAction( actionFlipX, "MainWindow/P&ixo/&Paint Buffer" )
mari.menus.addAction( actionFlipY, "MainWindow/P&ixo/&Paint Buffer" )
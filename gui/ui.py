import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from transcribe import *
from classes import *
from syntax_py import *
from test_autocomplete import get_model, auto_complete

import serial


class ListenerThread(QThread):
    released = pyqtSignal()
    pressed = pyqtSignal()

    def __init__(self):
        QThread.__init__(self)

        self.ser = serial.Serial()
        self.ser.port = "COM5"
        self.ser.baudrate = 9600
        self.ser.timeout = None
        try:
            self.ser.open()
        except:
            pass

    def run(self):
        while 1:
            tdata =  self.ser.read().decode('utf-8')
            if tdata == '0':
                self.released.emit()


class App(QWidget):

    def __init__(self):
        super().__init__()

        

        self.title = 'Ducky GUI'
        self.left = 50
        self.top = 50

        rec = QApplication.desktop().screenGeometry()
        self.maxHeight = rec.height()
        self.maxWidth = rec.width()

        self.width = self.maxWidth//1.3
        self.height = self.maxHeight//1.3

        self.initUI()
        self.connect()
        self.setFont(QFont('Helvetica', 20))
        self.pars = Parser()
        self.model, self.tokenizer = get_model()
        self.auto_complete = False

        self.thread = ListenerThread()
        self.thread.start()
        self.thread.released.connect(self.forward)

    def initUI(self):

        self.leftWidg = QWidget()
        self.leftWidg.setMaximumWidth(self.width//2.7)
        self.leftLayout = QVBoxLayout()

        code = self.makeCode()
        self.makeText()

        self.leftLayout.addWidget(self.textBox)
        self.leftLayout.addWidget(code)
        self.leftWidg.setLayout(self.leftLayout)

        self.layout = QHBoxLayout()

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.imWidg = QScrollArea(self)
        self.image = QLabel(self)
        pixmap = QPixmap('HackHarvard_voice_coding/white.png')
        if pixmap.height() < self.height//2 or pixmap.height() > self.height*2:
            pixmap = pixmap.scaledToWidth(self.width//2-50)
        self.image.setPixmap(pixmap)
        self.imWidg.setWidget(self.image)

        self.layout.addWidget(self.leftWidg)
        self.layout.addWidget(self.imWidg)
        self.setLayout(self.layout)

        self.show()

    
    def forward(self):
        print("successs")
    
    def connect(self):
        self.convert.clicked.connect(self.convertCallback)
        self.undo.clicked.connect(self.undoCallback)

    def makeCode(self):
        widget = QGroupBox("Code")
        self.code = QPlainTextEdit()
        self.code.setReadOnly(True)
        self.undo = QPushButton("Undo")
        self.auto = QPushButton("Auto Complete")
        self.convert = QPushButton("Convert")
        layout = QGridLayout()
        layout.addWidget(self.convert, 0, 0)
        layout.addWidget(self.undo, 0, 1)
        layout.addWidget(self.auto, 1, 1)
        layout.addWidget(self.code, 1, 0, 1, 2)
        widget.setLayout(layout)
        return widget

    def makeText(self):
        self.textEntryWidg = QPlainTextEdit()

        self.textBox = QGroupBox("Input")
        self.textBox.setFixedHeight(self.height//3)
        self.textBoxLayout = QVBoxLayout()
        self.textBoxLayout.addWidget(self.textEntryWidg)
        self.textBox.setLayout(self.textBoxLayout)

    def redrawImage(self):
        pixmap = QPixmap('classes_example.png')
        ratio = pixmap.height()/pixmap.width()
        ratioTarget = self.height*2/pixmap.height()
        if pixmap.height() < int(self.height//1.5):
            if ratio < ratioTarget:
                pixmap = pixmap.scaledToHeight(self.height-50)
            else:
                pixmap = pixmap.scaledToWidth(self.width//2-50)

        self.image.setPixmap(pixmap)
        self.image.setMinimumSize(pixmap.width()+10, pixmap.height()+10)
        self.layout.addWidget(self.leftWidg)
        self.layout.addWidget(self.imWidg)
        self.setLayout(self.layout)
        self.show()

    def convertCallback(self):
        text = self.textEntryWidg.toPlainText()
        self.pars.clear()
        self.pars.parseText(text)
        self.pars.write()
        self.pars.makePNG()
        self.redrawImage()
        with open(self.pars.getName()+'.py') as f:
            code = f.read()
            f.close()

        if self.auto_complete:
            prompts = [prompt for prompt in code.splitlines() if prompt != ""]
            code = auto_complete(prompts, self.model, self.tokenizer)

        self.code.setPlainText(code)
        self.highlighter = Highlighter(self.code.document())

    def undoCallback(self):
        text = self.textEntryWidg.toPlainText()
        i = text[:-1].rfind('.')
        if i != -1:
            text = text[:i+1]
        self.textEntryWidg.clear()
        self.textEntryWidg.setPlainText(text)
        self.convertCallback()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

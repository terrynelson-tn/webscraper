import sys
import random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore  import *
from scrapeDef import *

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'webscraper'
        self.left = 1000
        self.top = 720
        self.width = 400
        self.height = 140
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
    
        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280,40)
        
        # Create a button in the window
        self.button = QPushButton('search', self)
        self.button.move(20,80)
        
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()
    
    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        scrapeResult = scrape(textboxValue)
        # scrape Result is a list of results
        stringRes = ""
        for item in scrapeResult:
            # turn results into a string
            stringRes = stringRes + item + "\n" 

        result = QMessageBox.question(self, 'webscraper', "Results: \n\n" + stringRes, QMessageBox.Ok, QMessageBox.Ok)
        
        #QMessageBox.question(self, 'webscraper', "Results: " + scrapeResult[item], QMessageBox.Ok, QMessageBox.Ok)
        
        self.textbox.setText("")
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

import sys
import webbrowser
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore  import *
from scrapeDef import *

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'NEW'
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
        self.textbox.move(10, 20)
        self.textbox.resize(300,40)
        
        # Create a button in the window
        self.button = QPushButton('search', self)
        self.button.move(10,80)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        

        # Create another button in the window
        self.button1 = QPushButton('readme', self)
        self.button1.move(210,80)

        # connect button to function on_click
        self.button1.clicked.connect(self.on_click_readme)
        

        # Create another button in the window
        self.button2 = QPushButton('pageRef', self)
        self.button2.move(110,80)

        # connect button to function on_click
        self.button2.clicked.connect(self.on_click_reference)
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
        
        self.textbox.setText("")

    @pyqtSlot()
    def on_click_readme(self):
        f = open("README.md")
        QMessageBox.question(self, 'webscraper', "Readme: \n\n" + f.read(), QMessageBox.Ok, QMessageBox.Ok)
        print(f.read())

    @pyqtSlot()
    def on_click_reference(self):
        webbrowser.open('https://www.newegg.com/todays-deals?cm_sp=Homepage_dailydeal-_--_-10272021&quicklink=true')
    




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

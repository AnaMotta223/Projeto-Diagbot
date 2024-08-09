
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox, QAction
from PyQt5.QtGui import QPixmap, QIcon
import sys
import time

class loading:
   def progress(self):
  
        # setting for loop to set value of progress bar
        for i in range(101):
  
            # slowing down the loop
            time.sleep(0.05)
  
            # setting value to progress bar
            self.ProgressBar.setValue(i)
            self.show()
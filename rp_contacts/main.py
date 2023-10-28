# _*_ coding: utf-8 _*_
# rp_contacts/main.py

"""This module provides RPContacts application."""

import sys

from PyQt5.QtWidgets import QApplication
from .views import Window

def main():
    """RP Contacts Application"""

    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
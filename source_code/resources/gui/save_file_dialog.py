import os
import sys
from PyQt5 import QtWidgets

def save_file_dialog():
	dialog = QtWidgets.QFileDialog()
	options = QtWidgets.QFileDialog.Options()
	#options |= QtWidgets.QFileDialog.DontUseNativeDialog
	filename, _ = QtWidgets.QFileDialog.getSaveFileName(dialog, 'Save file', "","ASCII files (*.dat)")
	if filename:
		return filename
	else:
		return None
from PyQt5 import QtWidgets


def open_file_dialog():
	dialog = QtWidgets.QFileDialog()
	options = QtWidgets.QFileDialog.Options()
	#options |= QtWidgets.QFileDialog.DontUseNativeDialog
	filename, _ = QtWidgets.QFileDialog.getOpenFileName(dialog, 'Select file', "","ASCII files (*.ascii *.dat *.txt *.csv)")
	if filename:
		return filename
	else:
		return None
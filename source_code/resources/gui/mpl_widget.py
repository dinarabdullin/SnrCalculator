from PyQt5 import QtWidgets
import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

    
class MplWidget(FigureCanvas):
	def __init__(self, parent=None):
		self.fig = Figure()
		self.axes = self.fig.add_subplot(111)
		FigureCanvas.__init__(self, self.fig)
		self.setParent(parent)
		FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		FigureCanvas.updateGeometry(self)
#import sys
from PyQt5.QtCore import QObject, pyqtSlot
from resources.gui.open_file_dialog import open_file_dialog


class MainController(QObject):
    def __init__(self, model):
        super().__init__()
        self._model = model

    @pyqtSlot()
    def load_call(self):
        filename = open_file_dialog()
        if (filename != None):
            self._model.filename = filename
            
    @pyqtSlot(int)
    def change_mirror_data(self, value):
        self._model.mirror_data = bool(value)

    @pyqtSlot(str)	
    def change_acquisition_time(self, value):
        self._model.acquisition_time = float(value)

    @pyqtSlot(int)	
    def change_acquisition_time_units(self, value):
        self._model.acquisition_time_units = value

    @pyqtSlot(str)
    def change_modulation_depth(self, value):
        self._model.modulation_depth = float(value) * 0.01

    @pyqtSlot(int)
    def change_window_size(self, value):
        self._model.window_size = value
        
    @pyqtSlot(int)
    def change_polynomial_order(self, value):
        self._model.polynomial_order = value

    @pyqtSlot(int)	
    def change_snr_units(self, value):
        self._model.snr_units = value

    @pyqtSlot(int)	
    def change_display_signal(self, value):
        self._model.show_signal = bool(value)

    @pyqtSlot(int)
    def change_display_interpolation(self, value):
        self._model.show_extrapolation = bool(value)

    @pyqtSlot(int)
    def change_display_noise(self, value):
        self._model.show_noise = bool(value)

    @pyqtSlot(int)
    def change_display_modulation_depth(self, value):
        self._model.show_modulation_depth = bool(value)

    @pyqtSlot()	
    def optimize_window_size_call(self):
        self._model.optimize_window_size()
        
    @pyqtSlot()	
    def pick_window_size(self, event):
        if (event.pickx): 
            self._model.window_size = int(event.pickx[0][0])
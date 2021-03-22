import sys
import sys
import copy
import numpy as np
from scipy.signal import savgol_filter
from PyQt5.QtCore import QObject, pyqtSignal
from resources.initialization import initialization_data
from resources.gui.load_data import load_data
from resources.math.mirror_data import mirror_data
from resources.math.modulation_depth import calculate_modulation_depth
from resources.math.snr import calculate_snr
from resources.math.snr_units import change_snr_units
from resources.math.std import calculate_std
from resources.math.rmsd import calculate_rmsd


class Model(QObject):
    filename_changed = pyqtSignal()
    data_changed = pyqtSignal()
    window_size_ranges_changed = pyqtSignal()
    snr_changed = pyqtSignal()
    modulation_depth_changed = pyqtSignal()
    noise_std_changed = pyqtSignal()
    window_size_opt_changed = pyqtSignal()
    window_size_opt_reset = pyqtSignal()

    @property
    def filename(self):
        return self._filename
        
    @filename.setter
    def filename(self, value):
        self._filename = value
        self.filename_changed.emit()
        # read data
        self._original_data = {}
        self._original_data['t'], self._original_data['signal'] = \
            load_data(self._filename, initialization_data['column_number_time'], initialization_data['column_number_signal'])
        self._data = {}
        if (self._mirror_data):
            self._data['t'], self._data['signal'] = mirror_data(self._original_data['t'], self._original_data['signal'])
        else:
            self._data = copy.deepcopy(self._original_data)
        self._modulation_depth = calculate_modulation_depth(self._data['signal'])
        self._data['modulation_depth'] = (1.0 - self._modulation_depth) * np.amax(self._data['signal']) * np.ones(self._data['signal'].size)
        self.modulation_depth_changed.emit()
        # update the window size ranges
        self.update_window_size_ranges()
        self.window_size_ranges_changed.emit()
        # reset the window size optimization
        self._window_size_opt = {}
        self.window_size_opt_reset.emit()
        # update snr
        self.run_snr_calculation()
        self.snr_changed.emit()
        self.noise_std_changed.emit()
        self.data_changed.emit()

    @property
    def data(self):
        return self._data
        
    @property
    def mirror_data(self):
        return self._mirror_data
        
    @mirror_data.setter
    def mirror_data(self, value):
        self._mirror_data = value
        if (self._original_data):
            # update data
            if (self._mirror_data):
                self._data = {}
                self._data['t'], self._data['signal'] = mirror_data(self._original_data['t'], self._original_data['signal'])
            else:
                self._data = copy.deepcopy(self._original_data)
            self._data['modulation_depth'] = (1.0 - self._modulation_depth) * np.amax(self._data['signal']) * np.ones(self._data['signal'].size)
            # reset the window size optimization
            self._window_size_opt = {}
            self.window_size_opt_reset.emit()
            # update snr
            self.run_snr_calculation()
            self.snr_changed.emit()  
            self.data_changed.emit()

    @property
    def acquisition_time(self):
        return self._acquisition_time
        
    @acquisition_time.setter	
    def acquisition_time(self, value):
        self._acquisition_time = value
        # update snr
        if (self._snr_unitless):
            self._snr = change_snr_units(self._snr_unitless, self._snr_units, self._acquisition_time, self._acquisition_time_units)
            self.snr_changed.emit()

    @property
    def acquisition_time_units(self):
        return self._acquisition_time_units

    @acquisition_time_units.setter
    def acquisition_time_units(self, value):
        self._acquisition_time_units = initialization_data['acqusition_time_units_options'][value]
        # update snr
        if (self._snr_unitless):
            self._snr = change_snr_units(self._snr_unitless, self._snr_units, self._acquisition_time, self._acquisition_time_units)
            self.snr_changed.emit()   

    @property
    def window_size(self):
        return self._window_size
        
    @property
    def window_size_min(self):
        return self._window_size_min
        
    @property
    def window_size_max(self):
        return self._window_size_max 
        
    @window_size.setter
    def window_size(self, value):
        if (value % 2 == 0):
            self._window_size = value - 1
        else:
            self._window_size = value
        if (self._data):
            # update snr
            self.run_snr_calculation()
            self.snr_changed.emit()
            self.noise_std_changed.emit()
            self.data_changed.emit()
        if (self._window_size_opt):
            self.window_size_opt_changed.emit()

    @property
    def polynomial_order(self):
        return self._polynomial_order
        
    @polynomial_order.setter
    def polynomial_order(self, value):
        self._polynomial_order = value
        # update the window size ranges
        self.update_window_size_ranges()
        self.window_size_ranges_changed.emit()
        # reset the window size optimization
        self._window_size_opt = {}
        self.window_size_opt_reset.emit()        
        if (self._data):
            # update snr
            self.run_snr_calculation()
            self.snr_changed.emit()
            self.noise_std_changed.emit()
            self.data_changed.emit()

    @property
    def snr(self):
        return self._snr
        
    @property
    def snr_units(self):
        return self._snr_units

    @snr_units.setter
    def snr_units(self, value):
        self._snr_units = initialization_data['snr_units_options'][value]
        if (self._snr_unitless):
            # update snr
            self._snr = change_snr_units(self._snr_unitless, self._snr_units, self._acquisition_time, self._acquisition_time_units)
            self.snr_changed.emit() 
    
    @property
    def modulation_depth(self):
        return self._modulation_depth
        
    @modulation_depth.setter
    def modulation_depth(self, value):
        self._modulation_depth = value
        if (self._data):
            # update data
            self._data['modulation_depth'] = (1.0 - self._modulation_depth) * np.amax(self._data['signal']) * np.ones(self._data['signal'].size)
            # reset the window size optimization
            self._window_size_opt = {}
            self.window_size_opt_reset.emit()
            # update snr
            self.run_snr_calculation()
            self.snr_changed.emit()	
            self.noise_std_changed.emit()
            self.data_changed.emit()
    
    @property
    def noise_std(self):
        return self._noise_std    
    
    @property
    def show_signal(self):
        return self._show_signal
        
    @show_signal.setter
    def show_signal(self, value):
        self._show_signal = value
        if (self._data):
            self.data_changed.emit()

    @property
    def show_extrapolation(self):
        return self._show_extrapolation
        
    @show_extrapolation.setter
    def show_extrapolation(self, value):
        self._show_extrapolation = value
        if (self._data):
            self.data_changed.emit()
            
    @property
    def show_noise(self):
        return self._show_noise
        
    @show_noise.setter
    def show_noise(self, value):
        self._show_noise = value
        if (self._data):
            self.data_changed.emit()

    @property
    def show_modulation_depth(self):
        return self._show_modulation_depth
        
    @show_modulation_depth.setter
    def show_modulation_depth(self, value):
        self._show_modulation_depth = value
        if (self._data):
            self.data_changed.emit()

    @property
    def window_size_opt(self):
        return self._window_size_opt

    def update_window_size_ranges(self):
        # min window size
        if (self._polynomial_order % 2 == 0):
            self._window_size_min = self._polynomial_order + 3
        else:
            self._window_size_min = self._polynomial_order + 2
        # max window size
        if (self._data):
            max_length = int(self._data['signal'].size / 2)
            if (max_length % 2 == 0):
                self._window_size_max = max_length - 1
            else:
                self._window_size_max = max_length
        # check whether the current window size is larger than the min and smaller than max
        if (self._window_size < self._window_size_min):
            self._window_size = self._window_size_min
        if (self._window_size > self._window_size_max):
            self._window_size = self._window_size_max

    def run_snr_calculation(self):
        # interpolate the experimental time trace using the Savitzky-Golay filter
        self._data['interpolation'] = savgol_filter(self._data['signal'], window_length=self._window_size, polyorder=self._polynomial_order)
        # calculate the noise
        self._data['noise'] = self._data['signal'] - self._data['interpolation']
        # calculate SNR
        self._snr_unitless, self._noise_std = calculate_snr(self._modulation_depth, self._data['noise'])
        self._snr = change_snr_units(self._snr_unitless, self._snr_units, self._acquisition_time, self._acquisition_time_units)

    def optimize_window_size(self):
        window_size_array = np.arange(self._window_size_min, self._window_size_max+2, 2)
        rmsd_list = []
        noise_std_list = []
        snr_list = []
        for w in window_size_array:
            # interpolate the experimental time trace using the Savitzky-Golay filter
            interpolation = savgol_filter(self._data['signal'], window_length=w, polyorder=self._polynomial_order)
            # calculate mean-squared-deviation between the experimental signal and its interpolation
            rmsd = calculate_rmsd(self._data['signal'], interpolation)
            # calculate the noise
            noise = self._data['signal'] - interpolation
            # calculate the standard deviation of noise
            noise_std = calculate_std(noise)
            # calculate SNR
            snr_unitless = calculate_snr(self._modulation_depth, noise)
            # store calculated quantities
            rmsd_list.append(rmsd)
            noise_std_list.append(noise_std)
            snr_list.append(snr_unitless)
        self._window_size_opt['window_size'] = window_size_array
        self._window_size_opt['rmsd'] = np.array(rmsd_list)
        self._window_size_opt['noise_std'] = np.array(noise_std_list)
        self._window_size_opt['snr'] = np.array(snr_list)	
        self.window_size_opt_changed.emit()

    def __init__(self):
        super().__init__()
        self._filename = ''
        self._original_data = {}
        self._data = {}
        self._mirror_data = initialization_data['mirror_data']
        self._acquisition_time = initialization_data['acqusition_time']
        self._acquisition_time_units = initialization_data['acquisition_time_units']
        self._window_size = initialization_data['window_size']
        self._window_size_min = 0
        self._window_size_max = 1000
        self._polynomial_order = initialization_data['polynomial_order']
        self._modulation_depth = initialization_data['modulation_depth']
        self._noise_std = initialization_data['noise_std']
        self._snr_unitless = initialization_data['snr']
        self._snr = initialization_data['snr']
        self._snr_units = initialization_data['snr_units']
        self._show_signal = initialization_data['show_signal']
        self._show_extrapolation = initialization_data['show_interpolation']
        self._show_noise = initialization_data['show_noise']
        self._show_modulation_depth = initialization_data['show_modulation_depth']
        self._window_size_opt = {}
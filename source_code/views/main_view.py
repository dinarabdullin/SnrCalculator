import numpy as np
import matplotlib.pyplot as plt
# get the default matplotlib colors
mpl_colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
from matplotlib import rcParams
rcParams['font.size'] = 9
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from resources.main_view_ui import Ui_MainWindow
from resources.about_view_ui import Ui_AboutDialog
from resources.gui.mpl_widget import MplWidget
from resources.gui.mpl_toolbar import MplToolbar
from resources.initialization import initialization_data, snr_units_names, snr_units_acronyms
from resources.gui.save_file_dialog import save_file_dialog


class MainView(QtWidgets.QMainWindow):
    def __init__(self, model, main_controller):
        super().__init__()
        # init ui
        self._model = model
        self._main_controller = main_controller
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)  
        self.init_ui_widgets()
        self.init_menubar()
        # connect widgets to the controller
        self._ui.pushButton_load.clicked.connect(self._main_controller.load_call)
        self._ui.checkBox_mirror.stateChanged.connect(self._main_controller.change_mirror_data)
        self._ui.lineEdit_time.textChanged.connect(self._main_controller.change_acquisition_time)
        self._ui.comboBox_time.currentIndexChanged.connect(self._main_controller.change_acquisition_time_units)
        self._ui.lineEdit_modulation_depth.textChanged.connect(self._main_controller.change_modulation_depth)
        self._ui.spinBox_window.valueChanged.connect(self._main_controller.change_window_size)
        self._ui.spinBox_order.valueChanged.connect(self._main_controller.change_polynomial_order)
        self._ui.comboBox_snr.currentIndexChanged.connect(self._main_controller.change_snr_units)
        self._ui.checkBox_signal.stateChanged.connect(self._main_controller.change_display_signal)
        self._ui.checkBox_interpolation.stateChanged.connect(self._main_controller.change_display_interpolation)
        self._ui.checkBox_noise.stateChanged.connect(self._main_controller.change_display_noise)
        self._ui.checkBox_modulation_depth.stateChanged.connect(self._main_controller.change_display_modulation_depth)
        self._ui.pushButton_optimize.clicked.connect(self._main_controller.optimize_window_size_call)
        # listen for model event signals
        self._model.filename_changed.connect(self.on_filename_changed)
        self._model.data_changed.connect(self.on_data_changed)
        self._model.modulation_depth_changed.connect(self.on_modulation_depth_changed)
        self._model.window_size_ranges_changed.connect(self.on_window_size_ranges_changed)
        self._model.snr_changed.connect(self.on_snr_changed)
        self._model.noise_std_changed.connect(self.on_noise_std_changed)
        self._model.window_size_opt_changed.connect(self.on_window_size_opt_changed)
        self._model.window_size_opt_reset.connect(self.on_window_size_opt_reset)

    def init_ui_widgets(self):
        # add matplotlib items
        self.mplWidget_signal, self.mplToolbar_signal = self.add_mpl_item(self._ui.frame_signal)
        self.mplWidget_noise, self.mplToolbar_noise = self.add_mpl_item(self._ui.frame_noise)
        self.mplWidget_msd, self.mplToolbar_msd = self.add_mpl_item(self._ui.frame_msd)
        self.mplWidget_snr, self.mplToolbar_snr = self.add_mpl_item(self._ui.frame_snr)
        # unit values of the ui widgets
        self._ui.lineEdit_path.setReadOnly(True)
        self._ui.checkBox_mirror.setChecked(initialization_data['mirror_data'])
        self._ui.comboBox_time.clear()
        self._ui.comboBox_time.addItems(initialization_data['acqusition_time_units_options'])
        self._ui.spinBox_window.setValue(initialization_data['window_size'])
        self._ui.spinBox_order.setValue(initialization_data['polynomial_order'])
        self._ui.spinBox_order.setMinimum(initialization_data['polynomial_order_min'])
        self._ui.spinBox_order.setMaximum(initialization_data['polynomial_order_max'])
        self._ui.lineEdit_snr.setReadOnly(True)
        self._ui.comboBox_snr.clear()
        self._ui.comboBox_snr.addItems(initialization_data['snr_units_options'])
        self._ui.lineEdit_noise_std.setReadOnly(True)
        self._ui.checkBox_signal.setChecked(initialization_data['show_signal'])
        self._ui.checkBox_interpolation.setChecked(initialization_data['show_interpolation'])
        self._ui.checkBox_noise.setChecked(initialization_data['show_noise'])
        self._ui.checkBox_modulation_depth.setChecked(initialization_data['show_modulation_depth'])
        # some cosmetics
        self._ui.groupBox_loaddata.setStyleSheet("QGroupBox { font-weight: bold; }")
        self._ui.groupBox_interpolation.setStyleSheet("QGroupBox { font-weight: bold; }")
        self._ui.groupBox_snr.setStyleSheet("QGroupBox { font-weight: bold; }")
        self._ui.groupBox_display.setStyleSheet("QGroupBox { font-weight: bold; }")
        self._ui.groupBox_windowsize.setStyleSheet("QGroupBox { font-weight: bold; }")
        self._ui.checkBox_signal.setStyleSheet("color: "+mpl_colors[0])
        self._ui.checkBox_interpolation.setStyleSheet("color: "+mpl_colors[1])
        self._ui.checkBox_noise.setStyleSheet("color: "+mpl_colors[2])
        self._ui.checkBox_modulation_depth.setStyleSheet("color: "+mpl_colors[3])

    def add_mpl_item(self, parent):
        verticalLayout = QtWidgets.QVBoxLayout(parent)
        mplWidget = MplWidget(parent)
        mplToolbar = MplToolbar(mplWidget, parent)
        verticalLayout.addWidget(mplWidget)
        verticalLayout.addWidget(mplToolbar)
        return [mplWidget, mplToolbar]

    def init_menubar(self):
        self._ui.actionLoad.triggered.connect(self._main_controller.load_call)
        self._ui.actionSave_snr.triggered.connect(self.on_save_snr)
        self._ui.actionSave_interpolation.triggered.connect(self.on_save_interpolation)
        self._ui.actionExit.triggered.connect(self.close)
        self._ui.actionAbout.triggered.connect(self.on_about)

    def on_save_snr(self):
        filename = save_file_dialog()
        if (filename != None):
            data = {}
            data['Filename'] = self._model.filename
            data['Mirror data about 0'] = self._model.mirror_data
            data['Acquisition time'] = self._model.acquisition_time
            data['Acquisition time units'] = self._model.acquisition_time_units
            data['Modulation depth'] = self._model.modulation_depth
            data['Window size'] = self._model.window_size
            data['Polynomial order'] = self._model.polynomial_order
            data['Signal/Noise'] = self._model.snr
            for key, value in snr_units_acronyms.items():
                if (snr_units_names[key] == self._model.snr_units):
                    data['Signal/Noise units'] = snr_units_acronyms[key]
                    break
            file = open(filename, 'w')
            for key, value in data.items():
                file.write('{0:<30s} {1:<30s} \n'.format(key, str(value)))
            file.close()
        
    def on_save_interpolation(self):
        filename = save_file_dialog()
        if (filename != None):
            file = open(filename, 'w')
            file.write("{0:<16s} {1:<16s} {2:<16s} {3:<16s} {4:<16s}\n".format('t', 'signal', 'interpolation', 'noise', 'mod. depth'))
            for i in range(self._model.data['t'].size):
                file.write('{0:<16.4f} {1:<16.6f} {2:<16.4f} {3:<16.6f} {3:<16.6f}\n'.format(self._model.data['t'][i], self._model.data['signal'][i], self._model.data['interpolation'][i], self._model.data['modulation_depth'][i]))
            file.close() 

    def on_about(self): 
        dialog = QtWidgets.QDialog()
        ui = Ui_AboutDialog()
        ui.setupUi(dialog) 
        dialog.show()
        dialog.exec_()
        
    def update_signal_plot(self, mplWidget):
        # prepare the data to plot
        X = []
        Y = []
        colors = []
        if (self._model.show_signal):
            X.append(self._model.data['t'])
            Y.append(self._model.data['signal'])
            colors.append(mpl_colors[0])
        if (self._model.show_extrapolation):
            X.append(self._model.data['t'])
            Y.append(self._model.data['interpolation'])
            colors.append(mpl_colors[1])
        if (self._model.show_noise):
            X.append(self._model.data['t'])
            Y.append(self._model.data['noise'])
            colors.append(mpl_colors[2])
        if (self._model.show_modulation_depth):
            X.append(self._model.data['t'])
            Y.append(self._model.data['modulation_depth'])
            colors.append(mpl_colors[3])
        # update plot
        mplWidget.axes.clear()
        if (X):
            xmin = np.amin([np.amin(x) for x in X])
            xmax = np.amax([np.amax(x) for x in X])
            ymin = np.amin([np.amin(y) for y in Y])
            ymax = np.amax([np.amax(y) for y in Y])
            for i in range(len(X)):
                mplWidget.axes.plot(X[i], Y[i], color=colors[i])
            mplWidget.axes.set_xlim(xmin, xmax)
            mplWidget.axes.set_ylim(ymin-0.1, ymax+0.1)
            mplWidget.axes.set_xlabel('Time')
            mplWidget.axes.set_ylabel('Amplitude')
            mplWidget.fig.tight_layout()
        mplWidget.draw()

    def update_window_size_opt_plot(self, mplWidget, x, y, xlabel='', ylabel=''):
        mplWidget.axes.clear()
        #mplWidget.axes.plot(x, y, linestyle='-', marker='o', markersize=4, markerfacecolor='white', picker=self.line_picker)
        #mplWidget.axes.semilogx(x, y, linestyle='-', marker='o', markersize=4, markerfacecolor='white', picker=self.line_picker)
        #mplWidget.axes.semilogy(x, y, linestyle='-', marker='o', markersize=4, markerfacecolor='white', picker=self.line_picker)
        mplWidget.axes.loglog(x, y, linestyle='-', marker='o', markersize=4, markerfacecolor='white', picker=self.line_picker)
        mplWidget.fig.canvas.mpl_connect('pick_event', self._main_controller.pick_window_size)     
        mplWidget.axes.plot(self._model.window_size*np.ones(2), np.array([np.amin(y), np.amax(y)]), linestyle='--', color='red')
        mplWidget.axes.set_xlabel(xlabel)
        mplWidget.axes.set_ylabel(ylabel)
        mplWidget.fig.tight_layout()
        mplWidget.draw()

    def line_picker(self, line, mouseevent):
        if mouseevent.xdata is None:
            return False, dict()
        xdata = line.get_xdata()
        ydata = line.get_ydata()
        dlim = 1
        #d = np.sqrt((xdata - mouseevent.xdata)**2. + (ydata - mouseevent.ydata)**2.)
        d = np.sqrt((xdata - mouseevent.xdata)**2)
        ind = np.nonzero(np.less_equal(d, dlim))
        if len(ind):
            pickx = np.take(xdata, ind)
            picky = np.take(ydata, ind)
            props = dict(ind=ind, pickx=pickx, picky=picky)
            self._ui.spinBox_window.setValue(pickx[0][0])
            return True, props
        else:
            return False, dict()

    @pyqtSlot()
    def on_filename_changed(self):
        self._ui.lineEdit_path.setText(self._model.filename)

    @pyqtSlot()
    def on_data_changed(self):
        self.update_signal_plot(self.mplWidget_signal)
        
    @pyqtSlot()
    def on_modulation_depth_changed(self):
        text = "{:.1f}".format(100*self._model.modulation_depth)
        self._ui.lineEdit_modulation_depth.setText(text)
        
    @pyqtSlot()
    def on_window_size_ranges_changed(self):
        self._ui.spinBox_window.setMinimum(self._model.window_size_min)
        self._ui.spinBox_window.setMaximum(self._model.window_size_max)
        self._ui.spinBox_window.setValue(self._model.window_size)

    @pyqtSlot()
    def on_snr_changed(self):
        line_text = ''
        if np.isnan(self._model.snr):
            line_text = 'nan'
        else:
            line_text = str(int(self._model.snr))
        self._ui.lineEdit_snr.setText(line_text)

    @pyqtSlot()
    def on_noise_std_changed(self):
        line_text = ''
        if np.isnan(self._model.noise_std):
            line_text = 'nan'
        else:
            line_text = '{:>10.4f}'.format(float(self._model.noise_std))
        self._ui.lineEdit_noise_std.setText(line_text)

    @pyqtSlot()
    def on_window_size_opt_changed(self):
        self.update_window_size_opt_plot(self.mplWidget_noise, 
                                         self._model.window_size_opt['window_size'],
                                         self._model.window_size_opt['noise_std'],
                                         xlabel = 'Window size',
                                         ylabel = 'std(Noise)')
        self.update_window_size_opt_plot(self.mplWidget_msd, 
                                         self._model.window_size_opt['window_size'],
                                         self._model.window_size_opt['rmsd'],
                                         xlabel = 'Window size',
                                         ylabel = 'rmsd(Signal, Interpolation)')
        self.update_window_size_opt_plot(self.mplWidget_snr, 
                                         self._model.window_size_opt['window_size'],
                                         self._model.window_size_opt['snr'],
                                         xlabel = 'Window size',
                                         ylabel = 'Signal/Noise')
                                         
    @pyqtSlot()
    def on_window_size_opt_reset(self):
        self.mplWidget_noise.axes.clear()
        self.mplWidget_noise.draw()
        self.mplWidget_msd.axes.clear()
        self.mplWidget_msd.draw()
        self.mplWidget_snr.axes.clear()
        self.mplWidget_snr.draw()      
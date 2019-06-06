SnrCalculator
=========
The program SnrCalculator allows determination of signal-to-noise ratio (SNR) for pulsed EPR dipolar spectroscopy data. In this program, SNR is defined as a ratio between the modulation depth of the PDS time trace and the standard deviation of the corresponding noise. To extract noise from the experimental PDS time trace, this time traces is interpolated using the Savitzky-Golay filter and then the result of interpolation is subtracted from the time trace.

General Information
=========
The source code of the program is written in Python 3.7 using the libraries numpy, scipy, matplotlib, PyQt-5 and pyqt5-tools. 
The ready-to-use executables of the program are provided for Windows, Linux [in progress] and OS [in progress].

Copyright
=========
This program can be distributed under GNU General Public License.

If you use this code please cite: [edit]

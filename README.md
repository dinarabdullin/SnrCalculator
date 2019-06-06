SnrCalculator
=========
A program SnrCalculator allows determination of the signal-to-noise ratio (SNE) for the pulsed EPR dipolar spectroscopy data. In this program, the SNR is defined as a ratio between the modulation depth of the PDS time trace and the standard deviation of noise. To extract the noise from the experimental PDS time traces, these time traces are interpolated using the Savitzky-Golay filter and then the result of interpolation is subtracted from the time traces.

General Information
=========
The source code of the program is written in Python 3.7 using the libraries numpy, scipy, matplotlib, PyQt-5 and pyqt5-tools. 

Copyright
=========
This program can be distributed under GNU General Public License.

If you use this code please cite: [edit]

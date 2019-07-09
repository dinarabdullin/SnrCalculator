SnrCalculator
=========
The program SnrCalculator allows determining signal-to-noise ratios (SNR) of pulsed EPR dipolar spectroscopy (PDS) signals. In this program, SNR is defined as a ratio between the modulation depth of a PDS time trace and the standard deviation of noise. To extract the noise contribution from the PDS signal, the PDS time trace is interpolated using the Savitzky-Golay filter and then the result of the interpolation is subtracted from the original signal.

General Information
=========
The source code of the program is written in Python 3.7 using the libraries numpy, scipy, matplotlib, PyQt-5 and pyqt5-tools. 
The ready-to-use executables of the program are provided for Windows, Linux and OS [in progress] (see Releases tab)

Copyright
=========
This program can be distributed under GNU General Public License.

If you use this code please cite: [will be updated soon]

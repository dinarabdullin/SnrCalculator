SnrCalculator
=========
The program SnrCalculator allows determining the signal-to-noise ratio (SNR) of pulsed EPR dipolar spectroscopy (PDS) signals. In this program, SNR is defined as a ratio between the modulation depth of a PDS time trace and the standard deviation of noise. To extract the noise contribution from the PDS signal, the PDS time trace is interpolated using the Savitzky-Golay filter and then the result of the interpolation is subtracted from the original signal.

General Information
=========
The source code of the program is written in Python 3.7 using the libraries numpy, scipy, matplotlib, PyQt-5 and pyqt5-tools.

The Windows and Linux executables of the program are provided at:
https://github.com/dinarabdullin/SnrCalculator/releases

The user guide of the program will be published shortly.

Copyright
=========
This program can be distributed under GNU General Public License.

If you use this code please cite: 
D. Abdullin, P. Brehm, N. Fleck, S. Spicher, S. Grimme, O. Schiemann, Pulsed EPR Dipolar Spectroscopy on Spin Pairs with one Highly Anisotropic Spin Center: The Low‐Spin Fe(III) Case, Chem. Eur. J. 2019, 25, 14388-14398.

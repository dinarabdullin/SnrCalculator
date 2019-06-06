import numpy as np
from resources.initialization import snr_units_names

	
def snr_unitless(snr, N, Nunits):
	return snr

def snr_dB(snr, N, Nunits):
	return (20 * np.log10(snr))

def snr_hour(snr, N, Nunits):
	if (N != 0) and (Nunits == 'hours'):
		return (snr / np.sqrt(float(N)))
	elif (N != 0) and (Nunits == 'minutes'):
		return (snr / np.sqrt(float(N)/60.0))
	else:
		return np.nan

def snr_dB_hour(snr, N, Nunits):
	if (N != 0) and (Nunits == 'hours'):
		return (20 * np.log10(snr) / np.sqrt(float(N)))
	elif (N != 0) and (Nunits == 'minutes'):
		return (20 * np.log10(snr) / np.sqrt(float(N)/60.0))
	else:
		return np.nan
		
def snr_minute(snr, N, Nunits):
	if (N != 0) and (Nunits == 'minutes'):
		return (snr / np.sqrt(float(N)))
	elif (N != 0) and (Nunits == 'hours'):
		return (snr / np.sqrt(float(N)*60.0))
	else:
		return np.nan
		
def snr_dB_minute(snr, N, Nunits):
	if (N != 0) and (Nunits == 'minutes'):
		return (20 * np.log10(snr) / np.sqrt(float(N)))
	elif (N != 0) and (Nunits == 'hours'):
		return (20 * np.log10(snr) / np.sqrt(float(N)*60.0))
	else:
		return np.nan

def snr_scan(snr, N, Nunits):
	if (N != 0) and (Nunits == 'scans'):
		return (snr / np.sqrt(float(N)))
	else:
		return np.nan
		
def snr_dB_scan(snr, N, Nunits):
	if (N != 0) and (Nunits == 'scans'):
		return (20 * np.log10(snr) / np.sqrt(float(N)))
	else:
		return np.nan

snr_units_convertor = {
	'snr_unitless' : snr_unitless, 
	'snr_dB'       : snr_dB,
	'snr_hour'     : snr_hour,
	'snr_dB_hour'  : snr_dB_hour, 
	'snr_minute'   : snr_minute,
	'snr_dB_minute': snr_dB_minute, 
	'snr_scan'     : snr_scan,
	'snr_dB_scan'  : snr_dB_scan
}

def change_snr_units(snr, snr_units, N, N_units):
	for key, value in snr_units_convertor.items():
		if (snr_units_names[key] == snr_units):
			snr_new = snr_units_convertor[key](snr, N, N_units)
	return snr_new
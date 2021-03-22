snr_units_names = {
	'snr_unitless' : u'\u0075\u006e\u0069\u0074\u006c\u0065\u0073\u0073', 
	'snr_dB'       : u'\u0064\u0042',
	'snr_hour'     : u'\u0068\u006f\u0075\u0072\u207B\u00B9\u2E0D\u00B2',
	'snr_dB_hour'  : u'\u0064\u0042 \u0068\u006f\u0075\u0072\u207B\u00B9\u2E0D\u00B2', 
	'snr_minute'   : u'\u006d\u0069\u006e\u0075\u0074\u0065\u207B\u00B9\u2E0D\u00B2',
	'snr_dB_minute': u'\u0064\u0042 \u006d\u0069\u006e\u0075\u0074\u0065\u207B\u00B9\u2E0D\u00B2', 
	'snr_scan'     : u'\u0073\u0063\u0061\u006e\u207B\u00B9\u2E0D\u00B2',
	'snr_dB_scan'  : u'\u0064\u0042 \u0073\u0063\u0061\u006e\u207B\u00B9\u2E0D\u00B2'
}

snr_units_acronyms = {
	'snr_unitless' : 'unitless', 
	'snr_dB'       : 'dB', 
	'snr_hour'     : 'hour^(-1/2)', 
	'snr_dB_hour'  : 'dB hour^(-1/2)',  
	'snr_minute'   : 'minute^(-1/2)', 
	'snr_dB_minute': 'dB minute^(-1/2)', 
	'snr_scan'     : 'scan^(-1/2)', 
	'snr_dB_scan'  : 'dB scan^(-1/2)', 
}

initialization_data = {}
initialization_data['column_number_time'] = 0
initialization_data['column_number_signal'] = 1
initialization_data['mirror_data'] = False
initialization_data['acqusition_time'] = 0.0
initialization_data['acquisition_time_units'] = 'hours'
initialization_data['acqusition_time_units_options'] = ['hours', 'minutes', 'scans']
initialization_data['polynomial_order_min'] = 1
initialization_data['polynomial_order_max'] = 8
initialization_data['polynomial_order'] = 8
initialization_data['window_size'] = 11
initialization_data['modulation_depth'] = 0.0
initialization_data['noise_std'] = 0.0
initialization_data['snr'] = 0.0
initialization_data['snr_units'] = 'unitless'
initialization_data['snr_units_options'] = [
	snr_units_names['snr_unitless'],
	snr_units_names['snr_dB'],
	snr_units_names['snr_hour'],
	snr_units_names['snr_dB_hour'],
	snr_units_names['snr_minute'],
	snr_units_names['snr_dB_minute'],
	snr_units_names['snr_scan'],
	snr_units_names['snr_dB_scan']
]
initialization_data['show_signal'] = True
initialization_data['show_interpolation'] = True
initialization_data['show_noise'] = True
initialization_data['show_modulation_depth'] = True
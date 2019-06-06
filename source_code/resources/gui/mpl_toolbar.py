import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT


class MplToolbar(NavigationToolbar2QT):
	NavigationToolbar2QT.toolitems = (
		('Home', 'Reset original view', 'home', 'home'),
		('Back', 'Back to previous view', 'back', 'back'),
		('Forward', 'Forward to next view', 'forward', 'forward'),
		('Pan', 'Pan axes with left mouse, zoom with right', 'move', 'pan'),
		('Zoom', 'Zoom to rectangle', 'zoom_to_rect', 'zoom'),
		# ('Subplots', 'Configure subplots', 'subplots', 'configure_subplots'),
		#('Save', 'Save the figure', 'filesave', 'save_figure'),
	)
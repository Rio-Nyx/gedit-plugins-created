from gi.repository import GObject ,Gedit, Gtk

class ExamplePyPlugin(GObject.Object, Gedit.WindowActivatable):
	__gtype_name__ = "ExamplePyPlugin"

	view = GObject.property(type=Gedit.View)
	window = GObject.property(type=Gedit.Window)

	def __init__(self):
		GObject.Object.__init__(self)
		
	def do_activate(self):
		print ("Plugin created for",self.view)
		doc = self.window.get_active_document();
		if not doc:
			print ("Noe")
			return;
		tags="""<!DOCTYPE html>
<html>
		
<head>
<meta charset="UTF-8">	
<meta name="keywords" content="HTML, CSS, JavaScript">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="refresh" content="30">
<title>My page</title>
</head>
		
<body>
		
</body>
		
</html>"""
		doc.insert_at_cursor(tags)
		#Gtk.Widget.signals.leave_notify_event(window,event)
		#activates when pointer leaves the field
		pass
	def do_deactivate(self):
		print ("Plugin deactivate for",self.window)
		self.window=None
		pass

	def do_update_state(self):
		# Called whenever the view has been updated
		print ("Plugin update for")
		pass


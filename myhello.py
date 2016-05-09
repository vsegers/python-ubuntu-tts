#!/usr/bin/python2.5
# example helloworld.py

import pygtk
pygtk.require('2.0')
import gtk
import os, glob
import sys

class HelloWorld:

    # This is a callback function. The data arguments are ignored
    # in this example. More on callbacks below.
    def hello(self, widget, data=None):
        print "Hello World"

    def delete_event(self, widget, event, data=None):
        # If you return FALSE in the "delete_event" signal handler,
        # GTK will emit the "destroy" signal. Returning TRUE means
        # you don't want the window to be destroyed.
        # This is useful for popping up 'are you sure you want to quit?'
        # type dialogs.
        print "delete event occurred"

        # Change FALSE to TRUE and the main window will not be destroyed
        # with a "delete_event".
        return False

    def destroy(self, widget, data=None):
        print "destroy signal occurred"
        gtk.main_quit()

    def static_festival(self, widget, data=None):
	os.system("echo 'static festival' | festival --tts")
	
    def text_entry_festival(self, widget, data=None):
    	os.system("echo '"+self.entry.get_text()+"' | festival --tts")
    	
    def url_festival(self, widget, data=None):
    	os.system("festival --tts "+self.entry.get_text())

    def __init__(self):
        # create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
	self.window.set_size_request(300, 100)
    
        # When the window is given the "delete_event" signal (this is given
        # by the window manager, usually by the "close" option, or on the
        # titlebar), we ask it to call the delete_event () function
        # as defined above. The data passed to the callback
        # function is NULL and is ignored in the callback function.
        self.window.connect("delete_event", self.delete_event)
    
        # Here we connect the "destroy" event to a signal handler.  
        # This event occurs when we call gtk_widget_destroy() on the window,
        # or if we return FALSE in the "delete_event" callback.
        self.window.connect("destroy", self.destroy)
    
        # Sets the border width of the window.
        self.window.set_border_width(10)

    
        # Creates a new button with the label "Hello World".
        self.button = gtk.Button("Close")
	self.button1 = gtk.Button("speak TEXT")
	self.button2 = gtk.Button("speak URL")
    
        # When the button receives the "clicked" signal, it will call the
        # function hello() passing it None as its argument.  The hello()
        # function is defined above.
        self.button.connect("clicked", self.hello, None)
	self.button1.connect("clicked", self.hello, None)
	self.button2.connect("clicked", self.hello, None)

	self.entry = gtk.Entry()
	self.entry.set_max_length(50)
	#self.entry.connect("activate",self.enter_callback, entry)
	self.entry.set_text("hello")
	self.vbox = gtk.VBox(False, 0)
	self.window.add(self.vbox)
    
        # This will cause the window to be destroyed by calling
        # gtk_widget_destroy(window) when "clicked".  Again, the destroy
        # signal could come from here, or the window manager.
        self.button.connect_object("clicked", gtk.Widget.destroy, self.window)
 	self.button1.connect_object("clicked", self.text_entry_festival, self.window)   
 	self.button2.connect_object("clicked", self.url_festival, self.window)   

	self.box1 = gtk.HBox(False, 0)
	self.window.add(self.box1)
	self.box1.pack_start(self.button1, True, True, 0)
	self.box1.pack_start(self.button2, True, True, 0)
	self.vbox.pack_start(self.entry,True,True,0)
	self.vbox.pack_start(self.box1,True,True,0)
	self.vbox.pack_start(self.button, True, True, 0)
	

	    
        # The final step is to display this newly created widget.
        self.button.show()
        self.button1.show()
        self.button2.show()
	self.entry.show()
	self.box1.show()
	self.vbox.show()
    
        # and the window
        self.window.set_title("festival GUI")
        #self.window.set_icon("/home/vsegers/fun/fesival.png")
        self.window.show()

    def main(self):
        # All PyGTK applications must have a gtk.main(). Control ends here
        # and waits for an event to occur (like a key press or mouse event).
        gtk.main()

# If the program is run directly or passed as an argument to the python
# interpreter then create a HelloWorld instance and show it
if __name__ == "__main__":
    hello = HelloWorld()
    hello.main()


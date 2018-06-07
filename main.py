from kivy.app import App
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label

class Rectangles(FloatLayout):
	
	def __init__(self,**kwargs):
		
		super(Rectangles,self).__init__(**kwargs)
		
		# Title set-up and positioning
		self.title = Label(text='Complete[color=ff3333][b]ME[/b][/color]', markup = True, font_size = '35sp')
		self.add_widget(self.title)
		relativesize_x_title = 0.4  	# size of title label wrt window size (x-coordinate)
		relativesize_y_title = 0.2  	# size of title label wrt window size (y-coordinate)
		self.title.size_hint = (relativesize_x_title,relativesize_y_title)
		self.title.pos_hint = {'x':0.5-relativesize_x_title/2,'y':0.9-relativesize_y_title/2}
		
		# CompleteME Version number 
		self.label2 = Label(text='Version 0.0', font_size = '10sp')
		self.add_widget(self.label2)
		relativesize_x_version = 0.05  	# size of version label wrt window size (x-coordinate)
		relativesize_y_version = 0.05  	# size of version label wrt window size (y-coordinate)
		self.label2.size_hint = (relativesize_x_version,relativesize_y_version)
		self.label2.pos_hint = {'x':0.5-relativesize_x_version/2,'y':0.85-relativesize_y_version/2}
		
		# First button
		self.btn1 = Button(text='Heat Transfer Problem', font_size = '15sp')
		#self.btn1.bind(on_press=self.change1)
		self.add_widget(self.btn1)
		relativesize_x_btn = 0.25  	# size of buttons wrt window size (x-coordinate)
		relativesize_y_btn = 0.125  	# size of buttons wrt window size (y-coordinate)
		self.btn1.size_hint= (relativesize_x_btn, relativesize_y_btn) 	
		self.btn1.pos_hint = {'x':0.5-relativesize_x_btn/2,'y':0.6-relativesize_y_btn/2}
		
		# Second button
		self.btn2 = Button(text='Random Problem', font_size = '15sp')
		#self.btn2.bind(on_press=self.change2)
		self.add_widget(self.btn2)
		self.btn2.size_hint = (relativesize_x_btn, relativesize_y_btn)
		self.btn2.pos_hint = {'x':0.5-relativesize_x_btn/2,'y':0.3-relativesize_y_btn/2}

class MyApp(App):

	def build(self):
		return Rectangles()

if __name__ == '__main__':
    
	MyApp().run()

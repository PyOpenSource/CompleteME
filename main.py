from kivy.app import App
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class Rectangles(GridLayout):
	
	def __init__(self,**kwargs):
	
		super(Rectangles,self).__init__(**kwargs)
		self.cols = 1
		self.rows = 4
		
		self.label1 = Label(text='Complete[color=ff3333][b]ME[/b][/color]', markup = True)
		self.add_widget(self.label1)
		
		self.label2 = Label(text='Version 0.0')
		self.add_widget(self.label2)
		self.label2.size_hint = (0.5,0.5)
		
		self.btn1 = Button(text='Heat Transfer Problem')
		#self.btn1.bind(on_press=self.change1)
		self.add_widget(self.btn1)
		self.btn1.size_hint = (0.5,0.5)
		
		self.btn2 = Button(text='Random Problem')
		#self.btn2.bind(on_press=self.change2)
		self.add_widget(self.btn2)
		

class MyApp(App):

	def build(self):
		return Rectangles()

if __name__ == '__main__':
    
	MyApp().run()

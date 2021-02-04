class Animal:
	def reply(self):
		self.speak()

class Mammal(Animal):
	pass

class Lion(Mammal):
	def speak(self):
		import pyttsx3
		engine = pyttsx3.init()
		engine.say('А я лев - царь зверей рррраврррравррррав смертные! Я повелеваю этим зоопарком. ')
		engine.runAndWait()


class Cat(Mammal):
	def speak(self):
		import pyttsx3
		engine = pyttsx3.init()
		engine.say('А я кот    рррррр   ахахаха   мяу мяу')
		engine.runAndWait()


class Dog(Mammal):
	def speak(self):
		import pyttsx3
		engine = pyttsx3.init()
		engine.say('А я волк   гав гав     Прошу прощения сэр    оуууоууу  ')
		engine.runAndWait()


class Primate(Mammal):
	def speak(self):
		import pyttsx3
		engine = pyttsx3.init()
		engine.say('Хоть я и обезьяна, однако я хочу захватить мир. Ха ха ха ха')
		engine.runAndWait()


class Hacker(Primate):
	def speak(self):
		import pyttsx3
		engine = pyttsx3.init()
		engine.say('Это был зоопарк удивительных животных.  '
		 'Я программа и меня зовут  Джейн.  Я сделана с помощью ООП - Объектно Ориентированного Программирования. '
		 'Если вы не знаете, что это, то можете не беспокоиться, пока я обычная голосовая помощница, но каждый днем я буду улучшаться и расти.'
		 ' Мой создатель Антон Ластухин')
		engine.runAndWait()







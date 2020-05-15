class MyStuff(object):
    def __init__(self):
        self.tangerine = "and now a thousand years between"
    
    def apple(self):
        print("I AM A CLASSY APPLE!")
    
    def orange(self, name):
        print(f"Name is {name}")
    
thing = MyStuff()
thing.apple()
print(thing.tangerine)

stuff = MyStuff()
stuff.orange("Karan")
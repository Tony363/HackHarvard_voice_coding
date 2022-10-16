from classes import *
from transcribe import *

print(camelCase(['car','ride','share']))

v = Class("Vehicle")
v.addAttribute("something", "int")
c = Class("Car", "Vehicle")
c.addAttribute("fla", "float")
c.addMethod("setFla", ["fla", "shmu"])
f = open("car.py", "w")

v.write(f)
c.write(f)
f.close()

pars = Parser()


text = "Class vehicle. Attribute wheels type int. Attribute rubber type str. Method get speed."+\
"Class car. Ducky give me attribute speed type float. Ducky, give me method accelerate parameters rate."+\
    "Class truck inherits vehicle. Attribute mpg type float. Method try hard parameters rate speed look."+\
    "Class car inherits vehicle. method decelerate. Class Ford150 inherits truck. Attribute horsepower type float. "

# pars.parseSentence("Class vehicle.")
# pars.parseSentence("Attribute wheels type int.")
# pars.parseSentence("Class car.")
# print(pars.setCurrent('Vehicle'))
# pars.parseSentence("Ducky give me attribute speed type float.")
# classes = pars.getClasses()
# print(pars.setCurrent("Vehicle"))
# pars.parseSentence("Ducky, give me method vers parameters det fla")
pars.parseText(text)
pars.write()
draw_uml('DuckyProgram.py')
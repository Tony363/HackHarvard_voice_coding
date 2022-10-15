from classes import *

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
print(camelCase(getName(remPunc('Class vehicle.').lower().split(), 'class'), False))


text = "Class vehicle. Attribute wheels type int. Method get speed."+\
"Class car. Ducky give me attribute speed type float. Ducky, give me method accelerate parameters rate."+\
    "Class truck inherits vehicle. Attribute mpg type float. Method try hard parameters rate speed look."+\
    "Class car inherits vehicle. method decelerate. Class Ford150 inherits truck."

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

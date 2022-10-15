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

pars.parseSentence("Class vehicle.")
pars.parseSentence("Attribute wheels type int.")
pars.parseSentence("Class car.")
pars.parseSentence("Ducky give me attribute speed type float.")
pars.parseSentence("Ducky, give me method vers for parameters det fla")
print(pars.getClasses())
pars.write()

from gui.classes import Class, Parser, camelCase
from gui.transcribe import draw_uml


def main() -> None:
    print(camelCase(['car', 'ride', 'share']))

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

    text = "Class CNN. Attribute conv2d type nnConv2d. Attribute fc type nnLinear. Method get forward." +\
        "Class LSTM. Ducky give me attribute lstm type nnModule. Ducky, give me method initialize parameters tensor." +\
        "Class CNNLSTM inherits CNN. Attribute featureExtractor type nnModule. Method forward parameters tensor vocabSize." +\
        "Class Loader inherits DataLoader. method __iter__. Class Data inherits DataSet. Attribute queue type list."

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


if __name__ == "__main__":
    main()

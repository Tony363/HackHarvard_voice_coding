class Class:

    #stdTypes = [t for t in b.__dict__.values()]

    def __init__(self, name=None, inherits=None):
        self.__name = name
        self.__attributes = []
        self.__methods = {}
        self.__inherits = inherits

    def __eq__(self, other):
        return self.__name == str(other)

    def addAttribute(self, name, typ):
        self.__attributes.append((name, typ))

    def addMethod(self, name, *kwargs):
        params = []
        for arg in kwargs:
            params.append(str(arg))
        self.__methods[name] = params

    def setInherits(self, inherits):
        self.__inherits = inherits

    def write(self, file):
        if self.__inherits:
            file.write("class {}({}):\n\n".format(
                self.__name, self.__inherits))
        else:
            file.write("class {}:\n\n".format(self.__name))
        file.write("    def __init__(self):\n")
        for attribute in self.__attributes:
            file.write("        self.{} = {}()\n".format(
                attribute[0], attribute[1]))
        file.write("\n")
        for method in self.__methods:
            st = ""
            for param in self.__methods[method]:
                st += ", "+param
            file.write(
                "    def {}(self{}):\n        pass\n\n".format(method, st))


class Parser:

    keywords = set('class', 'inherits', 'method',
                   'attribute', 'attributes', 'undo')

    def __init__(self, name="DuckyProgram"):
        self.__classes = []
        self.__current = None
        self.__name = name

    def addClass(self, name, inherits=None):
        self.setCurrent(name)
        if self.__current is None:
            new = Class(name)
            if inherits is not None:
                new.setInherits(inherits)
            self.__classes.append(new)
            self.__current = new

    def findClass(self, name):
        for cls in self.__classes:
            if cls == name:
                return cls
        return None

    def setCurrent(self, name):
        self.__current = self.findClass(name)

    def write(self):
        with open(self.__name+'.py', 'w') as f:
            for cls in self.__classes:
                cls.write(f)
            f.close()

    def parseSentence(self, sentence):
        sentence = remPunc(sentence.lower().strip()).split()


def remPunc(sentence):
    punc = '.,!?<>\|()[]{}*$^'
    ans = ''
    for el in sentence:
        if el not in punc:
            ans += el
    return ans


def camelCase(wordls, func=True):
    if len(wordls) == 1:
        return wordls[0]
    elif len(wordls) > 1:
        if func:
            ans = wordls[0]
        else:
            ans = wordls[0].capitalize()
        for i in range(1, len(wordls)):
            ans += wordls[i].capitalize()
        return ans
    return None


def getName(sentence, key):
    if key in sentence:
        i = sentence.index(key)
        ans = []
        for j in range

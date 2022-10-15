import shlex
import subprocess


class SampleCase(object):
    def __init__(self):
        self.name = None
        self.__filename = None

    def __iter__(self):
        return self


class Vehicle:
    def __init__(self):
        self.__something = int()


class Car(Vehicle):

    def __init__(self):
        self.fla = float()

    def setFla(self, fla, shmu):
        # self.__fla = True
        pass


if __name__ == '__main__':
    args = shlex.split('-o png -p example test_uml.py')
    subprocess.call(['pyreverse'] + args)
    # Run(args)

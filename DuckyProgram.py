class Cnn:

    def __init__(self):
        self.conv2d = nnConv2d()
        self.fc = nnLinear()

    def getForward(self):
        pass

class Lstm:

    def __init__(self):
        self.lstm = nnModule()

    def initialize(self, tensor):
        pass

class Cnnlstm(Cnn):

    def __init__(self):
        self.featureextractor = nnmodule()

    def forward(self, tensor, vocabsize):
        pass

class Loader(Dataloader):

    def __init__(self):
      pass

    def __iter__(self):
        pass

class Data(Dataset):

    def __init__(self):
        self.queue = list()


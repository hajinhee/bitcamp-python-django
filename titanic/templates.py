from context.domains import Dataset
from context.models import Model
from titanic import TitanicModel


class TitanicTemplate(object):
    def __init__(self):
        self.model = Model()
        self.dataset = Dataset()
        self.titanic = TitanicModel()



from models import Model
from domains import Dataset


class View:
    model = Model()
    dataset = Dataset()

    def modeling(self, train, test):
        model = self.model

    def preprocess(self, train, test) -> object:
        model = self.model
        this = self.dataset
        this.train = model.new_model(train)
        this.test = model.new_model(test)
        # id 추출
        print(f'트레인 컬럼 {this.train.columns}')  # 속성 값
        print(f'트레인 헤드 {this.train.head()}')  # 메소드 값이라 파라미터존이 있음



from context.domains import Dataset
from context.models import Model
from titanic import TitanicModel
from icecream import ic
import matplotlib.pyplot as plt

'''
데이터 시작화
엔티티(개체)를 차트로 표현하는 것

모든 feature 를 다 그려야 하지만, 시간 관계상 
survived, pclass, sex, embarked 의 4개만 그리겠습니다. 
템플릿 메소드 패턴으로 구성하시오.

'''


class TitanicTemplate(object):
    model = Model()
    dataset = Dataset()

    def __init__(self, train_fname):
        self.entity = self.model.new_model(train_fname)
        this = self.entity
        ic(f'트레인의 타입: {type(this)}')
        ic(f'트레인의 컬럼: {this.columns}')
        ic(f'트레인의 상위 5명: {this.head()}')
        ic(f'트레인의 하위 5명: {this.tail()}')

    def visualize(self) -> None:     # hook 에는 메소드 호출을 제외한 다른 것을 포함하지 않는다.
        this = self.entity
        self.draw_survived(this)
        self.draw_pclass(this)
        self.draw_sex(this)
        self.draw_embarked(this)

    @staticmethod
    def draw_survived(this) -> None:
        f, ax = plt.subplots(1, 2, figsize=(18, 8))
        plt.show(this['Survived'])

    @staticmethod
    def draw_pclass(this) -> None:
        plt.show(this['Pclass'])

    @staticmethod
    def draw_sex(this) -> None:
        plt.show(this['Sex'])

    @staticmethod
    def draw_embarked(this) -> None:
        plt.show(this['Embarked'])










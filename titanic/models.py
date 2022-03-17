from icecream import ic
from context.domains import Dataset
from context.models import Model


class TitanicModel(object):
    model = Model()
    dataset = Dataset()

    def preprocess(self, train_fname, test_fname) -> object:        # Hook : __init__ 과는 결합도를 높이고 나머지 메소드와는 결합도를 낮춘다.
        this = self.dataset
        that = self.model
        this.train = that.new_dframe(train_fname)
        this.test = that.new_dframe(test_fname)
        this.id = this.test['PassengerId']
        this.label = this.train['Survived']
        this.train = this.train.drop('Survived', axis=1)  # axis = 축의 방향, 1=column, 0=row
        this = self.drop_feature(this, 'SibSp', 'Parch', 'Ticket', 'Cabin')
        '''
        this = self.create_train(this)
        this = self.name_nominal(this)
        this = self.age_ratio(this)
        this = self.sex_nominal(this)
        this = self.embarked_nominal(this)
        this = self.pclass_ordinal(this)
        this = self.fare_ratio(this)
        '''
        self.print_this(this)
        return this

    @staticmethod
    def print_this(this):
        print('*'*100)
        ic(f'1. Train 의 타입 : {type(this.train)}\n')        # this.train, this.test, this.id = 객체, property => 앞으로 가공할거라
        ic(f'2. Train 의 컬럼 : {this.train.columns}\n')
        ic(f'3. Train 의 상위 1개 : {this.train.head(1)}\n')   # ()가 있는 건 메소드
        ic(f'4. Train 의 null의 개수 :  {this.train.isnull().sum()}\n')
        ic(f'5. Test 의 타입 {type(this.test)}\n')
        ic(f'6. Test 의 컬럼 {this.test.columns}\n')
        ic(f'7. Test 의 상위 1개 {this.test.head(1)}\n')
        ic(f'8. Test 의 null의 개수 {this.test.isnull().sum()}\n')
        ic(f'9. id 의 타입 {type(this.id[:10])}\n')
        print('*' * 100)

    def create_this(self, dataset) ->object:
        this = dataset
        this.train = self.train  # DF = object
        this.test = self.test    # DF = object
        this.id = self.id        # Series
        return this

    @staticmethod
    def drop_feature(this, *feature) -> object:   # Asterisk(*): 여러 개의 인자 값을 한 번에 받음
        # for i in feature:
        #     this.train.drop(i, axis=1, inplace=True)
        #     this.test.drop(i, axis=1, inplace=True)

        # [i.drop(j, axis=1, inplace=True) for i in [this.train, this.test] for j in feature]
        # inplace: 값을 다시 할당하지 않아도 바로 삭제
        [i.drop(list(feature), axis=1, inplace=True) for i in [this.train, this.test]]
        return this

    @staticmethod
    def create_train(this) -> object:
        return this

    '''
    Categorical vs. Quantitative
    Cate -> nominal(이름) vs. ordinal(순서)
    Quan -> interval(상대적) vs. ratio(절대적)
    '''

    @staticmethod
    def pclass_ordinal(this) -> object:
        return this

    @staticmethod
    def name_nominal(this) -> object:
        return this

    @staticmethod
    def sex_nominal(this) -> object:
        return this

    @staticmethod
    def age_ratio(this) -> object:
        return this

    @staticmethod
    def fare_ratio(this) -> object:
        return this

    @staticmethod
    def embarked_nominal(this) -> object:
        return this

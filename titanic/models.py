import numpy as np
import pandas as pd
from icecream import ic
from context.domains import Dataset
from context.models import Model


class TitanicModel(object):
    model = Model()
    dataset = Dataset()

    def preprocess(self, train_fname, test_fname) -> object:        # Hook : __init__ 과는 결합도를 높이고 나머지 메소드와는 결합도를 낮춘다.
        this = self.dataset
        that = self.model
        feature = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
        this.train = that.new_dframe(train_fname)
        this.test = that.new_dframe(test_fname)
        this.id = this.test['PassengerId']
        this.label = this.train['Survived']
        this.train.drop('Survived', axis=1, inplace=True)  # axis = 축의 방향, 1=column, 0=row
        this = self.drop_feature(this, 'SibSp', 'Parch', 'Ticket', 'Cabin')
        this = self.extract_title_from_name(this)
        title_mapping = self.remove_duplicate(this)
        this = self.title_nominal(this, title_mapping)
        this = self.drop_feature(this, 'Name')
        this = self.sex_nominal(this)
        this = self.drop_feature(this, 'Sex')
        this = self.embarked_nominal(this)
        this = self.age_ratio(this)
        this = self.drop_feature(this, 'Age')
        this = self.fare_ratio(this)
        this = self.drop_feature(this, 'Fare')

        '''
        this = self.create_train(this)
        this = self.create_label(this)
        this = self.name_nominal(this)
        this = self.age_ratio(this)
        this = self.sex_nominal(this)
        this = self.embarked_nominal(this)
        this = self.pclass_ordinal(this)
        this = self.fare_ratio(this)
        '''
        # self.kwargs_sample(name='이순신')
        # self.name_nominal(this)
        self.df_info(this)
        return this

    @staticmethod
    def df_info(this):
        [print(f'{i.info()}') for i in [this.train, this.test]]
        ic(this.train.head(3))
        ic(this.test.head(3))

    @staticmethod
    def null_check(this):
        [ic(f'{i.isnull().sum()}') for i in [this.train, this.test]]

    @staticmethod
    def id_info(this):
        ic(f'id 의 타입  {type(this.id)}')
        ic(f'id 의 상위 3개 {this.id[:3]}')

    @staticmethod
    def print_this(this):
        print('*'*100)
        ic(f'1. Train 의 타입 : {type(this.train)}\n')        # this.train, this.test, this.id = 객체, property => 앞으로 가공할거라
        ic(f'2. Train 의 컬럼 : {this.train.columns}\n')
        ic(f'3. Train 의 상위 1개 : {this.train.head(1)}\n')   # ()가 있는 건 메소드
        ic(f'4. Train 의 null의 개수 : {this.train.isnull().sum()}\n')
        ic(f'5. Test 의 타입 : {type(this.test)}\n')
        ic(f'6. Test 의 컬럼 : {this.test.columns}\n')
        ic(f'7. Test 의 상위 1개 : {this.test.head(1)}\n')
        ic(f'8. Test 의 null의 개수 : {this.test.isnull().sum()}\n')
        ic(f'9. id 의 타입 : {type(this.id[:10])}\n')
        print('*' * 100)

    @staticmethod
    def drop_feature(this, *feature) -> object:  # Asterisk(*): 여러 개의 인자 값을 tuple 형태로 한 번에 받음
        # for i in feature:
        #     this.train.drop(i, axis=1, inplace=True)
        #     this.test.drop(i, axis=1, inplace=True)
        # [i.drop(j, axis=1, inplace=True) for j in feature for i in [this.train, this.test]]

        [i.drop(list(feature), axis=1, inplace=True) for i in [this.train, this.test]]

        return this

    @staticmethod
    def kwargs_sample(**kwargs) -> None:
        ic(type(kwargs))
        {print(''.join(f'key:{i}, val:{j}')) for i, j in kwargs.items()}  # key: name, val: 이순신
    '''
    Categorical vs. Quantitative
    Cate -> nominal(이름) vs. ordinal(순서)
    Quan -> interval(상대적) vs. ratio(절대적)
    '''

    @staticmethod
    def pclass_ordinal(this) -> object:
        return this

    @staticmethod
    def extract_title_from_name(this) -> None:  # train, test => df(object)
        for these in [this.train, this.test]:
            these['Title'] = these.Name.str.extract('([A-Za-z]+)\.', expand=False)  # 정규식
        # ic(this.train.head(5))
        return this

    @staticmethod
    def remove_duplicate(this) -> None:
        a = []
        for these in [this.train, this.test]:
            a += list(set(these['Title']))
        a = list(set(a))
        # print(f'>>> {a}')
        '''
        ['Mr', 'Sir', 'Major', 'Don', 'Rev', 'Countess', 'Lady', 'Jonkheer', 'Dr',
        'Miss', 'Col', 'Ms', 'Dona', 'Mlle', 'Mme', 'Mrs', 'Master', 'Capt']
        Royal : ['Countess', 'Lady', 'Sir']
        Rare : ['Capt','Col','Don','Dr','Major','Rev','Jonkheer','Dona','Mme' ]
        Mr : ['Mlle']
        Ms : ['Miss']
        Master
        Mrs
        '''
        title_mapping = {'Mr': 1, 'Ms': 2, 'Mrs': 3, 'Master': 4, 'Royal': 5, 'Rare': 6}
        return title_mapping

    @staticmethod
    def title_nominal(this, title_mapping) -> object:   # title_mapping 은 외부(preprocess)에 있어서 파라미터로 받음
        for these in [this.train, this.test]:
            these['Title'] = these['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
            these['Title'] = these['Title'].replace(['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer', 'Dona', 'Mme'], 'Rare')
            these['Title'] = these['Title'].replace(['Mlle'], 'Mr')
            these['Title'] = these['Title'].replace(['Miss'], 'Ms')
            # Master 는 변화없음
            # Mrs 는 변화없음
            these['Title'] = these['Title'].fillna(0)  # NaN 값(노동자 계급)을 채우는
            these['Title'] = these['Title'].map(title_mapping)  # 자연어를 기계어로 변환
        return this

    @staticmethod
    def sex_nominal(this) -> object:
        gender_mapping = {'male': 0, 'female': 1}
        for these in [this.train, this.test]:
            these['Gender'] = these['Sex'].map(gender_mapping)
        return this

    @staticmethod
    def age_ratio(this) -> object:
        train = this.train
        test = this.test
        age_mapping = {'Unknown': 0, 'Baby': 1, 'Child': 2, 'Teenager': 3, 'Student': 4,
                       'Young Adult': 5, 'Adult': 6,  'Senior': 7}
        train['Age'] = train['Age'].fillna(-0.5)
        test['Age'] = test['Age'].fillna(-0.5)         # -1 ~ 0 사이의 수로 만들어서 'NaN' => 'Unknown' 만들기 위해
        bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf]  # np.inf
        labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
        for these in train, test:
            these['AgeGroup'] = pd.cut(these['Age'], bins, labels=labels)  # pd.cut() 사용
            these['AgeGroup'] = these['AgeGroup'].map(age_mapping)  # map 사용
        return this

    @staticmethod
    def fare_ratio(this) -> object:
        fare_mapping = {'1등급': 1, '2등급': 2, '3등급': 3, '4등급': 4}
        this.train['Fare'] = this.train['Fare'].fillna(1)
        this.test['Fare'] = this.test['Fare'].fillna(1)
        # print(f'qcut 으로 bins 값 설정 {this.train["FareBand"].head()}')
        # bins = [-0.001, 7.91, 14.454, 31.0, np.inf]
        labels = ['4등급', '3등급', '2등급', '1등급']
        for these in this.train, this.test:
            these['FareBand'] = pd.qcut(these['Fare'], 4, labels=labels)
            these['FareBand'] = these['FareBand'].map(fare_mapping)
        return this

    @staticmethod
    def embarked_nominal(this) -> object:
        embarked_mapping = {'S': 1, 'C': 2, 'Q': 3}
        this.train = this.train.fillna({'Embarked': 'S'})  # test에는 NaN값이 없어서 train에만
        for these in [this.train, this.test]:
            these['Embarked'] = these['Embarked'].map(embarked_mapping)
        return this

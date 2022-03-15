from context.domains import Dataset
import numpy as np
import pandas as pd
import sklearn


class Model:
    def __init__(self):
        self.ds = Dataset()
        this = self.ds
        this.dname = './data/'
        this.sname = './save/'

    def new_model(self, fname) -> object:
        this = self.ds
        # index_col=0 해야 기존 index 값이 유지
        # 0은 컬럼명 중 첫 번째를 의미(배열구조)
        # pd.read_csv('경로/파일명.csv', index_col = '인덱스로 지정할 column명') Index 지정
        return pd.read_csv(f'{this.dname}{fname}', index_col=0)

    def save_model(self, fname, dframe):
        this = self.ds
        '''
        풀옵션은 다음과 같다
        df.to_csv(f'{self.ds.sname}{fname}',sep=',',na_rep='NaN',
                         float_format='%.2f',  # 2 decimal places
                         columns=['ID', 'X2'],  # columns to write
                         index=False)  # do not write index
         '''
        dframe.to_csv(f'{this.sname}{fname}', sep=',', na_rep='NaN')



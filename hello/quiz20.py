import random
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd


class Quiz20:

    def quiz20list(self) -> str:
        list1 = [1, 2, 3, 4]
        print(list1, type(list1))

        print(list1[0], list1[-1], list1[-2], list1[1:3])

        list2 = ['math', 'english']
        print(list2[0])
        print(list2[0][1])

        list3 = [1, '2', [1, 2, 3]]
        print(list3)

        list4 = [1, 2, 3]
        list5 = [4, 5]
        print(list4 + list5)
        print(2 * list4)

        list4.append(list5)
        print(list4)

        list4[-2:] = []
        print(list4)

        a = [1, 2]
        b = [0, 5]
        c = [a, b]
        print(c)
        print(c[0][1])
        c[0][1] = 10
        print(c)

        a = range(10)
        print(a)
        print(sum(a))

        b = [2, 10, 0, -2]
        print(sorted(b))

        b.index(0)
        len(b)
        print(b.index(0), len(b))
        return None


    def quiz21tuple(self) -> str:
        a = (1, 2)
        print(a, type(a))

        a = (1, 2)
        b = (0, (1, 4))
        a + b
        return None

    def quiz22dict(self) -> str:
        a = {'class': ['deep learning', 'machine learning'], 'num_students': [40, 20]}
        type(a)

        a['class']

        a['grade'] = ['A', 'B', 'C']
        a

        a.keys()

        list(a.keys())

        a.values()

        a.items()

        a.get('class')

        'class' in a

        return None

    def quiz23listcom(self) -> str:
        print('--------Legacy--------')
        a = []
        for i in range(5):
            a.append(i)
        print(a)

        print('-----Comprehension-----')
        a2 = [i for i in range(5)]  # range(5) = 0~4
        print(a2)
        return None

    def quiz24zip(self) -> {}:
        url = 'https://music.bugs.co.kr/chart/track/realtime/total'
        html_doc = urlopen(url)
        soup = BeautifulSoup(html_doc, 'lxml')
        ls1 = self.find(soup, 'p', 'title')
        ls2 = self.find(soup, 'p', 'artist')
        # self.dict1(ls1, ls2)
        # self.dict2(ls1, ls2)
        dict = {}
        for i, j in zip(ls1, ls2):
            dict[i] = j
        print(dict)
        return dict

    @staticmethod
    def dict2(ls1, ls2) -> None:
        dict = {}
        for i, j in enumerate(ls1):
            dict[j] = ls2[i]
        print(dict)

    @staticmethod
    def dict1(ls1, ls2) -> None:
        dict = {}
        for i in range(0, len(ls1)):
            dict[ls1[i]] = ls2[i]
        print(dict)

    def print_music_list(self, soup) -> None:
        artists = soup.find_all("p", {'class': 'artist'})
        print(''.join([i.text for i in artists]))
        print(soup.prettify())
        titles = soup.find_all("p", {'class': 'title'})
        titles = [i.text for i in titles]
        print('\n'.join(i.text.strip() for i in titles))

    def find_rank(self, soup) -> None:
        for i, j in enumerate(['artist', 'title']):
            for i, j in enumerate(Quiz20.find(soup, 'p', j)):
                print(f'{i}위: {j}')
        print('#'*100)

    @staticmethod
    def find(soup, tag, cls_name) -> []:
        return [i.text for i in soup.find_all(tag, {'class': cls_name})]

    def quiz25dictcom(self) -> str: return None

    def quiz26map(self) -> str: return None

    def quiz27melon(self) -> {}:
        headers = {'User-Agent': 'Mozilla/5.0'}
        url = 'https://www.melon.com/chart/index.htm?dayTime=2022030816'
        req = urllib.request.Request(url, headers=headers)
        soup = BeautifulSoup(urlopen(req), 'lxml')
        # songs = soup.find_all('div', {'class': 'ellipsis rank01'})
        # songs = [i for i in songs]
        ls1 = self.find(soup, 'div', 'ellipsis rank01')
        ls2 = self.find(soup, 'div', 'ellipsis rank02')
        # self.dict1(ls1, ls2)
        # self.dict2(ls1, ls2)
        dict = {}
        for i, j in zip(ls1, ls2):
            dict[i] = j
        print(dict)
        return dict

    def quiz28dataframe(self) -> None:
        # dict = self.quiz24zip()    # quiz24zip 의 return 타입에 의해 딕셔너리가 됨
        df = pd.DataFrame.from_dict(dict, orient='index')
        print(df)
        df.to_csv('./save/bugs.csv', sep=',', na_rep='NaN')

    def quiz29(self) -> str: return None


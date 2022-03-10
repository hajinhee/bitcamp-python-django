import random
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup


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
        # 맨 앞의 i는 리턴 값
        print(a2)
        return None

    @staticmethod
    def quiz24zip() -> str:
        url = 'https://music.bugs.co.kr/chart/track/realtime/total'
        html_doc = urlopen(url)
        soup = BeautifulSoup(html_doc, 'lxml')  # 'html.parser' -> 'lxml' 로 업데이트
        # artists = soup.find_all("p", {'class': 'artist'})
        # a = ''.join([i.text for i in artists])
        # print(soup.prettify())
        # titles = soup.find_all("p", {'class': 'title'})
        # titles = [i.text for i in titles]
        # print('\n'.join(i.text.strip() for i in titles))
        for i, j in enumerate(['artist', 'title']):
            # ls = [i for i in Quiz20.find(soup, j)]
            print('\n\n\n'.join(i for i in Quiz20.find(soup, j)))
        return None

    @staticmethod
    def find(soup, a) -> str:
        titles = soup.find_all("p", {'class': a})
        titles = [i.text for i in titles]
        return titles

    def quiz25dictcom(self) -> str: return None

    def quiz26map(self) -> str: return None

    def quiz27melon(self) -> str:
        headers = {'User-Agent': 'Mozilla/5.0'}
        url = 'https://www.melon.com/chart/index.htm?dayTime=2022030816'
        req = urllib.request.Request(url, headers=headers)
        soup = BeautifulSoup(urlopen(req), 'lxml')
        songs = soup.find_all('div', {'class': 'ellipsis rank01'})
        songs = [i for i in songs]
        print('\n'.join(i.text.strip() for i in songs))

        return None

    def quiz28(self) -> str:
        a = [i if i == 0 or i == 1 else i for i in range()]  # range() -> 수열(시퀀스)
        b = [i if i == 0 or i == 1 else i for i in []]  # 자료구조(컬렉션) -> []리스트 , ()튜플, {}딕셔너리
        # iterator -> default 값으로 element만 추출
        c = [(i, j) for i, j in enumerate([])]
        # enumeration -> index와 element 2개 추출
        d = ''.join(i.text for i in [])
        return None

    def quiz29(self) -> str: return None


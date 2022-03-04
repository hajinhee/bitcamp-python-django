import random

from hello.domains import myRandom


class Quiz10:

    def quiz10bubble(self) -> str: return None

    def quiz11insertion(self) -> str: return None

    def quiz12selection(self) -> str: return None

    def quiz13quick(self) -> str: return None

    def quiz14merge(self) -> str: return None

    def quiz15magic(self) -> str: return None

    def quiz16zigzag(self) -> str: return None

    def quiz17prime(self) -> str:
        num1 = myRandom(2, 100)
        num2 = myRandom(2, 100)
        prime = []
        count = 0
        for i in range(num1, num2 + 1):
            flag = 1
            for j in range(2, i):
                if i % j == 0:
                    flag = 0
                    break
            if flag == 1:
                prime.append(i)
                count += 1
        print(f'{prime} 총 {count}개 입니다.')
        return None

    def quiz18golf(self) -> str:
        answer = myRandom(1, 100)
        num = myRandom(1, 100)
        count = 0
        while 1:
            count += 1
            if num > answer:
                print('더 작은 값을 입력하세요.')
            elif num < answer:
                print('더 큰 값을 입력하세요.')
            else:
                print(f'{count}번째 시도. 정답입니다.')
        return None

    def quiz19booking(self) -> str: return None
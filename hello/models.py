import random


class Quiz01Calculator:
    def __init__(self, num1, opcode, num2):
        self.num1 = num1
        self.opcode = opcode
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 / self.num2

    def calcRes(self):
        res = 0
        if self.opcode == '+':
            res = self.add()
        elif self.opcode == '-':
            res = self.sub()
        elif self.opcode == '*':
            res = self.mul()
        elif self.opcode == '/':
            res = self.div()
        return f'{self.num1} {self.opcode} {self.num2} = {res}'


class Quiz02Bmi:
    @staticmethod
    def getBmi(member):
        this = member
        b = this.weight / (this.height * this.height) * 10000
        if b >= 35:
            res = '고도 비만'
        elif b >= 30:
            res = '비만'
        elif b >= 25:
            res = '경도 비만'
        elif b >= 23:
            res = '과체중'
        elif b >= 18.5:
            res = '정상'
        else:
            res = '저체중'
        return res


class Quiz03Grade:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    def sum(self):
        return self.kor + self.eng + self.math

    def avg(self):
        return self.sum() / 3

    def getGrade(self):
        if self.avg() >= 80:
            res = '합격'
        else:
            res = '불합격'
        return res


class Quiz04GradeAuto:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    def sum(self):
        return self.kor + self.eng + self.math

    def avg(self):
        return self.sum() / 3

    def getGrade(self):
        pass

    def chkPass(self):
        pass


def myRandom(start, end):
    return random.randint(start, end)


class Quiz05Dice:
    @staticmethod
    def cast():
        return myRandom(1, 6)


class Quiz06RandomGenerator:  # 원하는 범위의 정수에서 램덤값 1개 추출
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def getNumber(self):
        return random.randint(self.start, self.end)


class Quiz07RandomChoice(object):
    def __init__(self):  # 803호에서 랜덤으로 1명 이름 추출
        self.members = ['홍정명', '노홍주', '전종현', '정경준', '양정오',
                        "권혜민", "서성민", "조현국", "김한슬", "김진영",
                        '심민혜', '권솔이', '김지혜', '하진희', '최은아',
                        '최민서', '한성수', '김윤섭', '김승현',
                        "강 민", "최건일", "유재혁", "김아름", "장원종"]

    def chooseMember(self):
        ran = myRandom(1, 24)
        return self.members[ran]


class Quiz08Rps(object):
    def __init__(self, userNumber):
        self.userNumber = userNumber

    def rsp(self):
        com = myRandom(1, 3)
        user = self.userNumber
        arr = ['', '주먹', '가위', '보']
        score = user - com
        if score == -1 or score == 2:
            res = 'You Win'
        elif score == 0:
            res = 'Draw'
        else:
            res = 'You Lose'
        return f'User:{arr[user]} Com:{arr[com]} 결과:{res}'


class Quiz09GetPrime(object):
    def __init__(self):
        self.startNum = 0
        self.endNum = 0

    def get_prime(self):
        self.startNum = int(input('첫 번째 숫자를 입력하세요.'))
        self.endNum = int(input('두 번째 숫자를 입력하세요.'))
        num1 = self.startNum
        num2 = self.endNum
        prime = []
        count = 0

        for i in range(num1, num2+1):
            flag = 1
            for j in range(2, i):
                if i % j == 0:
                    flag = 0
                    break
            if flag == 1:
                prime.append(i)
                count += 1
        return f'{prime} 총 {count}개 입니다.'


class Quiz10LeapYear(object):
    def __init__(self, year):
        self.year = year

    def leapYear(self):
        y = self.year
        if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
            res = f'{y}년은 윤년입니다.'
        else:
            res = f'{y}년은 평년입니다.'
        return res


class Quiz11NumberGolf(object):
    def __init__(self):
        self.num = 0

    def numberGolf(self):
        answer = myRandom(1, 100)
        count = 0
        while 1:
            count += 1
            self.num = int(input('1~100사이의 정수 중 하나를 입력하세요.'))
            if self.num > answer:
                print('더 작은 값을 입력하세요.')
            elif self.num < answer:
                print('더 큰 값을 입력하세요.')
            else:
                return f'{count}번째 시도. 정답입니다. '


class Quiz12Lotto(object):
    def __init__(self):
        self.userNum = []

    def lotto(self):
        print('1~45까지의 숫자 중 6개를 입력하세요.')
        for i in range(6):
            self.userNum.append(int(input(str(i + 1) + '번째 숫자를 입력하세요.')))
        self.userNum.sort()  # 오름차순으로 정리

        lottoNum = []  # 당첨 번호 저장 리스트
        '''ran = set()  # 중복 값 삭제
        while len(ran) < 6:  # 문자열의 길이가 6개가 될 때까지
            ran.add(myRandom(1, 45))  # 중복 값을 제거하고 빈 공간에 6개 값이 모두 찰 때까지 랜덤 값 추가
            lottoNum = list(ran)  # 중복 없이 추출된 6개 숫자 리스트를 lottoNum에 저장'''
        while 1:
            ran = random.randint(1, 45)  # 1~45까지의 랜덤 값
            if ran not in lottoNum:  # 중복 값이 있는 지 확인
                lottoNum.append(ran)  # 추출된 랜덤 값이 lottoNum에 없으면 추가
            if len(lottoNum) == 6:  # lottoNum이 6이 되면 break
                break
        self.userNum.sort()  # 오름차순으로 정리

        lottoNum.sort()  # 오름차순으로 정리
        count = 0
        for i in range(6):
            for j in range(6):
                if self.userNum[i] == lottoNum[j]:
                    count += 1
        if count == 6:
            res = '1등 당첨입니다.'
        elif count == 5:
            res = '2등 당첨입니다.'
        elif count == 4:
            res = '3등 당첨입니다.'
        else:
            res = '낙첨입니다.'
        return f'선택 번호:{self.userNum}\n당첨 번호:{lottoNum}\n{count}개 {res}'


class Quiz13Bank(object):  # 이름, 입금, 출금만 구현
    def __init__(self):
        self.total = 0

    def save(self, money):
        self.total += money

    def withdraw(self, money):
        if money > self.total:
            print('잔고가 부족합니다.')
            return
        self.total -= money

    def bank(self):
        while 1:
            menu = int(input('0.Exit 1.입금 2.출금 3.잔고 확인'))
            if menu == 0:
                return
            elif menu == 1:
                self.save(int(input('입금할 금액을 입력하세요')))
            elif menu == 2:
                self.withdraw(int(input('출금할 금액을 입력하세요')))
            elif menu == 3:
                print(f'잔고: {self.total}원')


class Quiz14Gugudan(object):  # 책받침 구구단
    def __init__(self):
        pass



import random


def main():
    while 1:
        menu = input('0.Exit 1.계산기 2.BMI 3.성적표 4.성적표(Auto) '
                     '5.주사위 6.랜덤숫자 7.랜덤이름 8.가위바위보')
        if menu == '0':
            break
        elif menu == '1':
            q1 = Quiz01Calculator(int(input('첫 번째 숫자')), input('연산자'), int(input('두 번째 숫자')))
            print(f'{q1.num1} {q1.opcode} {q1.num2} = {q1.calcRes()}')
        elif menu == '2':
            q2 = Quiz02Bmi(input('이름'), int(input('키')), int(input('몸무게')))
            print(f'이름: {q2.name} 키: {q2.height} 몸무게: {q2.weight} BMI 지수: {q2.getBmi()}')
        elif menu == '3':
            q3 = Quiz03Grade(input('이름'), int(input('국어 점수')), int(input('영어 점수')), int(input('수학 점수')))
            print(f'이름:{q3.name} 합계:{q3.sum()} 평균:{q3.avg():.2f} {q3.getGrade()}입니다.')
        elif menu == '4':
            q4 = Quiz04GradeAuto(input('이름'), int(input('국어 점수')), int(input('영어 점수')), int(input('수학 점수')))
            for i in ['김지혜', '심민혜', '권솔이', '최은아', '하진희']:
                print(i)
        elif menu == '5':
            print(f'결과: {Quiz05Dice.cast()}')
        elif menu == '6':
            q6 = Quiz06RandomGenerator(int(input('첫 숫자')), int(input('끝 숫자')))
            print(f'결과: {q6.getNumber()}')
        elif menu == '7':
            q7 = Quiz07RandomChoice()
            print(q7.chooseMember())
        elif menu == '8':
            q8 = Quiz08Rps(int(input('1.주먹 2.가위 3.보')))
            print(q8.rsp())
        elif menu == '9':
            pass
        elif menu == '10':
            pass
        elif menu == '11':
            pass
        elif menu == '12':
            print(Quiz12Lotto.lotto())
        else:
            print('Wrong Number')


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
        if self.opcode == '+':
            return self.add()
        elif self.opcode == '-':
            return self.sub()
        elif self.opcode == '*':
            return self.mul()
        elif self.opcode == '/':
            return self.div()


class Quiz02Bmi:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def getBmi(self):
        b = self.weight / (self.height * self.height) * 10000
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
        return f'이름 {self.name}'


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
        comNumber = myRandom(1, 3)
        score = self.userNumber - comNumber
        if score == -1 or score == 2:
            res = '사용자 승'
        elif score == 0:
            res = '무승부'
        else:
            res = '사용자 패'
        return res


class Quiz09GetPrime(object):
    def __init__(self):
        pass


class Quiz10LeapYear(object):
    def __init__(self):
        pass


class Quiz11NumberGolf(object):
    def __init__(self):
        pass


class Quiz12Lotto(object):
    @staticmethod
    def lotto():
        for i in range(6):
            comNumber = random.randrange(1, 45)
            userNumber = random.randrange(1, 45)
            print(comNumber)
        return


class Quiz13Bank(object):  # 이름, 입금, 출금만 구현
    def __init__(self):
        pass


class Quiz14Gugudan(object):  # 책받침 구구단
    def __init__(self):
        pass


if __name__ == '__main__':
    main()

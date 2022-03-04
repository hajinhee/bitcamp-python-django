from hello import Member
from hello.domains import my100, myRandom, members


class Quiz00:
    def quiz00calculator(self) -> float:
        a = my100()
        b = my100()
        o = ['+', '-', '*', '/', '%']
        op = o[myRandom(0, 4)]
        if op == '+':
            res = f'{a} + {b} = {self.add(a, b)}'
        elif op == '-':
            res = f'{a} - {b} = {self.sub(a, b)}'
        elif op == '*':
            res = f'{a} * {b} = {self.mul(a, b)}'
        elif op == '/':
            res = f'{a} / {b} = {self.div(a, b)}'
        else:
            res = f'{a} % {b} = {self.mod(a, b)}'
        print(res)
        return None

    def add(self, a, b) -> float:
        return a + b

    def sub(self, a, b) -> float:
        return a - b

    def mul(self, a, b) -> float:
        return a * b

    def div(self, a, b) -> float:
        return a / b

    def mod(self, a, b) -> float:
        return a % b


    def quiz01bmi(self):
        this = Member()
        this.name = members()[myRandom(0, 23)]
        this.height = myRandom(150, 200)
        this.weight = myRandom(50, 100)
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
        print(f'이름: {this.name} 키: {this.height} 몸무게: {this.weight} BMI 지수: {res}')
        return None

    def quiz02dice(self):
        print(f'랜덤주사위 결과: {myRandom(1, 6)}')
        return None

    def quiz03rps(self):
        # 1 가위 2  바위 3 보
        user = myRandom(1, 3)
        com = myRandom(1, 3)
        arr = ['', '주먹', '가위', '보']
        score = user - com
        res = '무승부' if score == 0 else '승리' if score == -1 or score == 2 else '패배'
        print(f'플레이어:{arr[user]}, 컴퓨터:{arr[com]}, 결과:{res}')
        return None

    def quiz04leap(self):
        y = myRandom(1, 5000)
        print(f'{y}년은 윤년입니다.' if y % 4 == 0 and y % 100 != 0 or y % 400 == 0 else f'{y}년은 평년입니다.')
        return None

    def quiz05grade(self):
        name = members()[myRandom(0, 23)]
        kor = myRandom(0, 100)
        eng = myRandom(0, 100)
        math = myRandom(0, 100)
        sum = self.sum(kor, eng, math)
        avg = self.avg(sum)
        passChk = self.passChk(avg)
        print(f'이름:{name} 합계:{sum} 평균:{avg:.2f} {passChk}입니다.')
        return None

    def sum(self, kor, eng, math):
        return kor + eng + math

    def avg(self, sum):
        return sum / 3

    def passChk(self, avg):  # 60점이상이면 합격
        return '합격' if avg >= 60 else '불합격'


    def quiz06memberChoice(self):
        print(members()[(myRandom(0, 23))])
        return None

    def quiz07lotto(self):
        '''ran = set()  # 중복 값 삭제
        while len(ran) < 6:  # 문자열의 길이가 6개가 될 때까지
            ran.add(myRandom(1, 45))  # 중복 값을 제거하고 빈 공간에 6개 값이 모두 찰 때까지 랜덤 값 추가
            lottoNum = list(ran)  # 중복 없이 추출된 6개 숫자 리스트를 lottoNum에 저장'''
        lottoNum = []
        while 1:
            ran = myRandom(1, 45)  # 1~45까지의 랜덤 값
            if ran not in lottoNum:  # 중복 값이 있는 지 확인
                lottoNum.append(ran)  # 추출된 랜덤 값이 lottoNum에 없으면 추가
            if len(lottoNum) == 6:  # lottoNum이 6이 되면 break
                break
        lottoNum.sort()
        userNum = []
        while 1:
            u = myRandom(1, 45)  # 1~45까지의 랜덤 값
            if u not in userNum:  # 중복 값이 있는 지 확인
                userNum.append(u)  # 추출된 랜덤 값이 lottoNum에 없으면 추가
            if len(userNum) == 6:  # lottoNum이 6이 되면 break
                break
        userNum.sort()
        count = 0
        for i in range(6):
            for j in range(6):
                if userNum[i] == lottoNum[j]:
                    count += 1
        if count == 6:
            res = '1등 당첨입니다.'
        elif count == 5:
            res = '2등 당첨입니다.'
        elif count == 4:
            res = '3등 당첨입니다.'
        else:
            res = '낙첨입니다.'
        print(f'선택 번호:{userNum}\n당첨 번호:{lottoNum}\n{count}개 {res}')
        return None


    def quiz08bank(self):  # 이름, 입금, 출금만 구현
        name = members()[myRandom(0, 23)]
        money = myRandom(5000, 100000)
        total = myRandom(50000, 1000000)
        while 1:
            menu = int(input('1.입금 2.출금'))
            if menu == 1:
                res = f'이름:{name}\n{self.save(total, money)}'
            elif menu == 2:
                res = f'이름:{name}\n{self.withdraw(total, money)}'
            else:
                break
            print(res)
        return None

    def save(self, total, money):
        total += money
        return f'입금액:{money} 잔고:{total}'

    def withdraw(self, total, money):
        if money > total:
            res = f'잔고:{total} 잔고가 부족합니다.'
        else:
            total -= money
            res = f'출금액:{money} 잔고:{total}'
        return res


    def quiz09gugudan(self):  # 책받침구구단
        for i in range(2, 10, 4):
            for j in range(1, 10):
                for k in range(i, i + 4):
                    print(f'{k}*{j}={k * j}', end='\t')
                print()
            print('\n')

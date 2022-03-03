from hello.domains import Member
from hello.models import Quiz01Calculator, Quiz02Bmi, Quiz03Grade, Quiz04GradeAuto, Quiz05Dice, Quiz06RandomGenerator, \
    Quiz07RandomChoice, Quiz08Rps, Quiz10LeapYear, Quiz11NumberGolf, Quiz12Lotto, Quiz13Bank, Quiz09GetPrime

if __name__ == '__main__':
    while 1:
        menu = input('0.Exit\n'
                     '1.계산기\n'
                     '2.BMI\n'
                     '3.성적표\n'
                     '4.성적표(Auto)\n'
                     '5.주사위\n'
                     '6.랜덤숫자\n'
                     '7.랜덤이름\n'
                     '8.가위바위보\n'
                     '9.소수구하기\n'
                     '10.윤년/평년\n'
                     '11.숫자 맞추기\n'
                     '12.로또\n'
                     '13.은행\n'
                     '14.구구단\n')
        if menu == '0':
            break
        elif menu == '1':
            q1 = Quiz01Calculator(int(input('첫 번째 숫자')), input('연산자'), int(input('두 번째 숫자')))
            print(q1.calcRes())
        elif menu == '2':
            q2 = Quiz02Bmi()
            member = Member()
            member.name = input('이름: ')
            member.height = float(input('키: '))
            member.weight = float(input('몸무게: '))
            res = q2.getBmi(member)
            print(f'이름: {member.name} 키: {member.height} 몸무게: {member.weight} BMI 지수: {res}')
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
            q9 = Quiz09GetPrime()
            print(q9.get_prime())
        elif menu == '10':
            q10 = Quiz10LeapYear(int(input('연도를 입력하세요.')))
            print(q10.leapYear())
        elif menu == '11':
            print(Quiz11NumberGolf().numberGolf())
        elif menu == '12':
            print(Quiz12Lotto().lotto())
        elif menu == '13':
            q13 = Quiz13Bank()
            print(q13.bank())
        else:
            print('Wrong Number')

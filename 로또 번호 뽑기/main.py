from itertools import count
import random

lotto_num = [] # 로또 번호 리스트

def getRandomNumber():
    number = random.randint(1,45)
    return number

count = 1 # 횟수 저장 변수

while True: #숫자 뽑기
    if count > 6:                       # 뽑은 숫자가 6개라면
        break                           #탈출   
    random_number = getRandomNumber()   #로또 번호 뽑기
    if random_number in lotto_num:      #로또 번호가 겹치면 
        continue                        # 다시 돌리기
    else:                               #로또 번호가 겹치지 않으면 
        lotto_num.append(random_number) # 리스트에 로또 번호를 넣기
        count+=1  
print("이번 회차 로또 번호는" , lotto_num ,"입니다")
import time 

Start = input("Enter를 누르면 타이머가 시작합니다")
begin = time.time() 

Stop = input("Enter를 누르면 타이머가 종료됩니다")
end = time.time()

result = end - begin

result = round(result, 3)
print("시작 후", result, "초의 시간이 흘렀습니다")  

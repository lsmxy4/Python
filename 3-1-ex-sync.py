import time

def cook_ramen(customer,cook_time):
    print(f"손님 {customer} 주문 접수")
    print(f"손님 {customer} 라면 끓이는 중...")

    time.sleep(cook_time)
    print(f"{cook_time}초 대기")
    print(f"손님 {customer} 라면 완성")

def main():
    cook_ramen("A",5)
    cook_ramen("B",4)
    cook_ramen("C",3)

start = time.time()

main()

end = time.time()

print(f"전체 걸린 시간: 약{end - start:.2f}초")

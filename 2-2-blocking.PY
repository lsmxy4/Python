import time

def blocking_tast(name,seconds):
    print(f"{name} 시작")
    time.sleep(seconds)
    print(f"{name} 끝")

print("========blocking 방식========")

start = time.time()

blocking_tast("작업 1",3)
blocking_tast("작업 2",2)

end = time.time()

print(f"총 걸린 시간 : {end - start :.2f}초")
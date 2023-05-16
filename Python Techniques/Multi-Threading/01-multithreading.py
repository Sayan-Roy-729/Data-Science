from concurrent.futures import ThreadPoolExecutor
import threading
import time

# Indicates some task being performed
def func(seconds):
    print(f"Sleeping for {seconds} second(s)...")
    time.sleep(seconds)
    return f"Done sleeping for {seconds} second(s)..."

def main():
    # time1 = time.perf_counter()
    # # Normal function call
    # func(4)
    # func(2)
    # func(1)
    # time2 = time.perf_counter()
    # print(f"Normal function call took {time2 - time1} second(s)")

    time3 = time.perf_counter()
    # Same function call using threads
    t1 = threading.Thread(target=func, args=[4])
    t2 = threading.Thread(target=func, args=[2])
    t3 = threading.Thread(target=func, args=[1])

    t1.start()  # start the thread
    t2.start()  # start the thread
    t3.start()  # start the thread

    t1.join()  # wait for t1 to finish
    t2.join()  # wait for t2 to finish
    t3.join()  # wait for t3 to finish

    time4 = time.perf_counter()
    print("Threading took", time4 - time3, "second(s)")


def pooling_demo():
    with ThreadPoolExecutor() as executor:
        future1 = executor.submit(func, 3)

        future2 = executor.submit(func, 2)

        future3 = executor.submit(func, 4)

        print(future1.result())
        print(future2.result())
        print(future3.result())

def pooling_demo2():
    with ThreadPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = executor.map(func, secs)

        for result in results:
            print(result)


if __name__ == "__main__":
    # main()
    # pooling_demo()
    pooling_demo2()
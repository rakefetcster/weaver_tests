import test_website
import datetime
import time


def main():
    test_dict={}
    for i in range(10):
        start_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Test {i + 1} starting at {start_time}")
        test_dict[i + 1] = start_time
        test_website.end_to_end()
        time.sleep(30)
    print(test_dict)


if __name__ == "__main__":
    main()

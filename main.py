from executor import *


class Perform:
    @staticmethod
    def perform_task1():
        executor = Executor()
        executor.task1()

    @staticmethod
    def perform_task2():
        executor = Executor()
        executor.task2()

    @staticmethod
    def perform_task3():
        executor = Executor()
        executor.task3()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("TRANSACTION 1:")
    Perform.perform_task1()
    print("TRANSACTION 2:")
    Perform.perform_task2()
    print("TRANSACTION 3:")
    Perform.perform_task3()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

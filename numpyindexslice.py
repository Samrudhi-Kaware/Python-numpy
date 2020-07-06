import numpy as np


def function1():
    a1 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

    # indexing
    print(f"a1[0] = {a1[0]}")
    print(f"a1[-10] = {a1[-10]}")

    print(f"a1[9] = {a1[9]}")
    print(f"a1[-1] = {a1[-1]}")


# function1()


def function2():
    a1 = np.array([10, 20, 30, 40, 50])

    # indexing

    # 10, 20, 30, 40
    print(f"a1[[0, 1, 2, 3]] = {a1[[0, 1, 2, 3]]}")

    # 20, 30, 40
    print(f"a1[[1, 2, 3]] = {a1[[1, 2, 3]]}")
    print(f"a1[[-4, -3, -2]] = {a1[[-4, -3, -2]]}")
    print(f"a1[[False, True, True, True, False]] = {a1[[False, True, True, True, False]]}")

    # 20, 40
    print(f"a1[[1, 3]] = {a1[[1, 3]]}")
    print(f"a1[[-4, -2]] = {a1[[-4, -2]]}")
    print(f"a1[[False, True, False, True, False]] = {a1[[False, True, False, True, False]]}")


# function2()


def function3():
    a1 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

    # slicing

    # 20, 30, 40, 50
    print(f"a1[1:5] = {a1[1:5]}")

    # 10, 20, 30, 40, 50
    print(f"a1[0:5] = {a1[0:5]}")
    print(f"a1[:5] = {a1[:5]}")

    # 70, 80, 90, 100
    print(f"a1[6:10] = {a1[6:10]}")
    print(f"a1[6:] = {a1[6:]}")

    # all the values
    print(f"a1 = {a1}")
    print(f"a1[0:10] = {a1[0:10]}")
    print(f"a1[:] = {a1[:]}")


# function3()


def function4():
    a1 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

    # broadcast operators
    print(f"a1 > 40 = {a1 > 40}")
    print(f"a1 >= 40 = {a1 >= 40}")
    print(f"a1 < 40 = {a1 < 40}")
    print(f"a1 <= 40 = {a1 <= 40}")


# function4()


def function5():
    a1 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

    # filtering
    print(f"a1[a1 > 40] = {a1[a1 > 40]}")

    values_gt_40 = list(filter(lambda x: x > 40, a1))
    print(f"values_gt_40 = {values_gt_40}")

    print([x for x in a1 if x > 40])

    print(f"-" * 30)

    print(f"a1[a1 < 50] = {a1[a1 < 50]}")

    values_lt_50 = list(filter(lambda x: x < 50, a1))
    print(f"values_lt_50 = {values_lt_50}")

    print([x for x in a1 if x < 50])

function5()



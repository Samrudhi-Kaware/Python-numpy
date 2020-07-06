import numpy as np


def function1():
    # a1 = np.array([10, 20, 30, 40, 50])

    a1 = np.array([0, 0, 0, 0, 0])
    print(f"a1 = {a1}")

    a2 = np.zeros(5)
    print(f"a2 = {a2}")

    a3 = np.zeros(5, dtype=np.int8)
    print(f"a3 = {a3}")

    a4 = np.zeros([4, 4], dtype=np.int8)
    print(f"a4 = {a4}")


# function1()


def function2():
    values = (1, 1, 1, 1, 1)
    a1 = np.array(values)
    print(f"a1 = {a1}")

    a2 = np.ones(5, dtype=np.int8)
    print(f"a2 = {a2}")

    shape = (4, 4)
    a3 = np.ones(shape, dtype=np.int8)
    print(f"a3 = {a3}")


# function2()


def function3():
    # 1 0 0
    # 0 1 0
    # 0 0 1

    a1 = np.array([
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ])
    print(f"a1 = {a1}")

    a2 = np.eye(3, dtype=np.int8)
    print(f"a2 = {a2}")

    a3 = np.eye(9, dtype=np.int8)
    print(f"a3 = {a3}")


# function3()


def function4():
    random_1 = np.random.randint(80, 100, size=(12))
    print(f"random_1 = {random_1}")
    print(f"n dim = {random_1.ndim}")
    print(f"shape = {random_1.shape}")

    print("-" * 40)

    a1 = random_1.reshape((4, 3))
    print(f"a1 = {a1}")

    print("-" * 40)

    a2 = random_1.reshape((3, 4))
    print(f"a2 = {a2}")

    print("-" * 40)

    a3 = random_1.reshape((2, 2, 3))
    print(f"n dim = {a3.ndim}")
    print(f"a3 = {a3}")


function4()
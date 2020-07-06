
# import the package
import numpy as np

def function1():
    # list
    l1 = [10, 20, 30, 40, 50, 60]
    print(f"l1 = {l1}, type = {type(l1)}")

    # array
    # - memory will get allocated contiguously
    # - flat list
    # - collection of same typed values
    a1 = np.array([10, 20, 30, 40, 50, 60])
    print(f"a1 = {a1}, type = {type(a1)}")
# function1()


def function2():
    # list
    l1 = [
        [10, 20, 30],
        [40, 50, 60]
    ]
    print(f"l1 = {l1}, type = {type(l1)}")
    print(f"l1[0][0] = {l1[0][0]}")

    print("-" * 40)

    # array
    a1 = np.array([
        [10, 20, 30],
        [40, 50, 60]
    ])
    print(f"a1 = {a1}, type = {type(a1)}")
    print(f"a1[0][0] = {a1[0][0]}")


# function2()

def function3():
    # single dimensional
    a1 = np.array([10, 20, 30, 40, 50, 60])
    print(f"a1 = {a1}")
    print(f"data type = {a1.dtype}")
    print(f"count = {a1.size}")
    print(f"memory size of every value = {a1.itemsize}")
    print(f"total memory size = {a1.nbytes}")
    print(f"n dimensions = {a1.ndim}")
    print(f"shape = {a1.shape}")

    print("-" * 40)

    a2 = np.array([
        [10, 20, 30],
        [40, 50, 60]
    ])
    print(f"a1 = {a2}")
    print(f"data type = {a2.dtype}")
    print(f"count = {a2.size}")
    print(f"memory size of every value = {a2.itemsize}")
    print(f"total memory size = {a2.nbytes}")
    print(f"n dimensions = {a2.ndim}")
    print(f"shape = {a2.shape}")

    print("-" * 40)

    a3 = a2.reshape([3, 2])
    print(f"a3 = {a3}")
    print(f"data type = {a3.dtype}")
    print(f"count = {a3.size}")
    print(f"memory size of every value = {a3.itemsize}")
    print(f"total memory size = {a3.nbytes}")
    print(f"n dimensions = {a3.ndim}")
    print(f"shape = {a3.shape}")


# function3()


def function4():
    l1 = ["india", 10, 30, "True", True, False, 45.6]
    print(f"l1 = {l1}, type = {type(l1)}")
    for value in l1:
        print(f"value = {value}, type = {type(value)}")

    print("-" * 40)
    a1 = np.array(["india", 10, 30, "True", True, False, 45.6])
    print(f"a1 = {a1}, type = {type(a1)}")
    print(f"data type of every element in a1 = {a1.dtype}")


function4()
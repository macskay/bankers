#-*- encoding: utf-8 -*-

from bankers.deadlock import Deadlock


def deadlock():
    resource_vector = [1, 2, 1, 3]
    d = Deadlock()
    d.requirements = [[1, 0, 0, 0], [0, 0, 1, 0], [1, 2, 1, 3]]
    d.occupancies = [[0, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 0]]
    d.set_resource_rest_vector(resource_vector)
    print("Deadlock in first dataset? {0}".format(d.find_deadlock()))

def no_deadlock():
    resource_vector = [2, 2]
    d = Deadlock()
    d.occupancies = [[0, 1], [1, 0], [1, 0], [0, 1]]
    d.requirements = [[1, 0], [0, 0], [0, 1], [0, 0]]
    d.set_resource_rest_vector(resource_vector)
    print("Deadlock in first dataset? {0}".format(d.find_deadlock()))

def main():
    deadlock()
    no_deadlock()

if __name__ == '__main__':
    main()

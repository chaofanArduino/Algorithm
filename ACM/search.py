# -*- coding:utf-8 -*-


import random


class Searcher:
    def __init__(self):
        pass

    def __str__(self):
        pass

    @staticmethod
    def sequential_search(key, lists):
        for index in range(0, len(lists)):
            if key == lists[index]:
                return index
        return None

    @staticmethod
    def binary_search(key, lists):
        pass
    pass


if __name__ == '__main__':
    list_int = [random.randrange(10) for i in range(0, 10)]
    print(list_int)
    index = Searcher.sequential_search(5, list_int)
    print(index)
    if index is None:
        print('There is no element which is equal to {}'.format(5))
    else:
        print(list_int[index])
    pass

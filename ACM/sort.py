import random


class Sorter:
    def __init__(self):
        pass

    def __str__(self):
        pass

    @staticmethod
    def bubble_sort(lists):
        count = len(lists)
        for i in range(0, count):
            for j in range(0, count - i - 1):
                if lists[j + 1] < lists[j]:
                    lists[j + 1], lists[j] = lists[j], lists[j + 1]
        return lists

    @staticmethod
    def simple_selection_sort(lists):
        count = len(lists)
        for i in range(0, count):
            min_index = i
            for j in range(i + 1, count):
                if lists[min_index] > lists[j]:
                    min_index = j
            lists[i], lists[min_index] = lists[min_index], lists[i]
        pass


if __name__ == '__main__':
    list_int = [random.randrange(10000) for i in range(0, 10)]
    print(list_int)
    Sorter.bubble_sort(list_int)
    # Sorter.simple_selection_sort(list_int)
    print(list_int)
    pass

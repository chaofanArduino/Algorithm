# -*- coding:utf-8 -*-

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
        return lists

    @staticmethod
    def straight_insertion_sort(lists):
        count = len(lists)
        for i in range(1, count):
            index = None
            for j in range(i - 1, -1, -1):
                if lists[i] < lists[j]:
                    index = j
            if index is not None:
                temp = lists[i]
                for k in range(i, index, -1):
                    lists[k] = lists[k - 1]
                lists[index] = temp
        return lists

    @staticmethod
    def __quick_sort(lists, left_index, right_index):
        if left_index > right_index:
            return lists
        low = left_index
        high = right_index
        key = lists[left_index]
        while right_index > left_index:
            while lists[right_index] >= key and left_index < right_index:
                right_index -= 1
            lists[left_index] = lists[right_index]
            while lists[left_index] <= key and left_index < right_index:
                left_index += 1
            lists[right_index] = lists[left_index]
        lists[right_index] = key
        Sorter.__quick_sort(lists, low, right_index - 1)
        Sorter.__quick_sort(lists, left_index + 1, high)
        return lists

    @staticmethod
    def quick_sort(lists):
        return Sorter.__quick_sort(lists, 0, len(lists) - 1)


if __name__ == '__main__':
    list_int = [random.randrange(10000) for i in range(0, 10)]
    print(list_int)
    # Sorter.bubble_sort(list_int)
    # Sorter.simple_selection_sort(list_int)
    # Sorter.straight_insertion_sort(list_int)
    Sorter.quick_sort(list_int)
    print(list_int)
    pass

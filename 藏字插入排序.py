from utils import loader, generator_text, generator_code
import random
import time
from TibetanWord import TibetanWord


def insert_sort(data):
    """
    :param data: list<TibetanWord>. default size: [18786, 8]
    :return: just do reference operation
    """
    for i in range(2, len(data)):
        if data[i] < data[i - 1]:
            data[0] = data[i]
            j = i
            while data[0] < data[j-1]:
                data[j] = data[j - 1]
                j -= 1
            data[j] = data[0]


def insert_sort_reverse(data):
    for i in range(2, len(data)):
        if data[i] > data[i - 1]:
            data[0] = data[i]
            j = i
            while data[0] > data[j-1]:
                data[j] = data[j - 1]
                j -= 1
            data[j] = data[0]


if __name__ == '__main__':
    load_path = './藏字生成18785_编码.txt'
    output_text_path = './藏字生成ascending_text.txt'
    output_code_path = './藏字生成ascending_code.txt'

    data_A = loader(load_path)
    for word in data_A:
        word.creat_cmp_data()

    arr = [TibetanWord(), ] + data_A
    start = time.time()
    insert_sort(arr)
    end = time.time()
    runTime = end - start
    print("运行时间：", runTime, "秒")
    data_B = arr[1:]
    generator_text(data_B, output_text_path)
    generator_code(data_B, output_code_path)
    """
    第二次实验
    """
    start = time.time()
    insert_sort(arr)
    end = time.time()
    runTime = end - start
    print("运行时间：", runTime, "秒")
    """
    第三次实验
    """
    output_text_path = './藏字生成descending_text.txt'
    output_code_path = './藏字生成descending_code.txt'
    start = time.time()
    insert_sort_reverse(arr)
    end = time.time()
    runTime = end - start
    print("运行时间：", runTime, "秒")
    data_B = arr[1:]
    generator_text(data_B, output_text_path)
    generator_code(data_B, output_code_path)


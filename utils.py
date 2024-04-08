from copy import deepcopy
from TibetanWord import TibetanWord


def loader(file_path='./藏字生成18785_编码.txt'):
    """

    :param file_path: string
    :return: list<TibetanWord>
    """
    res = []
    f = open(file_path, 'r+', encoding='utf-8')
    line = f.readline()
    while line:
        temp_word = TibetanWord(eval(line))
        res.append(temp_word)
        line = f.readline()
    f.close()
    return res


def generator_text(data, file_path):
    """

    :param data: list<TibetanWord>
    :param file_path: string
    :return:
    """
    f = open(file_path, 'w', encoding='utf-8')
    for i in range(len(data)):
        f.write(data[i].get_word())
        f.write("\n")
    f.close()


def generator_code(data, file_path):
    """

    :param data: list<TibetanWord>
    :param file_path: string
    :return:
    """
    f = open(file_path, 'w', encoding='utf-8')
    for i in range(len(data)):
        f.write(str(data[i].data))
        f.write("\n")
    f.close()


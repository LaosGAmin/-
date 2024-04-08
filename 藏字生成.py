from copy import deepcopy
from TibetanWord import TibetanWord
import tables


def top_mid():
    up_table = tables.up_table
    word = []
    for i in range(len(up_table)):
        for j in range(len(up_table[i])-1):
            temp_word = TibetanWord()
            temp_word.data[1] = up_table[i][0]
            temp_word.data[2] = up_table[i][j+1] + 80
            word.append(temp_word)

    print(len(word))
    return word


def mid_down():
    down_table = tables.down_table
    word = []
    for i in range(len(down_table)):
        for j in range(len(down_table[i]) - 1):
            temp_word = TibetanWord()
            temp_word.data[2] = down_table[i][j + 1]
            temp_word.data[3] = down_table[i][0] + 80
            word.append(temp_word)

    print(len(word))
    return word


def mid_down_special():
    # 某一个具体下加字可能会作为再下加字
    # down_table_special的后三行各表示一个字, 每一行第二列为基字，第三列为下加字，第一列为再下加字
    down_table_special = tables.down_table_special
    word = []
    for i in range(len(down_table_special[0]) - 1):
        temp_word = TibetanWord()
        temp_word.data[2] = down_table_special[0][i + 1]
        temp_word.data[3] = down_table_special[0][0] + 80
        word.append(temp_word)

    for j in range(1, 4):
        temp_word = TibetanWord()
        temp_word.data[2] = down_table_special[j][1]
        temp_word.data[3] = down_table_special[j][2] + 80
        temp_word.data[4] = down_table_special[j][0] + 80
        word.append(temp_word)

    print(len(word))
    return word


def top_mid_down():
    # 三重字符
    triple_word = tables.triple_word
    word = []
    for i in range(len(triple_word)):
        for j in range(len(triple_word[i]) - 2):
            temp_word = TibetanWord()
            temp_word.data[1] = triple_word[i][0]
            temp_word.data[2] = triple_word[i][j+2] + 80
            temp_word.data[3] = triple_word[i][1] + 80
            word.append(temp_word)

    print(len(word))
    return word


def pre_mid():
    pre_table = tables.pre_table
    word = []
    for i in range(len(pre_table)):
        for j in range(len(pre_table[i]) - 1):
            temp_word = TibetanWord()
            temp_word.data[0] = pre_table[i][0]
            temp_word.data[2] = pre_table[i][j + 1]
            word.append(temp_word)

    print(len(word))
    return word


def pre_mid_down_and_pre_mid_top(top_mid_down):
    up_table = tables.up_table
    down_table = tables.down_table
    pre_table = tables.pre_table_whole
    word = []
    for i in range(len(pre_table)):
        for j in range(len(pre_table[i]) - 1):
            index1 = find_index(pre_table[i][j + 1], down_table)
            if len(index1) > 0:
                for idx in index1:
                    temp_word = TibetanWord()
                    temp_word.data[0] = pre_table[i][0]
                    temp_word.data[2] = pre_table[i][j + 1]
                    temp_word.data[3] = down_table[idx][0] + 80
                    word.append(temp_word)

    for j in range(len(pre_table[2]) - 1):
        index2 = find_index(pre_table[2][j + 1], up_table)
        if len(index2) > 0:
            for idx in index2:
                temp_word = TibetanWord()
                temp_word.data[0] = pre_table[2][0]
                temp_word.data[1] = up_table[idx][0]
                temp_word.data[2] = pre_table[2][j + 1] + 80
                word.append(temp_word)
    # 删除不符合音节规律的20个字. 因为不符合音节规律就没法发音.
    delete_list = [57, 55, 53, 50, 47, 45, 39, 36, 33, 32, 29,
                   22, 21, 14, 7, 4, 3, 2, 1, 0]

    for i in delete_list:
        del word[i]

    # 添加三重叠字中的6个与前加字0x0f56的组合
    add_list = [0, 1, 3, 4, 8, 9]
    for idx in add_list:
        temp_word = TibetanWord()
        temp_word.data[0] = 0x0f56
        temp_word.data[1] = deepcopy(top_mid_down[idx].data[1])
        temp_word.data[2] = deepcopy(top_mid_down[idx].data[2])
        temp_word.data[3] = deepcopy(top_mid_down[idx].data[3])
        word.append(temp_word)

    print(len(word))
    return word


def find_index(data, table):
    index = []
    for i in range(len(table)):
        if data in table[i][1:]:
            index.append(i)

    return index


def consonant():
    consonant_list = tables.consonant_list
    word = []
    for i in consonant_list:
        temp_word = TibetanWord()
        temp_word.data[2] = i
        word.append(temp_word)

    return word


def add_vowel(basic_words):
    vowel = tables.vowel
    word = []
    for element in basic_words:
        for v in vowel:
            temp_word = TibetanWord()
            temp_word.data = deepcopy(element.data)
            temp_word.data[5] = v
            word.append(temp_word)

    print(len(word))
    return word


def add_after(basic_and_vowel):
    after_table = tables.after_table
    word = []
    for element in basic_and_vowel:
        for v in after_table:
            temp_word = TibetanWord()
            temp_word.data = deepcopy(element.data)
            temp_word.data[6] = v
            word.append(temp_word)

    print(len(word))
    return word


def add_after_after(basic_and_vowel):
    after_after_table = tables.after_after_table
    word = []
    for element in basic_and_vowel:
        for i in range(len(after_after_table)):
            for j in range(len(after_after_table[i])-1):
                temp_word = TibetanWord()
                temp_word.data = deepcopy(element.data)
                temp_word.data[7] = after_after_table[i][0]
                temp_word.data[6] = after_after_table[i][j+1]
                word.append(temp_word)

    print(len(word))
    return word


if __name__ == '__main__':
    # for char in range(0x0f00, 0xfdb)
    basic_words = []
    function_list = [consonant(), top_mid(), mid_down(), pre_mid(), mid_down_special()]
    for func in function_list:
        basic_words = basic_words + func

    top_mid_down = top_mid_down()
    pre_mid_down_and_pre_mid_top = pre_mid_down_and_pre_mid_top(top_mid_down)
    basic_words = basic_words + top_mid_down + pre_mid_down_and_pre_mid_top
    print(len(basic_words))
    # 以上就是基础字的生成
    # basic_words_copy = deepcopy(basic_words)
    basic_multi_vowel = add_vowel(basic_words)
    basic_and_vowel = basic_words + basic_multi_vowel
    add_after = add_after(basic_and_vowel)
    add_after_after = add_after_after(basic_and_vowel)

    words_18785 = basic_words + basic_multi_vowel + add_after + add_after_after
    print(len(words_18785))

    f = open('./藏字生成18785_文本.txt', 'w', encoding='utf-8')
    for i in range(len(words_18785)):
        f.write(words_18785[i].get_word())
        f.write("\n")

    f.close()

    f = open('./藏字生成18785_编码.txt', 'w', encoding='utf-8')
    for i in range(len(words_18785)):
        f.write(str(words_18785[i].data))
        f.write("\n")

    f.close()


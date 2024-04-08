from copy import deepcopy
import tables


class TibetanWord:
    const_list = tables.const_list

    def __init__(self, inputs=None):
        """

        :param inputs[optional]: list<int> size: [1, 8]
        """
        #             pre,    top,    mid,   down, down_down, vowel, tail, after_tail
        #              0,      1,      2,      3,      4,      5,      6,      7
        self.data = [0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000]
        self.data_c = [0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000]
        if inputs is not None:
            self.data = deepcopy(inputs)

    def creat_cmp_data(self):
        self.data_c = self.get_letters()

    def get_letters(self, other_data=None):
        """
        decode self-data or other data into original unicode list. The input and self-data as below.
                                   pre,    top,    mid,   down,  down_down, vowel, tail, after_tail
                                    0,      1,      2,      3,      4,      5,      6      7
        inputs&return: list like [0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000]
        :param other_data:
        :return: decoded list
        """
        if other_data is not None:
            res = deepcopy(other_data)
        else:
            res = deepcopy(self.data)
        for i in range(len(res)):
            if res[i] != 0x0000 and res[i] not in TibetanWord.const_list:
                res[i] = res[i] - 80
        return res

    def get_word(self):
        """
        decode self-data (a unicode list) into a string
        :return: string
        """
        word = ''
        for letter in self.data:
            if letter != 0x0000:
                word = word + chr(letter)
        return word

    def __lt__(self, other):
        if self.data_c[2] != other.data_c[2]:
            return self.data_c[2] < other.data_c[2]
        elif self.data_c[1] != other.data_c[1]:
            return self.data_c[1] < other.data_c[1]
        elif self.data_c[0] != other.data_c[0]:
            return self.data_c[0] < other.data_c[0]
        elif self.data_c[3] != other.data_c[3]:
            return self.data_c[3] < other.data_c[3]
        elif self.data_c[4] != other.data_c[4]:
            return self.data_c[4] < other.data_c[4]
        elif self.data_c[5] != other.data_c[5]:
            return self.data_c[5] < other.data_c[5]
        elif self.data_c[6] != other.data_c[6]:
            return self.data_c[6] < other.data_c[6]
        else:
            return self.data_c[7] < other.data_c[7]

    def __gt__(self, other):
        if self.data_c[2] != other.data_c[2]:
            return self.data_c[2] > other.data_c[2]
        elif self.data_c[1] != other.data_c[1]:
            return self.data_c[1] > other.data_c[1]
        elif self.data_c[0] != other.data_c[0]:
            return self.data_c[0] > other.data_c[0]
        elif self.data_c[3] != other.data_c[3]:
            return self.data_c[3] > other.data_c[3]
        elif self.data_c[4] != other.data_c[4]:
            return self.data_c[4] > other.data_c[4]
        elif self.data_c[5] != other.data_c[5]:
            return self.data_c[5] > other.data_c[5]
        elif self.data_c[6] != other.data_c[6]:
            return self.data_c[6] > other.data_c[6]
        else:
            return self.data_c[7] > other.data_c[7]


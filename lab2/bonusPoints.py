from collections import defaultdict


def count1(words_list):
    word_count = {}
    for word in words_list:
        if word.isnumeric():
            if word in word_count.keys():
                word_count[word] += 1
            else:
                word_count[word] = 1

    return word_count


def count2(words_list):
    word_count = defaultdict(int)
    for word in words_list:
        try:
            word_count[int(word)] += 1
        except ValueError:
            continue
    return word_count

def sortFunc(x):
    print(x)
    return x

if __name__ == "__main__":
    my_string = "We are having 3 numbers of 5 pieces and each of them are having 3 stars"

    words = my_string.split(" ")
    word_count = count1(words)
    print(count1(words))
    word_count = {k: v for k, v in sorted(word_count.items(), key=lambda x: x[1])}
    print(word_count)
    print(count2(words))
from collections import defaultdict
def word_count(text):
    return len(text.split())

def char_count(text):
    dic = defaultdict(int)
    for char in text:
        char = char.lower()
        dic[char] +=1
    return dic

def sort_dict(dic):
    dict_list = []
    for key in dic:
        if key.isalpha():
            row = {"char":key, "cnt":dic[key]}
            dict_list.append(row)
    return sorted(dict_list, key = lambda x: x['cnt'],reverse=True)
    
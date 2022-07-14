# Group Anagrams using Python

"""
 Anagrams are words formed by rearranging the letters of another word, For example, car and arc, cat and act, etc
"""

from collections import defaultdict


def group_anagrams(the_list):
    df_dict = defaultdict(list)

    for i in the_list:
        sorted_list = ' '.join(sorted(i))
        df_dict[sorted_list].append(i)

    return df_dict.values()


words = ['eat', 'cat', 'bat', 'car', 'arc']

print(group_anagrams(words))

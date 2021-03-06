#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 03. 円周率
# "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
# という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

import sys

text   = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
answer = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]

# Case 1
##########
def remove_comma_and_period(strings):
    if sys.version_info.major < 3:
        # Python 2 の場合
        import string
        s = strings.translate(None, ',.')
    else:
        # Python 3 の場合
        s = strings.translate(str.maketrans('', '', ',.'))
    return s

result = []
words  = remove_comma_and_period(text).split()

for word in words:
    result.append(len(word))

assert result == answer
print(result)
# => [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]


# Case 2
##########
result = []
words  = text.split()

for word in words:
    result.append(len(word.rstrip(',.')))

assert result == answer
print(result)
# => [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]

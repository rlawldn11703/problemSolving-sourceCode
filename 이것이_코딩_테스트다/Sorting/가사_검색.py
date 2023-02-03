from bisect import bisect_left,bisect_right
import re
def find_range(arr,q):
    s1,s2 = re.sub('\?','a',q),re.sub('\?','z',q)
    start = bisect_left(arr,s1)
    end = bisect_right(arr,s2)
    return end-start
def solution(words, queries):
    word_bag = [[] for _ in range(10001)]
    rev_word = [[] for _ in range(10001)]
    for word in words:
        n = len(word)
        word_bag[n].append(word)
        rev_word[n].append(word[::-1])
    for i in range(len(word_bag)):
        word_bag[i].sort()
        rev_word[i].sort()
    answer = []
    for query in queries:
        n = len(query)
        if query.startswith('?'):
            answer.append(find_range(rev_word[n],query[::-1]))
        else:
            answer.append(find_range(word_bag[n],query))
    return answer

# 그룹 애너그램(153p)
import collections


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    # 정렬해서 같은 애들끼리 묶으면 됨
    dic = collections.defaultdict(list)
    for s in strs:
        dic[''.join(sorted(s))].append(s)
    return dic.values()


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
# [["bat"],["nat","tan"],["ate","eat","tea"]]

#查找常用字符

# 每一个单词都设置哈希表的话，哈希表的数量无法确定。所以就需要进行换一种思路，我们可以设置一个哈希表存储第一个单词中的所有字母的数量，之后再设置一个哈希表，通过不断进行更新第一个哈希表中字母的值，我们可以得到每一个单词中的公共字符。

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words: return []
        result = []
        hash =[0] * 26 #用来统计所有字符串里字符出现的最小频率
        for i, c in enumerate(words[0]): #用第一个字符串给hash初始化
            hash[ord(c) - ord('a')] += 1
        #统计除第一个字符串外字符的出现频率
        for i in range(1, len(words)):
            hashOtherStr = [0] * 26
            for j in range(len(words[i])):
                hashOtherStr[ord(words[i][j]) - ord('a')] += 1
            for k in range(26):
                hash[k] = min(hash[k], hashOtherStr[k])
                
        for i in range(26):
            while hash[i] != 0:
                result.extend(chr(i + ord('a')))
                hash[i] -= 1
        return result
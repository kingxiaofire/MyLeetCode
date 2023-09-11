#翻转字符串里的单词
class Solution:
    def reverseWords(self, s: str) -> str:
        # 删除前后空白
        s = s.strip()
        # 反转整个字符串
        s = s[::-1]
        # 将字符串拆为单词，并反转每个单词
        s = ' '.join(word[::-1] for word in s.split())
        return s
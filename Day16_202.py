#快乐数
class Solution:
    def isHappy(self, n: int) -> bool:
        record = []
         # 如果中间结果重复出现，说明陷入死循环了，该数不是快乐数
        while n not in record:
            record.append(n)
            new_num = 0
            n_str = str(n)
            for i in n_str:
                new_num += int(i) ** 2
            if new_num == 1:
                return True
            else:
                n = new_num
        return False
'''给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。

示例 1:

输入: "aba"
输出: True
示例 2:

输入: "abca"
输出: True
解释: 你可以删除c字符。
注意:

字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。
'''
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def search(chars, times):  # chars为待筛查的字符串，times表示当前还有几次删除机会
            begin, end = 0, len(chars) - 1
            while begin < end:
                if chars[begin] != chars[end]:  # 若左右指针指向的字符不同，代表 begin end的范围内有需要被删除的点
                    if times == 0:  # 发现了不同，但是却没有可以删除的次数了，那么肯定不能完成题目要求
                        return False
                    # 如果上一步没返回，说明还有可供删除的次数
                    # 选择删除当前left,right闭区间的左边或者右边后，继续搜索对应剩下的部分，看能否完成题目要求
                    # 由于选择删除左边或者右边，这就已经用了一次删除机会，所以递归的时候传入times-1
                    return search(chars[begin:end], times - 1) or search(chars[begin + 1:end + 1], times - 1)
                # 可以把begin end想成夹子的两端，如果不走上面的if分支(也就是说夹子左右两端的元素相同)
                # 那么就把夹子收紧
                begin += 1
                end -= 1
            return True  # 如果能一路顺利走到这，说明传入的chars为回文，那自然返回True就可以了

        return search(s, 1)
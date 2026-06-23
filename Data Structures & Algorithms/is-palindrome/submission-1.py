class Solution:
    def isPalindrome(self, s: str) -> bool:
            lst = list()
            for i in s:
                if i  == " ":
                    continue
                elif i.isalnum():
                    lst.append(i.lower())

            j = len(lst) - 1
            length = j + 1
            count = 0

            for i in lst:
                if i == lst[j]:
                    count += 1
                j -= 1

            if count == length:
                return True
            else:
                return False



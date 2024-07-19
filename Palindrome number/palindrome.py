class Solution:
    def is_palindrome_str_manipulation(self, x):
        x=str(x)
        reversed_x = x[::-1]
        if x == reversed_x:
            return True
        return False


    def is_palindrome_mathematical_reversion(self, x):
        y = 0
        z = x
        while z > 0:
            n = z % 10
            z = int(z / 10)
            y = y*10+n
        if x == y:
            return True
        else:
            return False




if __name__=="__main__":
    solution = Solution()
    x=-111
    is_palindrome = solution.is_palindrome_str_manipulation(x)
    print(is_palindrome)
    is_palindrome_int = solution.is_palindrome_reverting_integers(x)
    print(is_palindrome_int)




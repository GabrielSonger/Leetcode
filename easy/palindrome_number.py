class Solution(object):
    #v0
    def is_palindrome_v0(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif x == 0:
            return True
        else:						
            str_x = str(x)

        reverse_str_x = str_x[::-1]

        for index in range(len(str_x)):
            if str_x[index] != reverse_str_x[index]:
                return False
        return True

    #v1 follow up
    def is_plindrom_v1(self, x):
        '''reverse half of the number'''
        # edge cases: negavite, 0x0
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        else:
            reversed_num = 0
            while (x > reversed_num):
                reversed_num = reversed_num * 10 + x % 10
                x = x / 10

            return x == reversed_num or x == reversed_num / 10
                
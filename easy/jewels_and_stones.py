class Solution(object):
    def jewels_and_stones(self, J, S):
        count = 0
        for stone in S:
            if stone in J:
                count += 1
        return count

    # loop distinct J is more efficient
    def jwels_and_stones_1(self, J, S):
        count = 0
        for jew in J:
            count += S.count(jew)
        return count
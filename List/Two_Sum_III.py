class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """
    def __init__(self):
        self.nums = []

    def add(self, number):
        self.nums.append(number)

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        nums_set = set()
        for number in self.nums:
            if (value - number) in nums_set:
                return True
            nums_set.add(number)
        return False

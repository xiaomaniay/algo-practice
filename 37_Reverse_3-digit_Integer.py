class Solution:
    """
    @param number: A 3-digit number.
    @return: Reversed number.
    """

    def reverseInteger(self, number):
        tempString = ""
        for x in str(number):
            tempString = x + tempString

        return int(tempString)

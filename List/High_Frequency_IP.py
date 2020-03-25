class Solution:
    """
    @param ipLines: ip  address
    @return: return highestFrequency ip address
    """
    def highestFrequency(self, ipLines):
        freq = {}
        for x in ipLines:
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1
        freq_max = max(freq.values())
        for x in ipLines:
            if freq[x] == freq_max:
                return x

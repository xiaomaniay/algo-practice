class Solution:
    """
    @param s: The capacity of backpack
    @param v: The value of goods
    @param c: The capacity of goods
    @return: The answer
    """
    def getMaxValue(self, s, v, c):
        if not (v and c):
            return 0
        value = [(0, 0)]
        for i in range(len(c)):
            new_value = []
            for j in range(len(value)):
                if value[j][1] + c[i] > s:
                    break
                new_value.append((value[j][0] + v[i], value[j][1] + c[i]))
            merged_value = []
            while new_value or value:
                if new_value and value:
                    compare_val = new_value[0][0] > value[0][0]
                    compare_cap = new_value[0][1] > value[0][1]
                    if compare_val and compare_cap:
                        if compare_val:
                            merged_value.append(value[0])
                            value.pop(0)
                        else:
                            merged_value.append(new_value[0])
                            new_value.pop(0)
                    else:
                        merged_value.append(max(new_value[0], value[0]))
                        new_value.pop(0)
                        value.pop(0)
                else:
                    merged_value += (new_value or value)
                    break
            value = merged_value
        return value[-1][0]





if __name__ == "__main__":
    s = 195387950
    v = [277996895,67034365,215265173,17927245,196665561,122553408,229181848,37953684,130611629,18096518,221937650,16569090,215131206,246680015,75894559,177999561,249070738,321264238,110845985,176753214]
    c = [228482420,301972492,81534843,235620330,102486915,234004708,18881095,194477148,60832041,118314582,292428017,74861428,43938149,86992501,239732394,193891049,112838218,127944264,276821750,172241156]
    reslt = Solution().getMaxValue(s, v, c)
    print(reslt)

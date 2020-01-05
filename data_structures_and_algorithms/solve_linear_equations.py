import numpy as np
import math

# coefficients for each equation on the left side
# a = np.array([[1, 1, 1], [22.76, -0.612, 0], [0, 1.272, -0.237]])
# # the right had side of the equation
# b = np.array([1, 0, 0])
#
# x = np.linalg.solve(a, b)
# print(x)

# , [0, 6.22, -34.899]

# w_1= 0.0223
# w_2= 0.1564
# w_3=0.8394
# m_price= 7.99*w_1+(-0.01)*w_2+(3.75)*w_3
# bs_price = 7.99*w_1+(-0.35)*w_2+(4.45)*w_3
# print(m_price, bs_price)
# print(m_price - bs_price)
# print(w_2*1.272+ w_3*(-0.237))
# print(w_2*6.22+ w_3*(-34.899))

K=103.1
F=100
sigma = 0.3507 + 0.1683*(math.log(K/F))+ 5.1725*((math.log(K/F))**2)
print(sigma)


# w_1= 0.0042
# w_2= 0.1564
# w_3=0.8394
# print(w_1/w_3)
# print(w_2/w_3)
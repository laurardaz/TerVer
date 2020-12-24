# A = [26.65, 27.55, 29.45, 31.35, 33.25, 35.15, 37.05, 38.95]
# B = [9, 11, 16, 27, 19, 11, 5, 2]


# A = [0.3, 3.42, 6.53, 9.65, 12.77, 15.88, 19, 22.11]
# B = [5, 11, 19, 22, 26, 9, 6, 2]
# x_b = sum(i[0] * i[1] for i in zip(A, B)) / 100
# print(x_b)
# for j in range(2, 5):
#     print(list(pow(i[0] - x_b, j) * i[1] for i in zip(A, B)))


import math

# A = [- math.inf, 26.6, 28.5, 30.4, 32.3, 34.2, 36.1, 38]
# B = [26.6, 28.5, 30.4, 32.3, 34.2, 36.1, 38, + math.inf]
# C = [9, 11, 16, 27, 19, 11, 5, 2]
# x_b = 31.35
# sigma_b = 3.21

A = [-math.inf, 1.86, 4.97, 8.09, 11.21, 14.32, 17.44, 20.55]
B = [1.86, 4.97, 8.09, 11.21, 14.32, 17.44, 20.55, +math.inf]
C = [5, 11, 19, 22, 26, 9, 6, 2]
x_b = 10.0865
sigma_b = 4.97


z_i_1 = list((i - x_b) / sigma_b for i in A)
print(z_i_1)
z_i = list((i - x_b) / sigma_b for i in B)
print(z_i)



from scipy.special import erf

Phi = lambda x: (1 + erf(x/math.sqrt(2))) / 2 - 0.5

Phi_z_i_1 = list(map(Phi, z_i_1))
Phi_z_i = list(map(Phi, z_i))
print(list(zip(Phi_z_i_1, Phi_z_i)))


n_p_i = list(100 * (i[1] - i[0]) for i in zip(Phi_z_i_1, Phi_z_i))
print(n_p_i)
print(sum(n_p_i))

ni_npi = list(pow(i[0] - i[1], 2) / i[1] for i in zip(C, n_p_i))
print(ni_npi)
print(sum(ni_npi))


# A = -1.26
# for _ in range(8):
#     A += 3.11625
#     print(A)
#

# A = [-1.26, 1.86, 4.97, 8.09, 11.21, 14.32, 17.44, 20.55]
# B = [1.86, 4.97, 8.09, 11.21, 14.32, 17.44, 20.55, 23.67]
# for _ in range(8):

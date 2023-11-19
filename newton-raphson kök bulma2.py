def newton_raphson2(x0, iterasyon):
    for i in range(iterasyon):
        fx = 4 * (2.71828 ** (0.5 * x0)) - x0
        fx_turevi = 2 * (2.71828 ** (0.5 * x0)) - 1
        x0 = x0 - fx / fx_turevi
    return x0
x0 = 2
iterasyon=4
kokun_yaklasik_degeri = newton_raphson2(x0,iterasyon)
print("Yaklaşık kök: {}".format(kokun_yaklasik_degeri))

def newton_raphson1(x0, iterasyon):
    for i in range(iterasyon):
        fx = x0**(1/3)
        fx_turevi = (x0**(-2/3)/3)
        x0 = x0 - fx / fx_turevi
    return x0

x0 = 8
iterasyon = 3
kokun_yaklasik_degeri = newton_raphson1(x0, iterasyon)
print("Yaklaşık kök: {}".format(kokun_yaklasik_degeri))

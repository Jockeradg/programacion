x:float = (33 * (4.3e3) + (2.5e2)) * (27.6 - 37.8) / (12.7 + 1e-2 * 4.3)
y:float = (x - 23.4)**2
z:float = y * 102350000
r:float = abs((x + y*1e-3) / (100 - z))
s:complex = r + (2 + 3j) ** 2
t:complex = 1e22 * s**2 - 3 * 1e4j
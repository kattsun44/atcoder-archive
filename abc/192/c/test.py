n = 314

l = list(str(n))
g1 = int("".join(sorted(l)))
g2 = int("".join(sorted(l,reverse=True)))

print(g1,g2,g2-g1)
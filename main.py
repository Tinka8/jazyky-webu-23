cislo = int(input())
delitele = []

for i in range(1, cislo + 1):
  if cislo % i == 0:
    delitele.append(i)
  else:
    i += 1

delitele.sort(reverse=True)
map(str, delitele)
print(" ,".join(delitele))
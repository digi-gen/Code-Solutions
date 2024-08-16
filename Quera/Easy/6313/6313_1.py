# https://quera.org/problemset/6313

finall = []
while True:
    temp = int(input())
    if temp == 0:
        break
    else:
        if temp <= 1_000_000:
            finall.append(temp)
        elif 1_000_000 < temp <= 5_000_000:
            finall.append(int(temp-temp*0.1))
        else:
            finall.append(int(temp-temp*0.2))
            
print(*finall, sep='\n')

# Code wirter Github: https://github.com/mr-mahmood
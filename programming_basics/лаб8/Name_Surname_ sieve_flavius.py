def  sieve_flavius(n):
    lucky = []
    better_lucky = []
    for i in range(1, n + 1):
        lucky += [i]
    for j in range(1, n+1):
        for i in range(len(lucky) + 1):
            j += 1
            if lucky[j] % j == 0:
                better_lucky.append(lucky[j])
    return better_lucky
print(sieve_flavius(33))
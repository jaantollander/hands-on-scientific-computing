rounds = 8
t = time.time()

for i in range(rounds):
    a = np.random.random([1000, 1000])
    b = np.random.random([1000, 1000])
    rslt = np.corrcoef(a,b)

t_taken = time.time() - t

print('Takes {} seconds to calculate pearson product-moment correlation for 1000x1000 matrices'.format(t_taken))

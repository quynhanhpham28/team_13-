import random
total_flips = 0
num_simulations = 10
for _ in range(num_simulations):
    flips = 0
    consecutive_heads = 0
    consecutive_tails = 0
    while consecutive_heads < 3 and consecutive_tails < 3:
        flip_result = random.choice(['H', 'T'])
        print(flip_result, end=' ')
        flips += 1
        if flip_result == 'H':
            consecutive_heads += 1
            consecutive_tails = 0
        else:
            consecutive_tails += 1
            consecutive_heads = 0
    print("(",flips," flips)",sep='')
    total_flips += flips
average_flips = total_flips / num_simulations
print("On average,",average_flips,"flips were needed.")

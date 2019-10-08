import random

star = [16637, 14891, 15662, 4210, 14890, 3190, 15863, 17406, 17281, 16236, 7576, 11559, 13460, 13458, 14499, 14500, 14888, 1697, 15683, 15684, 17144, 17143, 17140, 17472]
cherry_blossom = [1966, 1725, 3019, 2234, 2151, 16932, 16947, 16959, 1600, 1012, 11403, 9466]

random.shuffle(star)
random.shuffle(cherry_blossom)

res = []
for i in range(12):
    temp = []
    temp.append(star[i*2])
    temp.append(star[i*2+1])
    temp.append(cherry_blossom[i])
    res.append(temp)

print(res)
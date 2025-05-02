# csv파일 불러와서 평균구하는 문제. 

infile = open('test_scores.csv', 'r')
lines = infile.readlines()
print(lines)
infile.close()

for line in lines:
    tokens = line.split(',')
    total = 0
    for score in tokens:
        total += float(score)              # float이 '\n'을 제거해주더라. 
        average = total/len(tokens)
    print('Average:', average)

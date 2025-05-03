import matplotlib.pyplot as plt

# 텍스트파일 가져와서 읽기
infile = open('GasPrices.txt', 'r')
lines = infile.readlines()
infile.close()

# '/n' 제거
for i in range(len(lines)):
    lines[i] = lines[i].rstrip('\n')

# 하나씩 필요한 것만 남기기
years = []
prices = []
for line in lines:
    line = line.split(':')      # ':'을 기준으로 분리
    year = int(line[0][-4:])    # 연도만 따로 분리 
    price = float(line[1])

    years.append(year)
    prices.append(price)

# 그래프의 x, y 설정
x = [year for year in range(years[0], years[-1]+1)]  # x: 1993년 ~ 2013년
y = []                                               # y: 연도별 값의 평균
for year in x:
   year_prices = []                                  # 연도별로 평균구하기
   for i in range(len(years)):
      if year == years[i]:
         year_prices.append(prices[i])
   
   avg = sum(year_prices) / len(year_prices)
   y.append(avg)

print(x);
print(y)

# 그래프 그리기 시작
plt.plot(x, y, 'o--')

# x(년도)가 2년마다 표시되게끔 xticks 이용
interval = []
for i in range(0, len(x), 2):
   interval.append(x[i])
plt.xticks(interval, rotation = 45)

plt.tight_layout()
plt.title("Average gas price per year in US")
plt.xlabel("year")
plt.ylabel("Avg.gas price per gallon[s]")
plt.grid()
plt.show()

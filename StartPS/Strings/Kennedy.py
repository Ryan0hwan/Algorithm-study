# Kennedy.txt 파일 이용

inputfile = open('Kennedy.txt', 'r')
line_list = inputfile.readlines()
inputfile.close()
print(line_list)

# 일단 '\n'부터 제거
for i in range(len(line_list)):
    line_list[i] = line_list[i].rstrip('\n')
print(line_list)

# 단어 하나씩으로 다 분리.
stop_words = ['a', 'an', 'the', 'and', 'or', 'but', 'as', 'of']
all_words = []
for item in line_list:
    words = item.split()    # 하나를 공백으로 분리하니까 단어가생기는거지.
    for word in words:      # 단어를 하나씩 도는거지
        if word not in stop_words:
           all_words.append(word)  # append와 +의 차이가 뭐지?
           
print(all_words)
print(len(all_words))    # 27개중 관사 분리시키니까 16개

# 관사(stop words)를 빼고 카운트해보자.

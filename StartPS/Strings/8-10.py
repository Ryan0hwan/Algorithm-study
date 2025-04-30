# 10. 문자열 입력 -> 가장 자주 쓰인 문자 출력. 
# 어떤 문자의 개수 비교 -> 바로 dictionary문제임을 인지.

sentence = input()

def mode(sen):
   char_count = {}   # 딕셔너리 초기화

   for ch in sen:                           
       if ch in char_count:
            char_count[ch] += 1
       else:
            char_count[ch] = 1
 
   max_count = 0
   mode_char = None

   for ch, count in char_count.items():
      if count > max_count:
         mode_char = ch                   # 딕셔너리 안에서 max값 찾을 때 많이 쓰이는거. 
         max_count = count 
    
   return mode_char


print(mode(sentence))

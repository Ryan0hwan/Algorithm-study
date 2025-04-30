
# 9. 문자열 입력 -> 모음의 개수, 자음의 개수, 단어의 개수 [함수 3개 쓸 것.]

sentence = input()

def vowel_count(sen):
   count = 0
   vowels = "aeiouAEIOU"

   for ch in sen:
      if ch in vowels:
         count+=1
   
   return count 

def consonant_count(sen):
   count = 0
   consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

   for ch in sen:
      if ch in consonants:
         count+=1

   return count      

def word_count(sen):
   words = sen.split()       
   return len(words)

print(f'Number of vowels: {vowel_count(sentence)}')
print(f'Number of consonants: {consonant_count(sentence)}')
print(f'Number of words: {word_count(sentence)}')

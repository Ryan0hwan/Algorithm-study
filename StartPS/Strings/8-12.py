# 12. Pig Latin 게임.
# 단어마다, 첫 글자를 단어의 맨뒤로 보내고, AY도 붙임.

sentence = input()


def pig_latin(text):
   text = text.upper()
   words = text.split()

   convert_words = []
   for word in words:
        convert_word = word[1:] + word[0] + "AE"
        convert_words.append(convert_word)    
   return " ".join(convert_words)

print(sentence)
print(pig_latin(sentence))

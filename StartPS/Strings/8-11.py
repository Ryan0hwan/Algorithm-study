# 11. 다 붙어있는 문자열을 입력받아, 대문자가 나오면 분리하고, 대문자는 첫글자만 남겨두기
# 예시 "StopAndSmellTheRoses."라는 문자열은 "Stop and smell the roses."로 변환\

sentence = input()

def convert(text):
    result = text[0]

    for ch in text[1:]:
       if ch.isupper():
          result += " " + ch.lower()
       else:
          result += ch

    return result

print(convert(sentence))

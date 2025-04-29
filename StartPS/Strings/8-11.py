# Write a program that accepts as input a sentence in which all of the words are run together but the first character of each word is uppercase. 
# Convert the sentence to a string in which the words are separated by spaces, and only the first word starts with an uppercase letter. 
# For example the string "StopAndSmellTheRoses." would be converted to "Stop and smell the roses."

# 단어마다 첫글자가 대문자인 문장 입력받아서, 단어들을 띄어쓰기로 구분하고, 대문자는 첫문자만 남겨두기 문제.

def split_and_format(sentence):
    # 단어들을 담을 리스트 초기화
    words = []
    current_word = sentence[0]  # 첫 글자에서 시작

    # 두 번째 문자부터 끝까지 반복
    for char in sentence[1:]:
        if char.isupper():
            # 대문자가 나오면 새로운 단어의 시작이므로 기존 단어 저장
            words.append(current_word)
            current_word = char
        else:
            # 아니면 현재 단어에 이어붙임
            current_word += char

    # 마지막 단어도 리스트에 추가
    words.append(current_word)

    # 전체를 소문자로 바꾸되 첫 단어만 첫 글자 대문자
    formatted_sentence = ' '.join(words).lower()
    formatted_sentence = formatted_sentence[0].upper() + formatted_sentence[1:]

    return formatted_sentence

# 예제 실행
input= "StopAndSmellTheRoses"
output= split_and_format(input)
print(output)

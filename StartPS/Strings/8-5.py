# 5. 숫자+문자 전화번호 -> 숫자 전화번호로 바꾸기 문제

telephone = input()

def translate_telephone(number):
    translate_num = ""      
    
    for ch in number:
        if ch.isalpha():                # 알파벳에 맞는 숫자를 배정         
            if ch in 'ABC':
               translate_num += '2'
            elif ch in 'DEF':
               translate_num += '3'
            elif ch in 'GHI':
               translate_num += '4'
            elif ch in 'JKL':
               translate_num += '5'
            elif ch in 'MNO':
               translate_num += '6'
            elif ch in 'PQRS':
               translate_num += '7'
            elif ch in 'TUV':
               translate_num += '8'
            elif ch in 'WXYZ':
               translate_num += '9'
        else:                         # 숫자나 특수문자일 경우 그냥 붙여주기
            translate_num += ch             

    return translate_num

print(translate_telephone(telephone))

import re

def read_file_words(file_path):
    """
    파일을 읽고 모든 단어의 세트를 반환합니다.
    단어는 알파벳과 숫자만 포함하며 대소문자를 구분하지 않습니다.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read().lower()
            # 알파벳, 숫자 및 공백만 남기고 모든 문자 제거
            content = re.sub(r'[^a-z0-9\s]', ' ', content)
            # 공백으로 분리하여 단어 목록 생성
            words = content.split()
            return set(words)
    except FileNotFoundError:
        print(f"오류: '{file_path}' 파일을 찾을 수 없습니다.")
        return set()
    except Exception as e:
        print(f"파일 '{file_path}'을 읽는 중 오류 발생: {e}")
        return set()

def compare_files(file1_path, file2_path):
    """두 파일의 내용을 비교하고 다양한 세트 연산 결과를 표시합니다."""
    
    # 각 파일에서 단어 세트 가져오기
    words1 = read_file_words(file1_path)
    words2 = read_file_words(file2_path)
    
    if not words1 and not words2:
        print("두 파일을 모두 읽을 수 없습니다. 프로그램을 종료합니다.")
        return
    
    # 1. 두 파일에 포함된 모든 고유 단어 목록 (합집합)
    all_unique_words = words1.union(words2)
    print("\n1. 두 파일에 포함된 모든 고유 단어:")
    print_word_set(all_unique_words)
    
    # 2. 두 파일에 모두 나타나는 단어 목록 (교집합)
    words_in_both = words1.intersection(words2)
    print("\n2. 두 파일에 모두 나타나는 단어:")
    print_word_set(words_in_both)
    
    # 3. 첫 번째 파일에만 나타나는 단어 목록 (차집합)
    words_only_in_first = words1.difference(words2)
    print("\n3. 첫 번째 파일에만 나타나는 단어:")
    print_word_set(words_only_in_first)
    
    # 4. 두 번째 파일에만 나타나는 단어 목록 (차집합)
    words_only_in_second = words2.difference(words1)
    print("\n4. 두 번째 파일에만 나타나는 단어:")
    print_word_set(words_only_in_second)
    
    # 5. 첫 번째 또는 두 번째 파일에만 나타나는 단어 목록 (대칭 차집합)
    words_in_either_not_both = words1.symmetric_difference(words2)
    print("\n5. 첫 번째 또는 두 번째 파일에만 나타나는 단어 (둘 다 아님):")
    print_word_set(words_in_either_not_both)

def print_word_set(word_set):
    """세트의 단어를 정렬하여 출력합니다."""
    if not word_set:
        print("(없음)")
    else:
        sorted_words = sorted(word_set)
        for word in sorted_words:
            print(f"  {word}")

def main():
    print("두 파일의 내용을 비교하는 프로그램")
    file1_path = input("첫 번째 파일 경로를 입력하세요: ")
    file2_path = input("두 번째 파일 경로를 입력하세요: ")
    
    compare_files(file1_path, file2_path)

if __name__ == "__main__":
    main()

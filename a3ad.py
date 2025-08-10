def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

def main():
    word = input("Введите слово или фразу: ")
    if not word:
        print("Ошибка: введите непустую строку!")
    elif is_palindrome(word):
        print(f"'{word}' - это палиндром!")
    else:
        print(f"'{word}' - не палиндром.")

if __name__ == "__main__":
    main()
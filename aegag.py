def count_vowels(text):
    vowels = 'aeiouаеёиоуыэюя'
    text = text.lower()
    count = sum(1 for char in text if char in vowels)
    return count

def main():
    text = input("Введите строку: ")
    if not text:
        print("Ошибка: введите непустую строку!")
    else:
        result = count_vowels(text)
        print(f"Количество гласных: {result}")

if __name__ == "__main__":
    main()
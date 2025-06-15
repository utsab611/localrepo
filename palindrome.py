class Palindrome:
    def __init__(self, word: str):
        self.word = word

    def is_palindrome(self) -> bool:
        normalized = self.word.lower()
        return normalized == normalized[::-1]

    def __str__(self):
        return f'"{self.word}" is a palindrome.' if self.is_palindrome() else f'"{self.word}" is not a palindrome.'

if __name__ == "__main__":
    word = "Utsabastu"
    palin_check = Palindrome(word)
    print(palin_check)
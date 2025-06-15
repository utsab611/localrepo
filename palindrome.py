class palindrome:
    def __init__(self,s):
        self.word=s
    def check(self):
        if self.word==self.word[::-1]:
            print("The word is palindrome")
        else:
            print("The word is not palindrome")

if __name__=="__main__":
    word="asdfdsa"
    palin_check=palindrome(word)
    palin_check.check()




n=input()
words={}
for i in range(int(n)):
    word=input()
    if word not in words:
        words[word]=1
    else:
        words[word]=words[word]+1
n=input()
for i in range(int(n)):
    word=input()
    if word not in words:
        print(0)
    else:
        print(words[word])
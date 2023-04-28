f=open("file.txt","r")

content=f.read()
print("Content of file:-")
print(content)

content=content.split('\n')
words=[]
for line in content:
    words.extend(line.split(' '))

d={}
m=0
for word in words:
    word=word.rstrip('.').rstrip(',').rstrip(':').rstrip(';')
    word=word.lower()
    if word in d:
        d[word]+=1
    else:
        d[word]=1

    m=max(m,d[word])

ans=[]
for word in d:
    if d[word]==m:
        ans.append(word)

print(f"\nMost frequent words in file are:-")
for i in ans:
    print(i,end=' ')

"""
Content of file:-
The paragraph is a paragraph but it is not a paragraph because its not a one.
The one which find is the one.

Most frequent words in file are:-
the paragraph is a one
"""

#to display  word with longest length
str1=input("enter the string to display word with longest length: ")
list1=str1.split()
m=0
word=0
print(list1)
for i in range(len(list1)):
    if(m<len(list1[i])):
        m=len(list1[i])
        word=i
print("the word with longest lenght",list1[word])

#to determine frequncy of occurance of particular character in string
str1=input("enter the string to count frquency of occurance:")
char=input("enter character to find:")
counter=0
for i in range(len(str1)):
    if char==str1[i]:
        counter+=1
print("character",char,"is present",counter,"times in string",str1)
#to count occurance of each word in given string

str1 = input("Enter input string To count the occurrences of each word: \n")

list1 = str1.split()

list2 = set(list1)  
list3 = list(list2)  

print(list1) 
print(list3) 
list4 = []
list5 = []
counter = 0
for i in range(len(list3)):      
    counter = 0
    for j in range(len(list1)): 
        if list3[i] == list1[j]:
            counter += 1
    list4 = list3[i], counter
    list5.append(list4)
print("\n", list5 ) 
#to check wheter givem string is plaimdrone or not
a=input("enter string is palimdrome or not:")
c=a[::-1]
if(c==a):
    print("string is plaimdrome\\")
else:
    print("not")
#to display index of first appearca eof the substring
str1 = input("Enter the string To display index of first appearance of the substring:- \n")
sub1 = input("Enter substring:- \n")
index=str1.find(sub1)
sublen = len(sub1)
print("substring index :", index)
        
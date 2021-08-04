import csv

print("File:")
file1 = input()

with open(file1, newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

list1 = []
str1 = ""
for n in data:
	list1.append('"'+n[0]+'"')

for n in list1:
	str1 = str1+' OR '
	str1 = str1+n

print(data)
print(list1)
print(str1)

text_file = open("output.txt", "w")
n = text_file.write(str1)
text_file.close()

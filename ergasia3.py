import string
allowed_chars = string.ascii_letters + " "
with open("text1.txt") as f:
    text = f.read()
    for c in text:
        if c in allowed_chars:
            text = f.read()
words = list(text.split(" "))
print(words)  #αρχικη λιστα με τις λεξεις

for i in words:
    for j in words:
        if i == j:
            continue
        if len(i) + len(j) == 20:
            words.remove(i)
            words.remove(j)

print(words)  #λιστα μετα απο διγραφη των ζευγαριων που εχουν αθροισμα 20

words_len = []  #καινουργια λιστα μονο με τα length των λεξεων ωστε να βγαλω στατιστικα
for k in words:
    words_len.append(len(k))

#dictionary οπου εχει σαν key τα μηκη των λεξεων και σαν value ποσες φορες υπαρχει λεξη με αυτο το μηκος
dict_of_counts = {item: words_len.count(item) for item in words_len}

print(dict_of_counts)

for key, value in dict_of_counts.items():
    if value == 0:
        continue
    print(f"There is {value} words of {key} letters.")

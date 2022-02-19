lines = [] #λιστα με τις γραμμες του text
first = [] #λιστα με τα x
second = [] #λιστα με τα y
third = [] #λιστα με τα names

with open('text.txt') as f: #ανοιγω και διαβαζω καθε γραμμη του αρχειου text
    lines = f.readlines()

print("Τα διαθέσιμα κλειδιά είναι : ['x', 'y', 'name']")
ep = input("Ποιό από τα διαθέσιμα κλειδία σε ενδιαφέρει; : ")

#αρχικοποιηση μεταβλητων
maxx=0
minx = 0
l = 0

if (ep == 'x'): # αν το επιλεγμενο κλειδι ειναι το x
    for line in lines:  # αφαιρω τα κενα κ βαζω τα λεξ στο dict που ειναι str
        l = l + 1
        dict = line.rstrip()
        list = dict.split()  # φτιαχνω μια λιστα με τα dict
        first = list[1].replace(',', '')  # afairw to komma

        if l ==1:
            firstx =int(first) #η πρωτη τιμη του x
        x = int(first) #ολες οι τιμες των x
        if (maxx < x):
            maxx = x #η μεγαλυτερη τιμη του x
        if (minx > x):
            minx = x #η μικροτερη τιμη του x
        if (firstx == x):
            famx = x #η δημοφιλεστερη τιμη του x
        firstx = x # καθε γορα κραταει την προηγουμενη τιμη του x

    #εμφανιση αποτελεσματων
    print("Η μεγαλύτερη τιμή είναι : ", maxx)
    print("Η μικρότερη τιμή είναι : ", minx)
    print("Η δημοφιλέστερη τιμή είναι : ", famx)

#αρχικοποιηση μεταβλητων
maxy = 0
miny = 0
z = 0

if (ep=='y'): #αν το επιλεγμενο κλειδι ειναι το y
    for line in lines:  # αφαιρω τα κενα κ βαζω τα λεξ στο dict που ειναι str
        z = z + 1
        dict = line.rstrip()
        list = dict.split()  # φτιαχνω μια λιστα με τα dict
        second = list[3].replace(',', '')  # afairw to komma

        if z == 1:
            firsty = int(second) #η πρωτη τιμη του y
        y = int(second) #ολες οι τιμες του y
        if (maxy < y):
            maxy = y #η μεγαλυτερη τιμη του y
        if (miny > y):
            miny = y #η μικροτερη τιμη του y
        if ( firsty == y):
            famy = y #η δημοφιλεστερη τιμη του y
        firsty =  y #καθε γορα κραταει την προηγουμενη τιμη του y

    #εμφανιση αποτελεσματων
    print("Η μεγαλύτερη τιμή είναι : ", maxy )
    print("Η μικρότερη τιμή είναι : ", miny )
    print("Η δημοφιλέστερη τιμή είναι : ", famy )

#αρχικοποιηση μεταβλητων
#σε συγκριση γραμματων εστω οτι το a<z
maxname = 'a'
minname = 'z'
k=0
g='a'

if(ep=='name'): #αν το επιλεγμενο κλειδι ειναι το name
    for line in lines:  # αφαιρω τα κενα κ βαζω τα λεξ στο dict που ειναι str
        k = k + 1
        dict = line.rstrip()
        list = dict.split()  # φτιαχνω μια λιστα με τα dict
        third = list[5].replace('"', "")

        if (maxname < third[0]):
            maxname = third #η μεγαλυτερη τιμη του name
        if (minname > third[0]):
            minname = third # η μικροτερη τιμη του name
        if (k==1):
            fname = third
        if (fname==third):
            famname = third #η δημοφιλεστερη τιμη του name
        else:
            g = third
        if ( g == third):
            famname = g #η δημοφιλεστερη τιμη του name

    #εμφαιση αποτελεσματων
    print("Η μεγαλύτερη τιμή είναι : ", maxname )
    print("Η μικρότερη τιμή είναι : ", minname )
    print("Η δημοφιλέστερη τιμή είναι : ", famname )

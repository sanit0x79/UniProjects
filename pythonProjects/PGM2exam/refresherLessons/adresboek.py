names = ["John", "Amber", "Judith", "Kees"]
phone = ["06-12345", "06-23456", "06-34567", "06-45678"]

i = 0

#for x in names:
    #if x == "Judith":
        #for y in phone:
            #i += 1
            #if i == 3:
                #                print(x, y)   
#    else:
#        print("This is not Judith")   


# Correct solution
#for b in range(len(names)):
    #    if names[b] == "Judith":
        #        print(names[b])
#        print(phone[b])
# Second solution
#i = 0
#for x in names:
#    if x == "Judith":
#        print(phone[i])
#    i += 1

addressbook = {
        }
for i in range(len(names)):
    addressbook[names[i]] = phone[i]
print(addressbook)


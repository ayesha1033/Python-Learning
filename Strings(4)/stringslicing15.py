'''
name = "humty"

print(name[0:2]) # goes from 0 to 2-1 i.e 0 to 1, output: hu

print(name[0:-1]) # same as name[0:4] , output: humt

'''

name = "abcdefgh0987"
#print(name[0:10:n]) #skip n-1 characters

print(name[0:10:1]) #skip 0 characters, output: abcdefgh09
print(name[0:10:2]) #skip 1 character, output: aceg09
print(name[0:10:3]) #skip 2 characters, output: adg0

print(name[:10]) #same as name[0:10], output: abcdefgh09
print(name[0:]) #same as name[0:len(name)], output: abcdefgh0987

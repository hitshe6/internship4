string = "ABEC"

substring_start = ['a','e','i','o','u','A','E','I','O','U']

amazing_substrings = []

for i in range(len(string)):
    if string[i] in substring_start:
        for j in range(len(string[i:])+1):
            amazing_substring = string[i:i+j]
            if amazing_substring!='':
                amazing_substrings += [amazing_substring]

print (amazing_substrings ,len(amazing_substrings)%10003)

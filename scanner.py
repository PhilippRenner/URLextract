##
##
##

import re
import urllib

#with open('/mnt/c/Users/.../Virusemails.txt') as f:
with open('/home/Virusemails.txt') as f:
    text = f.read()

    href_regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    #href_regex = '(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    urls = re.findall(href_regex, text)

    href_regex_dns = '@\S+[.]\S+'
    #href_regex_dns = '@S+([\w-]+\.)+[\w-]{2,4}$'
    urlsdns = re.findall(href_regex_dns, text)

print(urlsdns)


with open('/home/PHURLresult.txt', 'w') as f:
    for item in urls:
        f.write("\n"+item)
f.close()

whitelist = ['aol', 'analytik-jena','gmx','gmail','web']

with open('/home/PHURLresult.txt', 'a') as f:
    for item in urlsdns:
        input=item.translate(item.maketrans('','','*%,&@!;<>:()"'))
        if any(x in input for x in whitelist):
            print (input)
        else:
         f.write("\n"+input)

f.close()

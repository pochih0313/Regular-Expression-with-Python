import urllib.request
import re
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

s = input("input author name: ")
s = s.split(" ")
s[0] = s[0].replace(",","%2C")
author = "%s"%s[0].capitalize()
for i in range(len(s)-1):
    s[i+1] = s[i+1].replace(",","%2C")
    author = author + "+%s"%s[i+1].capitalize()
print(author)
# if(s[2]):
#     author = "%s+%s+%s"%(s[0],s[1],s[2])
# elif(s[1]):
#     author = "%s+%s"%(s[0],s[1])
# else:
#     author = "%s"%s[0]
#author = "Ian+Goodfellow"

url = "https://arxiv.org/search/?query=" + author + "&searchtype=author"
#url = "https://arxiv.org/search/?query=Ian+Goodfellow&searchtype=all&abstracts=show&order=-announced_date_first&size=50&start=50"
content = urllib.request.urlopen(url)
html_str = content.read().decode('utf-8')
pattern2 = 'has-text-black-bis has-text-weight-semibold\">Submitted[\s\S]*?<span'
count = {}

while(1):
    result2 = re.findall(pattern2, html_str)
    for r in result2:
        date = r.split("has-text-black-bis has-text-weight-semibold\">Submitted</span>")[1].split("<span")[0].strip()
        year = date.split(" ")[2].strip(';')
        if year in count.keys():
            print("plus")
            count[year] += 1
        else:
            count[year] = 1
        print(count)

    next_url_pattern = "<nav class=\"pagination is-small is-centered breathe-horizontal\"[\s\S]*?Next"
    next_url = re.findall(next_url_pattern, html_str)
    if(next_url):
        print(next_url)
        next_url = next_url[0].split("Previous")[1].split("</a>")[1].split("<a href")[1].split(">Next")[0]
        print(next_url)
        if(next_url[2] != '\"'): #if there exists next page
            next_url = "https://arxiv.org/search/?query="+author+"&searchtype=author&abstracts=show&order=-announced_date_first&size=50&"+next_url.split("author&amp;")[1].split("\"")[0]
            print(next_url)
            next_content = urllib.request.urlopen(next_url)
            html_str = next_content.read().decode('utf-8')
        else:
            break
    else:
        break

list1 = list(count.keys())
list2 = list(count.values())
plt.bar(list1,list2)
plt.show()

# pattern = 'title is-5 mathjax[\s\S]*?</p>'
# result = re.findall(pattern, html_str)


# print("[ Author: " + author + " ]")
# for r in result:
#     title = r.split("title is-5 mathjax\">")[1].split("</p>")[0].strip()
#     print(title)
import urllib.request
import re
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

#s = input("input author name: ")
#s = s.split(" ")
#author = "%s+%s"%(s[0],s[1])
author = "Ian+Goodfellow"

url = "https://arxiv.org/search/?query=" + author + "&searchtype=author"
content = urllib.request.urlopen(url)
html_str = content.read().decode('utf-8')

pattern = 'title is-5 mathjax[\s\S]*?</p>'
result = re.findall(pattern, html_str)
pattern2 = 'has-text-black-bis has-text-weight-semibold\">Submitted[\s\S]*?<span'
result2 = re.findall(pattern2, html_str)

count = {}
for r in result2:
    date = r.split("has-text-black-bis has-text-weight-semibold\">Submitted</span>")[1].split("<span")[0].strip()
    #print(date)
    year = date.split(" ")[2].strip(';')
    if year in count.keys():
        print("plus")
        count[year] = 
    else:
        count[year] = 1
    
    count[year] = 1
    print(count)


# print("[ Author: " + author + " ]")
# for r in result:
#     title = r.split("title is-5 mathjax\">")[1].split("</p>")[0].strip()
#     print(title)
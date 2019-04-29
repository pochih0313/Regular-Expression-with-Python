import urllib.request
import re
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import time

s = input("input author name: ")
s = s.split(" ")
s[0] = s[0].replace(",","%2C")
author = "%s"%s[0].capitalize()
for i in range(len(s)-1):
    s[i+1] = s[i+1].replace(",","%2C")
    author = author + "+%s"%s[i+1].capitalize()
print("[ Author: %s ]" % author)

url = "https://arxiv.org/search/?query=" + author + "&searchtype=author"
content = urllib.request.urlopen(url)
html_str = content.read().decode('utf-8')
pattern1 = 'has-text-black-bis has-text-weight-semibold\">Submitted[\s\S]*?<span'
pattern2 = "<a href=\"/search/\?searchtype=author&amp;query=[\s\S]*?</a>"
count = {}
count_coauthor = {}
next_page_num = 0

while(1):
    result1 = re.findall(pattern1, html_str)
    result2 = re.findall(pattern2, html_str)
    for r in result1:
        date = r.split("has-text-black-bis has-text-weight-semibold\">Submitted</span>")[1].split("<span")[0].strip()
        year = date.split(" ")[2].strip(';')
        if year in count.keys():
            #print("plus")
            count[year] += 1
        else:
            count[year] = 1
    #print(count)
    
    for r in result2:
        name = r.split("\">")[1].split("</a>")[0].strip()
        name1 = r.split("query=")[1].split("\">")[0].strip()
        temp = name.split(' ')
        name2 = "%s"%temp[0]
        for i in range(len(temp)-1):
            name2 = name2 + "+%s"%temp[i+1]
        #print(name)
        # print(name1)
        # print(name2)
        if ((author != name1) & (author != name2)):
            if name in count_coauthor.keys():
                count_coauthor[name] += 1
            else:
                count_coauthor[name] = 1
            #print (count_coauthor)
            #time.sleep(1)

    next_url = []
    next_u = ""
    next_page_num += 50
    next_url_pattern = "start="+str(next_page_num)+"[\s\S.]*?class=\"pagination-next\" >Next"
    next_url = re.findall(next_url_pattern, html_str)
    if(next_url):
        next_u = "https://arxiv.org/search/?query="+author+"&searchtype=author&abstracts=show&order=-announced_date_first&size=50&start="+next_url[0].split("start=")[1].split("\"")[0]
        #print(next_u)
        next_content = urllib.request.urlopen(next_u)
        html_str = next_content.read().decode('utf-8')
    else:
        break

### Question 1 ###
print(count)
list1 = list(count.keys())
list2 = list(count.values())
plt.bar(list1,list2)
plt.show()

### Question 2 ###
co_list = sorted(count_coauthor)
for i in range(len(co_list)):
    print("[ %-29s ]: %2d times" % (co_list[i], count_coauthor[co_list[i]]))
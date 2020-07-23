from selenium import webdriver
import time
import sys
import pandas as pd
from pandas import ExcelWriter
import os.path
import csv
import unidecode

driver = webdriver.Chrome()
#instagram link here
driver.get("https://www.instagram.com/p/CC2cg-ml7SN/")
time.sleep(3)

with open('churches.csv', newline='',encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    churches = list(reader)
print(str(churches[-1]).lower())
numchurches=len(churches)
print(numchurches)

#if user not logined
try:
    close_button = driver.find_element_by_class_name('xqRnw') 
    close_button.click()
except:
    pass


try:
    load_more_comment = driver.find_element_by_css_selector('.MGdpg > button:nth-child(1)')
    print("Found {}".format(str(load_more_comment)))
    i = 0
    # Number of times to try and load more comments
    while load_more_comment.is_displayed() and i < int(100):
        load_more_comment.click()
        time.sleep(1.5)
        load_more_comment = driver.find_element_by_css_selector('.MGdpg > button:nth-child(1)')
        print("Found {}".format(str(load_more_comment)))
        i += 1
except Exception as e:
    print(e)
    pass


#create lists for the usernames, comments and the church
user_names = []
user_comments = []
user_churches=[]

comment = driver.find_elements_by_class_name('gElp9 ')

#for each comment that is int he list we are going to proceess and separate byb comment and name
for c in comment:
    container = c.find_element_by_class_name('C4VMK')
    name = container.find_element_by_class_name('_6lAjh').text
    content = container.find_element_by_tag_name('span').text
    content = content.replace('\n', ' ').strip().rstrip()

    user_names.append(name)
    user_comments.append(content)   

#for each comment that has been processed we are going to see if there is a church from the list and add add it to the list of churches
for comment in user_comments:
    nochurch = True
    #remove the accents of the string and make it all lowercase
    unaccented_string = unidecode.unidecode(comment)
    currentcomment=str(unaccented_string).lower()
    #print("\n",currentcomment)

    #loop through the list of churches and see if they are found in the comment
    for church in churches:
        #set as lower case
        currentchurch= str(church[0]).lower()
        #print(currentchurch)

        #check for the church  in the comment and if exists add to the list
        if((currentchurch in currentcomment)):
            print("\n",currentchurch)
            print(currentcomment)
            nochurch= False
            user_churches.append(str(church[0]))
            break
        #check for the church  in the comment and if exists without any spaces add to the list
        if ((currentchurch.replace(" ", "")) in currentcomment):
            print("\n",currentchurch.replace(" ", ""))
            print(currentcomment)
            nochurch= False
            user_churches.append(str(church[0]))
            break

        #if the tests fail and no church is found by the end of the lists set nochurch to be true and break
        if(currentchurch.lower()==str(churches[-1]).lower):
            print("\n",str(churches[-1]).lower)
            print(currentchurch)
            nochurch=True
            break

    #is no church then add a new church to the list
    else:
        if(nochurch):
            nochurch=False
            user_churches.append("NoChurchFound")


      
        
#remove the headers
user_names.pop(0)
user_comments.pop(0)
user_churches.pop(0)

#create excel file
print("Names:", len(user_names),"\nComment: ", len(user_comments),"\nChurches: ",len(user_churches))
fname = 'comments.xlsx'
temp = {'name':user_names, 'comment': user_comments, "Church": user_churches}
df = pd.DataFrame(temp)
writer = ExcelWriter(fname)
df.to_excel(writer, 'comments', index=False)
writer.save()
driver.close()

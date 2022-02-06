#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


import re
def solution(new_id):
    answer = ''


# In[ ]:


#Level_1
new_id = new_id.lower()


# In[ ]:


#Level_2
new_id = re.sub('[^0-9a-z._-]','',new_id)


# In[ ]:


#Level_3
 new_id = re.sub('[.]{2,}','.',new_id)


# In[ ]:


#Level_4
new_id = re.sub('\A[.]|[.]\Z','',new_id)


# In[ ]:


#Level_5
if len(new_id) == 0 :
    new_id = 'a'


# In[ ]:


#Level_6
elif len(new_id) >= 16 :
    new_id = re.sub('[.]\Z','',new_id[:15])


# In[ ]:


#Level_7
while len(new_id) < 3 :
    new_id = new_id + new_id[-1]


# In[ ]:


answer = new_id
return answer


# In[ ]:


#Study
# re = regular expression 정규표현식
# replace : a=>b , re.sub : a(조건)=>b 
# re.sub(pattern,NEW_text,text)
# text에서 패턴일치부분을 NEW_text로 치환


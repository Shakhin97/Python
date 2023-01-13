#!/usr/bin/env python
# coding: utf-8

# In[14]:


talaba = {'ism': 'Korakhanov Shakhirddin', 'yosh':25, 't_yil':1997}
print(f"{talaba['ism'].title()},        {talaba['t_yil']} - yilda tug'ilgan,         {talaba['yosh']} yoshda")


# In[15]:


talaba


# In[16]:


talaba['kurs'] = 'Bitirgan'


# In[17]:


talaba


# In[18]:


talaba['Fakultet'] = 'Gidromelioratsiya'


# In[19]:


talaba['Viloyati'] = 'Qashqadaryo'


# In[20]:


talaba


# In[21]:


handy = {'ali':'Iphone X',
         'Vali':'Iphone 11 Pro Max',
         'Shakhin':'Iphone 13 Pro Max',
         'Baha':'Redmi 11 Pro',
         'Sardor':'Galaxy S21' 
    
}


# In[22]:


handy


# In[34]:


handys = handy.get('Shakhin', 'Bunday ism mavjud emas') #  get methodi agar kalit soz topilmasa ikkinch qiymatni yani bunday ism mavjud emasni chiqaradi


# In[35]:


print(handys)


# In[ ]:





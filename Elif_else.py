#!/usr/bin/env python
# coding: utf-8

# In[5]:


hungry = True
if hungry:
    print('FEED ME!')
else:
    print("Im not hungry")


# In[18]:


i = 1
fact = 1
n  = int(input("N="))
while i<=n:
    fact = fact*i
    i = i+1
    print(str(n)+"!="+str(fact))


# In[19]:


loc = 'Game'
if loc == 'Auto Shop':
    print("Cars are coll!")
elif loc == 'Bank':
    print("Money is cool!")
elif loc =='Store':
    print("Welcome to the Store")
else:
    print("i do not know much ")


# In[23]:


name = 'Shakhriddin'
if name == "Bahriddin":
    print("Hallo Bahriddin")
elif name == 'Shakhriddin':
    print('Hallo Shakhriddin')
else:
    print('Du kannst mich mall')


# In[24]:


a =5
a==5


# In[27]:


a!=5


# In[28]:


ism = 'Ali'
ism = input('Ismingizni nima?\n>>>')
if ism.lower() != 'ali':
    print(f"Uzr, {ism.title()}, biz Alini kutayapmiz.")
else:
    print("Salom Ali")
ism.lower() == 'ali'


# yosh = int(input('Yoshingiz nechchida?'))
# if yosh<=5:
#      print("Siz uchun kirish bepul.")
# elif yosh <=12:
#      print("Siz uchun kirish narxi: 5000 so'm")
# elif yosh <=18:
#      print("Siz uchun kirish narxi: 8000 so'm")
# else:
#      print("Siz uchun kirish narxi : 1000 so'm")

# In[39]:


kun = input("Bugun nima kun?")
harorat = float(input('Havo harorati qanday?'))
if (kun.lower()== 'yakshanba' or kun.lower()== 'shanba') and harorat>=30:
    print("Cho'milgani ketdik! ")
elif kun.lower()== 'yakshanba' or kun.lower()== 'shanba' and harorat <30:
    print("Uyda qolamiz")


# In[40]:


kun == 'Juma'


# In[44]:


narh = 15000
choy = True
salat = True
non = True
kompot = False
assorti = False

if choy:
    print("Mijoz choy sotib oldi")
    narh = narh + 2000
if salat:
    print("Mijoz salat sotib oldi")
    narh = narh + 3000
if non:
    print("Mijoz non sotib oldi")
    narh = narh + 2000
if kompot:
    print("Mijoz kompot sotib oldi")
    narh = narh + 5000
if assorti:
    print("Mijoz assorti sotib oldi")
    narh = narh + 5000

print(f"Jami {narh} so'm")


# In[1]:


mylist = [(1,2),(3,4),(5,6), (7,8)]


# In[3]:


mylist


# In[4]:


len(mylist)


# In[8]:


for (a,b) in mylist:
    print(b)
    


# In[14]:


#while operatori bilan ishlaymiz
x = 0
while x<5:
    print(f" x ning qiymati  {x} ga teng boladi")
    x=x+1


# In[15]:


print( "Hello World!")


# In[17]:


print("O'ngacha sanaymiz")
for n in range(10):
    print(n+1)


# In[20]:


son = 50
if son>=0:
    print("Musbat son")
else:
    print("Manfiy son")


# In[22]:


son = int(input("Istalgan son kiriting: "))
print(f"{son} ning kvadrati {son**2} ga teng")


# In[ ]:





# In[ ]:





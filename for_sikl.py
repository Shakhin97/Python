#!/usr/bin/env python
# coding: utf-8

# In[5]:


mehmonlar = ['Shahriddin','Doston', 'Sardor', 'Aminbek', 'Elyor', 'Farruh', 'Shahzod', 'Xojiakbar', 'Xumoyun' ]
for mehmon in mehmonlar:
    print(f"Assalom alekum Hurmatli {mehmon}, sizni 3-oktabr kungi bayramga taklif qilamiz")
    print('Xurmat bilan Shakhriddin Korakhanov')
    


# In[8]:


sonlar = list(range(1,11))
for son in sonlar:
    print(f"{son} ning kvadrati =  {son**2} ga teng bo'ladi   ")


# In[13]:


sonlar_kvadrati = []
for son in sonlar:
    sonlar_kvadrati.append(son**2)
print(sonlar)
print(sonlar_kvadrati)


# In[14]:


dostlar = []
print("5 ta eng yaqin do'stingizni kiriting")
for n in range(5):
    dostlar.append(input(f"{n+1}- do'stingizni ismini kiriting: "))
print(dostlar)    
    


# In[16]:


sabzavotlar = ['kartoshka','sabzi','bodring','pomidor','lavlagi']
for sab in sabzavotlar:
    print(f"Kep qoling bugun {sab}ning narxi juda arzon bo'lib ketdi")


# In[18]:


for n in range(5):
    print(f"Kod {n+1} marta takrorlandi")


# In[30]:


toq = list(range(11,100,+2))


# In[ ]:





# In[33]:


for kub in toq:
    print(kub**3 )


# In[34]:


kinolar = []
print("Eng sevimli kinoyingizni kiriting:")
for n in range(5):
    kinolar.append(input(f"{n+1} kinoning nomini kiriting:"))
print(kinolar)    


# In[36]:


n_people = int(input("Bugun necha kishi bn suhbat qildingiz?>>>"))

suxbat = []
print("Bugun kim bilan ko'rishdingiz")
for n in range(n_people):
    suxbat.append(input(f"{n+1}-tanishgan insoningizni ismini kiriting:"))
print(suxbat)    


# In[ ]:





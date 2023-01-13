#!/usr/bin/env python
# coding: utf-8

# In[1]:


def salom_ber():
    """Salom ber degan funksiya"""
    print("Assalom alekum")
salom_ber()


# In[4]:


def salom_ber(ism):
    """Salom ber degan funksiya, foydalanuvchining ismini so'rab unga salom beradi
    """
    print(f"Assalom alekum , hurmatli {ism.title()}")
salom_ber('Shahin')


# In[11]:


def user( ism ,familiya, t_yil, j_yil=2022):
    """Userning ism familiyasi va tug'ilgan yilini hisoblaydi"""
    print(f"Assalom alekum , hurmatli {ism.title()}")
    print(f"Xush kelibsiz , hurmatli {ism.title()} {familiya.title()}")
    print(f"Siz {j_yil -t_yil} yoshda ekansiz")
user('Shahriddin', 'Korakhanov',1997)


# In[26]:


def kv(son):
    """sonning kvadratini hisoblaymiz"""
    print(f"{son} ning kvadrati {son**2} ga teng")
    print(f"{son} ning kubi esa {son**3} ga teng")
kv(5)


# In[30]:


def juft_toq(son): 
    """sonning juft yoki toqligini tekshiradi"""
    print(f"{son%2==0} bo'lsa juft {son%2!=0} toq bo'ladi ")
juft_toq(15)  


# In[40]:


def juftmi(son):
    if son%2:
        print(f"{son} toq bo'ladi")
    else:
        print(f"{son} juft bo'ladi")
juftmi(156)


# In[43]:


def sonlar(son1, son2):
    """Sonlar bir biriga tengligini tekshiradi"""
    if son1==son2:
        print("Sonlar bir biriga teng")
    else:
        print("Boshqa son kirit!")
sonlar(3,3)


# In[48]:


def son(x,y):
    print(f" x = {x} ning qiymatini {y} darajaga oshiramiz javobi = {x**y} nechiga tengligini ko'rsatadi")
son(8,3)


# In[49]:


# Foydalanuvchidan son qabul qilib, sonni 2, 3, 4 va 5 ga qoldiqsiz bo'linishini tekshiruvchi 
# funksiya yozing. 
# Natijalarni konsolga chiqaring ("15 soni 3 ga qoldiqsiz bo'linadi" ko'rinishida)
def bolinish_alomatlari(son):
    for n in range(2,11):
        if not son%n:
            print(f"{son} {n} ga qoldiqsiz bo'linadi")

bolinish_alomatlari(20)


# In[63]:


def oraliq(kam,kop):
    sonlar = []
    while kam<kop:
        sonlar.append(kam)
        kam=kam+1
    return sonlar
print(oraliq(1,5))


# In[65]:


sonlar = oraliq(0,9)


# In[66]:


print(sonlar)


# In[69]:


def toliq_ism_yasa(ism, familiya):
    """To'liq ism qaytaruvchi funksiya"""
    toliq_ism = f"{ism} {familiya}"
    return toliq_ism
talaba=toliq_ism_yasa('Shahriddin', 'Korakhanov')


# In[70]:


print(talaba)


# In[74]:


talaba1 = toliq_ism_yasa('Rustam' ,'Adhamov')
talaba2 = toliq_ism_yasa("Madina","Yusupaliyeva")
print(f"Semestrni 5 bahoga tamomlagan {talaba1} va {talaba2}ga 1 mln so'm stipendiya berilsin")


# In[92]:


def toliq_ism(ism, familiya , sharif=''):
    if sharif:
        toliq = f"{ism} {sharif} {familiya}"
    else:
        toliq = f"{ism} {familiya}"
    return toliq.title()
rus = toliq_ism('rustam','adhamov','botirovich')
mad = toliq_ism('madina','yusupaliyeva')
print(f"O'quv tilini 5 bahoga yopgan {rus} va {mad}larga 1 mln so'm pul bering ")


# In[93]:


def avto_info(kompaniya, model, rangi, karobka,yili,narhi=None):
    avto ={
        'kompaniya':kompaniya,
        'model': model,
        'rang': rangi,
        'karobka':karobka,
        'yil': yili,
        'narx': narhi
    }
    return avto
avto1= avto_info('GM','Malibu','qora','avtomat',2020,35000)
avto2= avto_info('BMW','M7','kulrang','avtomat',2022)
avtolar = [avto1, avto2]
print("Bozordagi mavjud mashinalar")
for avto in avtolar:
    if avto['narx']:
        narx = avto['narx']
    else:
        narx = "No'malum"
    print(f"{avto['rang']} {avto['model']}. Narxi = {narx} $ da")


# In[130]:


def oraliq(min , max , qadam =''):
    sonlar = []
    qadam = []
    while min<max:
        sonlar.append(min)
        min+=1 
    return sonlar
print(oraliq(1,15,1))


# In[145]:


print("Saytimizdagi avtolar ro'yhatini shakllantiramiz:")
avtolar=[]
while True:
    print("\n Quyidagi ma'lumotlarni kiriting",end ='')
    kompaniya=input("Ishlab chiqaruvchi: ")
    model = input("Modeli: ")
    rang = input('Rangi: ')
    karobka = input("Karobka: ")
    yil = input('Yili: ')
    narx = input('Narxi: ')
    avtolar.append(avto_info(kompaniya, model, rang, karobka,yil, narx))
    javob = input("Yana avto qo'shasizmi? (yes/no): ")
    if javob == 'no':
        break
print("\nSalonimizdagi avtolar: ")
for avto in avtolar:
    if avto['narx']:
        narx= avto['narx']
    else:
        narx= "No'malum"
    print(f"{avto['rang'].title()} {avto['model'].title()},{karobka} karobka. Narhi: {narx}")


# In[146]:


print(avtolar)


# In[158]:


name= input("Ismingizni kiiting: ")
if name=='Akmal':
    print("Salom Akmal Kadirov")
elif name == 'Kadirov':
    print("Salom Akmal Kadirov")
elif name =="Rustam":
    print('Salom Rustam Ahmedov')
else:
    print("Salom kim bo'lsang ham")


# In[159]:


oylar =list(range(1,13))


# In[160]:


oylar


# In[172]:


pip install pandas


# In[167]:


import pandas as pd


# In[174]:


import pandas as pd
oylar= [{'Yanvar':31, 'Fevral':28,'Mart':31, 'Aprel':30,'May':31,'Iyun':30,'Iyul':31,'Avgust':31,'Sentabr':30,'Oktyabr':31,'Noyabr':30,'Dekabr':31}]
df = pd.DataFrame(oylar)


# In[175]:


import numpy as np


# In[ ]:





# In[ ]:





# In[ ]:





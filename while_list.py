#!/usr/bin/env python
# coding: utf-8

# In[3]:


print("Yaqin do'stlar ro'yhatini tuzamiz")
ismlar =[]
n=1
while True:
    savol = f"{n}-do'stingizni ismini kiriting: "
    ism = input(savol)
    ismlar.append(ism)
    takrorlash = input("Yana ism qo'shasizmi? (ha/yo'q)")
    n+=1
    if takrorlash !="ha":
        break
print("Do'stlaringiz ro'yhati: ")
for ism in ismlar:
    print(ism.title())


# In[4]:


print("Do'stlaringiz yoshini saqlaymiz: ")
dostlar ={}
ishora = True
while ishora:
    ism= input("Do'stingizni ismini kiritng: ")
    yosh = input(f"{ism.title()}ning yoshini kiriting: ")
    dostlar[ism]= int(yosh)
    
    javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
    if javob == "yo'q":
        ishora = False
for ism , yosh in dostlar.items():
    print(f"{ism.title()} {yosh} yoshda")


# In[7]:


talabalar = ['Rustam','Lochin','Ilyos','Feruza', 'Madina', 'Shahriddin', 'Davron', 'Sardor','Olim','Ilhom']
baholangan_talabalar = {}
while talabalar:
    talaba = talabalar.pop()
    baho = input(f"{talaba.title()}ning bahosini kiriting: ")
    print(f"{talaba.title()} baholandi! ")
    baholangan_talabalar[talaba] = int(baho)


# In[9]:


print("Mahsulotlar ro'yhatini tuzamiz: ")
savat = []
while True:
    tovar = input("Savatga mahsulotingiz qo'shing!: ")
    savat.append(tovar)
    javob = input("Yana mahsulot qo'shasizmi. (ha/yo'q): ")
    if javob != 'ha':
        break
    


# In[10]:


buyurtmalar = ['olma','anjir','uzum','qovun']
mahsulotlar = {'olma':20000,
               'shaftoli':25000,
               'tarvuz':18000,
               'uzum':22000}

while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narh = mahsulotlar[buyurtma]
        print(f"{buyurtma.title()} - {narh} so'm")
    else:
        print(f"Bizda {buyurtma} yo'q")


# In[ ]:





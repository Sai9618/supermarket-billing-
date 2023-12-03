from datetime import datetime
print(25*"*","SAI KUMAR MART",25*"*")
name=input("enter your name:")
#list of items
lists= '''
Rice    Rs 40/kg
sugar   Rs 50/kg
salt    RS 20/kg
Oil     Rs 1100/liter
paneer  Rs 110/kg
Maggi   Rs 50/kg
Boost   Rs 90/each
Colgate Rs 85/each
'''
#declaration
price=0
pricelist=[]
Totalprice=0
Finalfinalprice=0
ilist=[]
qlist=[]
plist=[]

#rates for items
items={'rice':40,
'sugar':50,
'salt':20,
'Oil':110,
'paneer':110,
'Maggi':50,
'Boost':90,
'Colgate':85}
option=int(input('for list of item press 1:'))
if option==1:
    print(lists)
    for i in range(len(items)):
        inp1=int(input('if you want to buy press 1 or 2 for exit:'))
        if inp1==2:
            break
        if inp1==1:
            item=input('enter your item:')
            quantity=int(input("enter quantity:"))
            if item in items.keys():
                price=quantity*(items[item])
                pricelist.append((item,quantity,items,price))
                Totalprice+=price
                ilist.append(item)
                qlist.append(quantity)
                plist.append(price)
                gst=(Totalprice*6)/100
                finalamount=gst+Totalprice
            else:
                print("sorry you entered item is not available now:")
        else:
            print("you entered wrong number")
        inp=input("can i bill the items for press yes or no:")
        if inp=='yes':
            pass
            if finalamount!=0:
                print(25*"=","SAI KUMAR MART",25*"=")
                print(28*' ',"Nellore")
                print("Name:",name,30*" ",'Date:',datetime.now())
                print(75*"=")
                print("sno",8*" ",'items',8*" ",'quantity',4*' ','price')
                for i in range(len(pricelist)):
                    print(i,8*' ',3*' ',ilist[i],6*' ',qlist[i],11*' ',plist[i])
                    print(75*"=")
                    print(50*' ','Totalamount:','Rs',Totalprice)
                    print("get amount",50*" ",gst)
                    print(50*" ",'finalamount:','Rs',finalamount)
                    print(75*"=")
                    print(50*" ",'thanks for visiting')
                    print(50*" ",'please visit again')
#chapter3
name=input("enter your name:")
print(name +" "+ "Good Afternoon")



letter= """ Dear <|Name|>,
YOu are selected!
Date:<|date|> """

name=input("enter Name")
date=input("enter Date")
letter=letter.replace("<|Name|>",name)
letter=letter.replace("<|date|>",date)
print(letter)

st="this is a string with double spaces"
print(st.find(" "))

sts="this   is double spaced"
sts=sts.replace(" ", " ")
print(sts)

letter2="Hey sheer,\n this your python course.\n thank you!"
print(letter2)



#chapter4
sheer=[]
sheer.append(24)
sheer.append(5)
sheer.append(8)
sheer.append(20)
sheer.append(18)
sheer.append(6)
sheer.append(15)
sheer.append(10)

print(sheer)


marks=[50,80,40,80,60,30,57]
marks.sort()

print(marks.count(80))

nums=[4,7,9,8]
total=sum(nums)
print(f"sum={total}")


q=(4,0,0,8,7,6,0)
print(f"zeroes count={q.count(0)}")


she=(1,2,3)
she[0]=100
print(she)


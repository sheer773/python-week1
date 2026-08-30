#chapter5
dict={
   "good morning":"subodayam",
   "morning":"udhayam",
   "good":"manchidi",
}
print(dict["morning"])


s=set()
s.add(1)
s.add(3)
s.add(1)
print(s)

s={11,"11"}
print(len(s))


s={11, 11.0, "11"}
print(len(s))

 
s={}
print(type(s))
s=set()
print(type(s))
s=[]
print(type(s))


lang={}
lang["sheer"]="telugu"
lang["she"]="english"
print(lang)


#chapter6
a=40
b=3
c=78
d=20
if a>b and a>c and a>d:
    print("a is biggest")
elif b>a and b>c and b>d:
    print("b is biggest")
elif c>a and c>b and c>d:
    print("c is biggest")
else:
    print("d is biggest")

sub1=70
sub2=90
sub3=40
total=(sub1+sub2+sub3)/3
if(sub1>33 and sub2>33 and sub3>33 and total>=40):
    print("Pass")
else:
    print("Fail")

text="this is text"
if("this is " in text or "buy" in text):
    print("spam")

post =" I am learning from Harry bhai"
if "harry" in post.lower():
    print("yes")

friends=["rani","raji","her"]
if "raji"  in friends:
    print("yes")

name="sheeruu"
if len(name)<10:
    print("<10 chars")
else:
    print(">=10 chars")
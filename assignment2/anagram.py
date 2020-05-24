s1=str(input("enter string"))
s2=str(input("enter string 2"))

def check(s1,s2):
  if sorted(s1)==sorted(s2):
    print("anagrams")
  else:
    print("Not anagrams")
    
check(s1,s2)

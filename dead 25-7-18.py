
# coding: utf-8

# In[ ]:


def dead(a,b):
    if a == "female":
        return b+87
    elif a == "male":
        return b+85
    else:
        print("Unknown gender input...")
        return b+86
a = input("Are you Male or Female? ").lower()
b = int(input("I was born in the year: "))
print("You'll probably die around the year", dead(a,b))
delay = input("Press enter to finish")


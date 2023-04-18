from about import me

print(me)

print(me["name"])

name = me["name"]
last = me["last_name"]
print(name +  " " + last)

# add 
me["age"] = me["age"] + 1
print(me)

#add
me["preferred_color"] = "green/pink"
print(me)

age = me["age"]
print(name + ": " + str(age))

# string format
print(f"{name}: {age}")

# delete a key from dict
del me["age"]


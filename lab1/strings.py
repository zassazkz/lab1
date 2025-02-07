a = "Hello, World!"
print(a[1])

for x in "banana":
  print(x)

a = "Hello, World!"
print(len(a))

txt = "The best things in life are free!"
print("free" in txt)

txt2 = "The best things in life are free!"
if "free" in txt2:
  print("Yes, 'free' is present.")

b = "Hello, World!"
print(b[2:5])


c = "Hello, World!"
print(c.lower())


d = " Hello, World! "
print(d.strip()) # returns "Hello, World!"


e = "Hello, World!"
print(e.split(",")) # returns ['Hello', ' World!']



price = 59
txt3 = f"The price is {price:.2f} dollars"
print(txt3)
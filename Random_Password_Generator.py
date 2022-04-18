import random
while True:
    passlen=int(input("Enter the Length of Password:-"))
    x="abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ~@#$%^&*()_<>+<>?"
    password="".join(random.sample(x,passlen))
    print(password)

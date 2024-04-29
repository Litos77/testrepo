for num_bottles in range(99, 0, -1):
    print(f"{num_bottles} bottles of beer on the wall.")
    print(f"{num_bottles} bottles of beer.")

    if num_bottles == 1:
        print(f"Take one down, pass it around, no more bottles of beer on the wall.")
    else:
        print(f"Take one down, pass it around, {num_bottles - 1} bottles of beer.")
    print('*' * 50)

# with a while loop 

num_bottles = 99

while num_bottles > 0:
    print(f"{num_bottles} bottles of beer on the wall.")
    print(f"{num_bottles} bottles of beer.")

    if num_bottles == 1:
        print(f"Take one down, pass it around, no more bottles of beer on the wall.")
    else:
        print(f"Take one down, pass it around, {num_bottles - 1} bottles of beer.")
    print('*' * 50)
    num_bottles -= 1
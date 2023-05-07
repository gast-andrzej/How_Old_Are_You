def How_Years_You_Old(z=int(input("what year were you born in? "))): return print(f"You are {int(__import__('datetime').date.today().year)-z} years old.")
How_Years_You_Old()
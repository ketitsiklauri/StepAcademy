# მონაცემთა ტიპები და type()
age = 25                
height = 1.78       
name = "ნინა"        
is_student = True   

# მათემატიკური ოპერაციები
print(type(age))
print(type(height))
print(type(name))
print(type(is_student))


# ორი რიცხვის შეყვანა
first = float(input("შეიყვანეთ პირველი რიცხვი: "))
seccond = float(input("შეიყვანეთ მეორე რიცხვი: "))

# მათემატიკური ოპერაციები
print(first + seccond)
print(first - seccond)
print(first * seccond)
print(first / seccond)
print(first // seccond)
print(first % seccond)
print(first ** seccond)

# სახელისა და გვარის შეყვანა
first_name = input("შეიყვანეთ სახელი: ")
last_name = input("შეიყვანეთ გვარი: ")

# სრული სახელი
full_name = first_name + " " + last_name

print(full_name)
print(full_name.upper())
print(full_name.lower())
print(full_name.capitalize())

# sep: სიტყვებს შორის გამყოფი (ნაგულისხმევია ინტერვალი)
print("to be", "or", "not to be", sep="-")
print(1, 2, 3, 4, sep="***")
print("ქეთი", "წიკლაური", "36", sep="\t")

# end: ბეჭდვის ბოლოს დამატებული სიმბოლო (ნაგულისხმევია \n, ანუ ახალი ხაზი)
print(end=" | ")
print(end=" | ")
print(end="!!!\n")

age = 36
height = 1.69
is_student = False

# შედარების ოპერატორები
print(age, "== 18 =", age == 18)
print(age, "!= 18 =", age != 18)
print(age, "> 18 =", age > 18)
print(age, "< 18 =", age < 18)
print(age, ">= 20 =", age >= 20)
print(age, "<= 19 =", age <= 19)

print()  

# ლოგიკური ოპერატორები
print("age > 18 and is_student =", age > 18 and is_student)
print("height > 1.80 and is_student =", height > 1.80 and is_student)
print("height > 1.80 or is_student =", height > 1.80 or is_student)
print("not is_student =", not is_student)
print("not (age < 18) =", not (age < 18))

# მონაცემების შეყვანა
name = input("შეიყვანეთ სახელი: ")
age = int(input("შეიყვანეთ ასაკი: "))
height = float(input("შეიყვანეთ სიმაღლე (მეტრებში): "))

# ტიპების შემოწმება (სურვილისამებრ)
print(type(name), type(age), type(height))

# მისალმება
print("გამარჯობა,", name + "!")
print("თქვენ ხართ", age, "წლის და თქვენი სიმაღლეა", height, "მეტრი.")

N = int(input())
age_arr = []
name_arr = []
for _ in range(N):
    age, name = input().split()
    age = int(age)

    if age_arr == []:
        age_arr += [age]
        name_arr += [name]
    elif len(age_arr) == 1 and age_arr[0] > age:
        age_arr.insert(0, age)
        name_arr.insert(0, name)
    else:
        for i in range(1, len(age_arr)):
            if age_arr[0] > age:
                age_arr.insert(0, age)
                name_arr.insert(0, name)
                break
            elif len(age_arr) >= 2 and age_arr[i-1] <= age < age_arr[i]:
                age_arr.insert(i, age)
                name_arr.insert(i, name)
                break
        else:
            age_arr += [age]
            name_arr += [name]

for j in range(N):
    print(f'{age_arr[j]} {name_arr[j]}')

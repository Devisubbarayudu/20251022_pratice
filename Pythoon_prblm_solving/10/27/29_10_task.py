emp_name=["deviya","ramya","lethi","chithra"]
emp_sal=[2000,1500,3000,3000]
max=emp_sal[0]
for i in range(1,len(emp_sal)):
    if emp_sal[i]>max:
        max=emp_sal[i]
for i in range(len(emp_name)):
    if max==emp_sal[i]:
        print(emp_name[i])
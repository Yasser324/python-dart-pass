"""
Q1;

An error in naming the method, before which the type of this method must be added ===>(VOID)

"""

class Myclass:
    def Print_EO(self):
        rang=int(input("Enter the range :"))
        arr=[]
        for i in range(rang):
            b=int(input(f"Enter the Value #{i} :"))
            arr.append(b)
        for j in arr:
            if j %2==0:
                print(f"The {j} Even ")
            else:
                print(f"The {j} odd")
obj=Myclass()
obj.Print_EO()


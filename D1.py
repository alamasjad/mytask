from datetime import date

class UserData:
    data={}
    def __init__(self,Name,DOB):
        self.Name=Name
        self.DOB=DOB
        self.data[self.Name]=self

    def Show_Age(self):
        self.tdate=date.today()
        self.tyear=date.today().year
        self.age_in_days=self.tdate-self.DOB
        self.age_in_years=self.tyear-self.DOB.year
        print(f"{self.Name} Your age in days are: {self.age_in_days}")
        print(f"{self.Name} Your age in days are: {self.age_in_years}")


def take_input(ans):
    while ans:
        name=input('Enter Your Name:')
        year=int(input('Enter Your Year of Birth:'))
        month=int(input('Enter Your Month of Birth:'))
        day=int(input('Enter Your Day of Birth:'))
        dob=date(year,month,day)
        u1=UserData(name,dob)
        u1.Show_Age()
        ans=int(input("Enter 1 To Continue and 0 To Stop:"))
    return

take_input(1)



        
import csv


class compute_average:
    def __init__(self,name,math,science,english):
        self.name=name
        self.math=math
        self.science=science
        self.english=english
        self.average=(self.math+self.science+self.english)/3


    def write(self):
        with open('D4_output.csv','a',newline="") as file2:
            writer=csv.writer(file2)
            if file2.tell() == 0:
                writer.writerow(['Name', 'Average'])
            writer.writerow([self.name,self.average])


#object creation
with open('D4_grades.csv','r') as file:
    data=csv.reader(file)
    for i,row in enumerate(data):
        print(row)
        if i==0:
            continue
        try:
            std=compute_average(row[0],int(row[1]),int(row[2]),int(row[3]))
            std.write()
        except (TypeError, IndexError,ValueError) as e:
            print(f"Error: {e}")
            print("Please Enter Marks of All The Subjects")
            print("Your marks will be zero By Default")
            std=compute_average(row[0],1,1,1)
            std.write()
        
"""This project helps me learn multiple things like
specially about errors"""
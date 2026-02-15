def student_result(name,*marks):
    total_marks=0
    for i in marks:
        total_marks=total_marks+i
    if total_marks>=40:
        print("Pass")
    else:
        print("fail")
            
print(student_result('arun',50,45,22))



def salary_report(department,*salaries):
    count_salaries=0
    for i in salaries:
        if i>30000:
            count_salaries+=1
            
    if count_salaries>=3:
        print(f'{department} salary is {count_salaries}')
    else:
        print("sorry")
        
       
       
salary_report("Python",250000,20000,12000,12345)
salary_report("Django",30000)



def vote_result(candidates,*votes):
    yes_count=0
    no_count=0
    for i in votes:
         if i=='y':
             yes_count=yes_count+1
         elif i=='n':
             no_count=no_count+1
    if yes_count>no_count:
        print(f'{candidates} is the winner')
    else:
        print(f'{candidates} lost')
        
vote_result('arun','y','y','n','y')
vote_result("arjun",'n','n,','n')


def student_marks(**kwargs):
    for i in kwargs:
        marks=kwargs[i]
        if marks>=40:
            print(f'{i} pass')
        else:
            print(f'{i} fail')
            
student_marks(math=60,dsa=90,oop=30)
    
    
def salary(**kwargs):
    for i in kwargs:
        salary=kwargs[i]
        if salary>50000:
            print(f'{salary} is higher')
        else:
            print(f'{salary} is lower')
            
salary(name='arun',salary=40000)


def class_info(**kwargs):
    for i in kwargs:
        student_info=kwargs[i]
        if student_info==10:
            print(f'{i} is in {student_info}')
        elif student_info>10:
            print(f'{i} is in {student_info}')
            
class_info(arun=10,aakash=12)


def student(name, *marks, **details):
    print("Name:", name)
    print("Marks:", marks)
    if marks:
        avg = sum(marks) / len(marks)
    else:
        avg = 0
    print("Average:", avg)

    print("Details:")
    for key, value in details.items():
        print(key, ":", value)
student("Arun", 70, 80, 90, city="Kathmandu", age=20)



def bill(*items, **prices):
    total = 0
    for item in items:
        if item in prices:
            total += prices[item]
        else:
            print(item, "price not found")

    print("Total bill:", total)
bill("pizza", "burger", pizza=200, burger=150, coke=50)




    
    

            
        
from unicodedata import name

students=[("Alice",78),("Bob",45),("Charlie",90),("Diana",62),("Kent",30)]
def print_students(students):
    for student in students:
        name,score=student
        print(name,score)
        # return(name, score)
print_students(students)

def student_that_score_above_60(students):
    student_score_above_60=[student for student in students if student[1]>60]
    return student_score_above_60

print(student_that_score_above_60(students))

def student_that_passed(students):
    count=0
    for student in students:
        if student[1]>50:
            count+=1
    return count

print(student_that_passed(students))

products=[("Laptop",1200),("Mouse",25),("Keyboard",45),("Monitor",300),("USB Cable",10)]
def product_cost_more_than_100(products):
    def cost_more_than_100(products):
        return products[1] > 100
    product_cost_more_than_100=list(filter(cost_more_than_100,products))
    return product_cost_more_than_100
print(product_cost_more_than_100(products))

def sum_product_cost(products):
    sum=0
    for product in products:
        sum+=product[1]
    return sum
print(sum_product_cost(products))

def unpack_products_and_print(products):
    for product in products:
        product_name, product_price=product
        print(product_name,product_price)
    return
unpack_products_and_print(products)

points = [ (2, 3),(-1, 4),(5, -6),(0, 7),(-3, -2)]

def filter_the_positive_point(points):
    positive_points=[]
    for point in points:
        x_point, y_point=point
        if x_point > 0 and y_point > 0:
            positive_points.append((x_point, y_point))
    return positive_points
print(filter_the_positive_point(points))

employees = [("John", "IT", 50000),("Jane", "HR", 45000),("Mike", "IT", 60000),("Sara", "Finance", 70000)]
def filter_employees_list(employees):
    it_employees=[]
    it_employees_above_5500=[]
    for employee in employees:
        name, department, salary=employee
        if department=="IT":
            it_employees.append((name, department, salary))
    for employee in it_employees:
        name, department, salary=employee
        if salary>55000:
            it_employees_above_5500.append(name)
    return it_employees_above_5500
print(filter_employees_list(employees))




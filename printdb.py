from persistence import *

 
    

def main():
    #TODO: implement
    cur = repo._conn.cursor()
    
    
    #Activities
    print("Activities")
    a = cur.execute("SELECT * FROM activities ORDER BY date ").fetchall()
    
    for act in a:
       to_print = "("
       for i in act:
            
            if isinstance(i,int):
                to_print += str(i)+ ", "
            elif isinstance(i,bytes): 
                to_print += "'"+ str(i.decode()) +"')" 
     
       print(to_print)
        
        
        
    #Branches
    print("Branches")  
    b = cur.execute("SELECT * FROM branches ORDER BY id").fetchall()
    for branch in b:
        to_print = "("
        for i in branch:
            if isinstance(i,int):
                to_print += str(i) 
            elif isinstance(i,bytes): 
                to_print += ", '"+ str(i.decode()) +"', " 
        print(to_print + ")")
        
    #Employees
    print("Employees")
    c= cur.execute("SELECT * FROM employees ORDER BY id").fetchall()
    for emp in c:
        to_print = "("
        for i in emp:
            if isinstance(i,bytes):
                to_print += "'"+ str(i.decode()) +"', "
               # to_print += str(i) +", " 
            else: 
                to_print +=  str(i) +", "
        to_print = to_print[:-2]
        print(to_print + ")")
        
    #Products
    print("Products")
    d= cur.execute("SELECT * FROM products ORDER BY id").fetchall()
    for prod in d:
        to_print = "("
        for i in prod:
            if isinstance(i,bytes):
                to_print += "'"+ str(i.decode()) +"', "
               # to_print += str(i) +", " 
            else: 
                to_print +=  str(i) +", "
        to_print = to_print[:-2]
        print(to_print + ")")
        
    #Suppliers
    print("Suppliers")
    e= cur.execute("SELECT * FROM suppliers ORDER BY id").fetchall() 
    for sup in e:
        to_print = "("
        for i in sup:
            if isinstance(i,bytes):
                to_print += "'"+ str(i.decode()) +"', "
               # to_print += str(i) +", " 
            else: 
                to_print +=  str(i) +", "
        to_print = to_print[:-2]
        print(to_print + ")")
        


#     #Employees report
    print("Employees report")
    
    emp_rep = cur.execute("""SELECT employees.name, employees.salary, branches.location, SUM(-1*activities.quantity*products.price) as 'total_sales'
    FROM employees INNER JOIN branches ON employees.branche = branches.id
    LEFT JOIN activities on  employees.id = activities.activator_id
    LEFT JOIN products on activities.product_id = products.id
    GROUP BY employees.id
    ORDER BY employees.name;""").fetchall()

    for x in emp_rep:
        to_print = ""
        for i in x:
            if(i == None):
                to_print += "0 "
            elif isinstance(i,bytes):
                to_print += ""+ str(i.decode()) +" "
               # to_print += str(i) +", " 
            else: 
                to_print +=  str(i) +" "
        to_print = to_print[:-1]
        print(to_print )




    
    
    #activities report
    print("Activities report")
    
    act_rep = cur.execute("""SELECT activities.date, products.description, activities.quantity, employees.name, suppliers.name 
                         FROM  activities INNER JOIN products ON activities.product_id = products.id LEFT JOIN employees ON activities.activator_id = employees.id LEFT JOIN suppliers ON activities.activator_id = suppliers.id 
                          ORDER BY activities.date; """).fetchall()
    
    for z in act_rep:
        to_print = "("
        for i in z:
            if isinstance(i,bytes):
                to_print += "'"+ str(i.decode()) +"', "
               # to_print += str(i) +", " 
            else: 
                to_print +=  str(i) +", "
        to_print = to_print[:-2]
        print(to_print + ")")
    
    

if __name__ == '__main__':
    main()
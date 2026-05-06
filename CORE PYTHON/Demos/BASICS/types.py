#with passing parameter and with returning values
def emp(id,name,sal):
    id_str = f'ID = {id}'
    name_str = f'NAME = {name}'
    sal_str = f'SALARY = {sal}'

    return id_str,name_str,sal_str
i=101
nm='ABC'
s=15000
#to grt one returning value
res=emp(i,nm,s)
print(res)
#to get multiple returning value
res1,res2,res3 = emp(i,nm,s)
print(res1)
print(res2)
print(res3)
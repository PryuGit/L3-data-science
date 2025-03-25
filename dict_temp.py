#asks for avg temperature of each day and display in dictionary form
def get_daily_temp():
    dict={}
    for x in range(7):
        key=input("enter day of the week:")
        value=float(input('enter temp:'))
        dict[key]=value
    return dict

d=get_daily_temp()
print(d)

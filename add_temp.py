#adding temperature and day in dictionary
def add_daily_temps(day,temp):
    if day not in dict:#checking whether the day is present
        dict[day]=temp
    return dict
dict={'monday':24,'tuesday':23,'wednesday':25}
print(dict)
#adding new values
update=add_daily_temps('thursday',23)
print(update)

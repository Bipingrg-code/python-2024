import time
# import nepali_datetime 

print(time.ctime(100000))  #convert a time expressed in  seconds since epoch to a readable string
                            #epoch = when your computer thinks time began (reference point)
                            
print(time.time())   #return current seconds since 


time_object = time.localtime()
# print(time_object)
formated_time  = time.strftime("%B %d %Y %H:%M:%S",time_object)
# print(formated_time)

time_tupple = (2021,5,20,3,35,2,0,0,0)
time_string = time.asctime(time_tupple)
print(time_string)


# nepali_date = nepali_datetime.date.today()
# print(nepali_datetime.datetime.now())
#exception handling
print("resource starts")
try:
    a= int(input("first entry: "))
    b= int(input("second entry: "))
    result = a/b
    print(result)

except Exception as e:
    print(e)
except ZeroDivisionError as zde:
    print(zde)
finally:
    print("resource complete")

print("End of the code")
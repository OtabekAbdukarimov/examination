def my_func(a,b):
    try:
        return a+b
    except:
        print("Mistake in exercise")
    finally:
        print("Not result found")
result=my_func(17,"7")
print(result)
def is_larger_than_10(x):
    print("step2:function called")
    print("step3:int check starting")
    if not isinstance(x,int):
        print(f"step4:{x} is not an int")
        print("step5:return")
        return None
    if x > 10:
        print(f"step6: if condition check starting")
        print(f"step7:{x} is greater than 10")
        print("step8:return")
        return True
    else:
        print(f"step9:{x} is smaller than 10")
        print("step10: return")
        return False
print("step1 for test1: call function")
print(is_larger_than_10("hi"))
print("step1 for test2: call function")
print(is_larger_than_10(20))
print("step1 for test3: call function")
print(is_larger_than_10(5))
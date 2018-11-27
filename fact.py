def fact(n):
    return fact_iter(n, 1)
# 尾递归调用
def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print(fact(120), fact_iter(5, 1))

def fun(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)
print(fun(120))

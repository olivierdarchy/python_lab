def fast_exp(num, exp) :
    """
        quick way to evaluate num to power exp (recursive)
    """
    if exp == 1 :
        return num
    elif exp % 2 == 0 :
        return fast_exp(num, exp // 2) ** 2
    else :
        return num * fast_exp(num, exp // 2) ** 2

if __name__ == "__main__" :
    print(fast_exp(2, 8))

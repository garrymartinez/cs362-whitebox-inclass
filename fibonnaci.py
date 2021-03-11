def fibonnaci(num):
    if num <= 1:
        return num
    else:
        return(fibonnaci(num - 1)+fibonnaci(num - 2))

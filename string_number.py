# string double number from integer
def dbl_number(num: int) -> str:
    if len(str(num)) == 1:
        return f"0{str(num)}"
    elif len(str(num)) == 2:
        return str(num)
    else:
        return str(num)

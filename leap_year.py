def is_leap_year(year):
    if year%4 == 0 and year%100!=0:
        return True
    elif year%400 == 0:
        return True
        
    elif year%100 == 0:
        return False
    else:
        # TODO: write code...if year%100 == 0:
        return False
    # Write your code here. 
    # Don't change the function name.
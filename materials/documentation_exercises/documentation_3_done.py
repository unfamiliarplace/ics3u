# Documentation practice 3

def is_mixed_case(s: str) -> bool:
    """
    Return True iff a contains at least one lowercase
    and one uppercase letter.
    """
    
    found_upper = False
    found_lower = False
    
    for char in s:
        
        if char.isupper():
            found_upper = True
            
        elif char.islower():
            found_lower = True
            
    return found_upper and found_lower

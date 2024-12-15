import random

def generateId(length=8):
    """
    Tạo một ID số ngẫu nhiên với độ dài được chỉ định.
    
    Args:
        length (int): Độ dài của ID. Mặc định là 8.
        
    Returns:
        str: ID số ngẫu nhiên.
    """
    return int(''.join([str(random.randint(0, 9)) for _ in range(length)]))
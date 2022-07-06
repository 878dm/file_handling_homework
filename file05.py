def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    k=0
    l=0

    for i in data:
        if i.isdigit():
            k+=1
    l=len(data)-k
    arr=[k,l]
    return arr

# Read data from file
f=open('txt_file/data05.txt')
x=f.read()
print(main(x))
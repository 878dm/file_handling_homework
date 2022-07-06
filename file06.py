def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    arr_1=[]
    arr=data.split()
    for i in arr :
        k=len(i)
        arr_1.append(k)
    return arr_1
# Read data from file
f=open('txt_file/data06.txt')
data=f.read()
print(main(data))
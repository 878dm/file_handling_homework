def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    arr=[]
    arr1=[]
    for i in data:
        if i.isdigit():
            arr.append(i)
        else :
            arr1.append(i)
    return arr1
# Read data from file
f=open('txt_file/data04.txt')
data=f.read()
print(main(data))
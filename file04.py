def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    arr=[]
    for i in data:
        if i.isalpha():
            arr.append(i)
    return arr
# Read data from file
f=open('txt_file/data04.txt')
x=f.read()
print(main(x))
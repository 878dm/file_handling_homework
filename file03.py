def main(data:str):
    """
    The data is from the file. Return the numbers as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    arr=[]
    for i in data :
        if i.isdigit() :
            arr.append(i)
    return arr
# Read data from file
f=open('txt_file/data03.txt')
x=f.read()
print(main(x))
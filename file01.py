def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    arr = []
    for i in data.split(','):
        arr.append(int(i))
    return arr


# Read data from file
f = open('txt_file/data01.txt','r')
data=f.read()
print(main(data))

def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    arr=[]
    for i in data :
        if i.isdigit():
            arr.append(i)
    return min(arr)
# Read data from file
f=open('txt_file/data09.txt')
data = f.read()
print(main(data))
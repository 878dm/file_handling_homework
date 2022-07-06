def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    arr1=[]
    arr=data.split("\n")
    for i in arr:
        k=len(i)
        arr1.append(k)
    return max(arr1)
# Read data from file
f=open('txt_file/data10.txt')
data = f.read()
print(main(data))
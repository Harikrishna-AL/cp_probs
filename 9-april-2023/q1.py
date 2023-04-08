a=int(input(""))
n=list(map(int, input("").strip().split()))
result = []
def find_idx(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return i + 1
def main():
    for i in range(1,len(n)+1):
        result.append(find_idx(n,i))
    for i in range(len(result)):
        print(result[i],end=" ")

main()

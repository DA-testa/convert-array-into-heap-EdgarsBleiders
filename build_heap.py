# python3

def sift_down(data, i, swaps):
    min = i
    left = 2*i+1
    if left < len(data) and data[left] < data[min]:
        min = left
    
    right = 2*i+2
    if right < len(data) and data[right] < data[min]:
        min = right
    
    if i!=min:
        swaps.append((i,min))
        data[i], data[min] = data[min], data[i]
        sift_down(data, min, swaps)

def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    for i in range(len(data) // 2, -1, -1):
        sift_down(data, i, swaps)
    return swaps



def main():
    
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file

    text = input()
    # input from keyboard
    if "I" in text:
        n = int(input())
        data = list(map(int, input().split()))
    
    if "F" in text:
        file = input()
        with open("tests/" + file, 'r') as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    assert len(swaps) <=4*n
    print(len(swaps))

    # output all swaps
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()

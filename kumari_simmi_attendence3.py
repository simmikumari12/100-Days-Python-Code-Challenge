def main():
    input_ls = []
    print("\nEnter Items: ")
    while True:
        try:
            item = int(input())
            input_ls.append(item)
        except ValueError:
            pass
        except KeyboardInterrupt:
            break
        except EOFError:
            break
    while True:
        try:
            target = int(input("Target: "))
            break
        except ValueError:
            pass

    sorted_list = merge_sort(input_ls)
    print(f"Sorted List: {sorted_list}")
    print(binary_search(sorted_list, 0, len(sorted_list) - 1, target))

def merge_sort(nums):
    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i = i + 1

            else:
                result.append(right[j])
                j = j + 1
        result = result + left[i:] + right[j:]
        return result
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)

def binary_search(arr, low, high, target):

    if low > high:
        return -1
    
    mid = (low + high) // 2
    if target == arr[mid]:
        return mid
    elif target < arr[mid]:
        return binary_search(arr, low, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, high, target)

if __name__ == "__main__":
    main()

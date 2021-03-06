import random

def quick_sort(arr, low, high):
  if (low < high):
    q = randomized_partition(arr, low, high)
    quick_sort(arr, low, q-1)
    quick_sort(arr, q+1, high)
  return arr

def partition(arr, low, high):
  x = arr[high]
  i = low - 1
  for j in range(low, high):
    if arr[j] <= x:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]
  arr[i+1], arr[high] = arr[high], arr[i+1]
  return i+1

def randomized_partition(arr, low, high):
  i = random.randint(low, high)
  arr[i], arr[high] = arr[high], arr[i]
  return partition(arr, low, high)
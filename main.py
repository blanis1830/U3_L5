#Blayne Hoy
#U3 Lab 5

array = (129, 48, 79, 23, 54, 49, 13, 9, 17, 281)

def quick_sort(array):
  if len(array) <= 1:
    return array
  pivot = array[-1]
  left_array = [x for x in array[:-1] if x <= pivot]
  right_array = [x for x in array[:-1] if x > pivot]

  return quick_sort(left_array) + [pivot] + quick_sort(right_array)

def main():
  sort = quick_sort(array)
  print(sort)

if __name__ == "__main__":
  main()
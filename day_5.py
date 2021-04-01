def multiples():
   for i in range(1,num_of_multiples + 1):
      multiple = num * i
      print(f"{num} x {i} = {multiple}")

if __name__ == '__main__':
   num = int(input("Find multiples of : "))
   num_of_multiples = int(input("Number of multiples you want to find: "))
   multiples()

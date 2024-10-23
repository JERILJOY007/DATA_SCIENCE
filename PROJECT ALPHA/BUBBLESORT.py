
elements = []
num_elements = int(input("Enter the number of elements: "))

print("Enter the elements:")
for i in range(num_elements):
    elements.append(int(input()))

print("Original array:", elements)

n = len(elements)


for i in range(n):

    for j in range(0, n-i-1):

        if elements[j] > elements[j+1]:
            elements[j], elements[j+1] = elements[j+1], elements[j]

print("Sorted array:", elements)
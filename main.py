array = [1,5,10,15,20,25]
sumarr = []

for y in range(len(array)):
  sumarr.append(0)

for x in range(len(array)):
  if x == 0:
    sumarr[0] = array[x] + array[x+1]

  if x == len(array)-1:
    sumarr[x] = array[len(array)-1] + array[len(array)-2]

  else: 
    sumarr[x] = array[x-1] + array[x] + array[x+1]

print(array)
print(sumarr)
    

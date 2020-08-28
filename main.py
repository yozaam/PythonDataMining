# trainingData = []

# for i in range(15):
#   trainingData.append(input().split(","))

#print(trainingData)

# finds the position of height in sorted list
# using binary search hvariant as seen here:
# https://www.topcoder.com/binary-stride-a-variant-on-binary-search/
def finder(data , target):
  n = len(data)
  start = 0
  jump = n//2
  while(jump>=1):
    while(start+jump<n):
      if(data[jump+start][2]<target):
        # safe to jump here!
        start+=jump

    jump/=2

  return start 
  # return the closest value >= target

trainingData = [['Kristina', 'F', '1.6m', 'Short'], ['Jim', 'M', '2m', 'Tall'], ['Maggie', 'F', '1.9m', 'Medium'], ['Martha', 'F', '1.88m', 'Medium'], ['Stephanie', 'F', '1.7m', 'Short'], ['Bob', 'M', '1.85m', 'Medium'], ['Kathy', 'F', '1.6m', 'Short'], ['Dave', 'M', '1.7m', 'Short'], ['Worth', 'M', '2.2m', 'Tall'], ['Steven', 'M', '2.1m', 'Tall'], ['Debbie', 'F', '1.8m', 'Medium'], ['Todd', 'M', '1.95m', 'Medium'], ['Kim', 'F', '1.9m', 'Medium'], ['Amy', 'F', '1.8m', 'Medium'], ['Wynette', 'F', '1.75m', 'Medium']]

for data in trainingData:
  data[2] = data[2][:-1]
  # remove last 'm' from height
  data[2] = float(data[2])

print(trainingData)

trainingData.sort(key = lambda x: (x[2])) 

# print(trainingData)

# now it is sorted ! just going to binarysearch 
# for each value in classifier! and find closest 
# points to it above and below!!!


print(finder(trainingData, 1.7))
# should return index of 1.7 in trainingData?

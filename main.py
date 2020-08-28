# trainingData = []

# for i in range(15):
#   trainingData.append(input().split(","))

#print(trainingData)

# finds the position of height in sorted list
# using binary search hvariant as seen here:
# https://www.topcoder.com/binary-stride-a-variant-on-binary-search/
def lowerBound(data , target):
  n = len(data)
  start = 0
  jump = n//2
  while(jump>=1):
    # print("jump:",jump)
    while(start+jump<n):
      if(data[jump+start][2]<target):
        # safe to jump here!
        start+=jump
      else:
        break

    jump//=2

  return start 
  # return the closest value >= target

def kClosest(start, target, k, data):
  # from start check up and down continuosly 
  # to find k closest neighbours
  knn = [] 
  # i will store the indices in that list!
  up = start
  down = start + 1

  while(len(knn) < k):
    # need to pick an element!

    # if up or down have gone outside boundary !
    # just pick whoever is indside boundary!!
    if(down >= len(data) and up<0) or (up>=len(data)):
      # cant pick anyone more... k is bigger than the list size!!!!
      return knn
    elif up<0:
      knn.append(down)
      down+=1
    elif down >= len(data):
      knn.append(data[up])
      up+=1
    else :
      upDistance = data[up][2] - target
      downDistance = data[down][2] - target

      if upDistance<downDistance:
        knn.append(up)
        up+=1
      else :
        knn.append(down)
        down+=1

  return knn

def majority(knn, trainingData) :
  count = {
    'Short':0,
    'Medium':0,
    'Tall':0
  }

  result = 'Tall'
  resultCount = 0

  for index in knn:
    if index<0 or index>=len(trainingData):
      continue
    category = trainingData[index][3]
    count[category]+=1
    if resultCount < count[category]:
      resultCount = count[category]
      result = category
  
  return result

trainingData = [['Kristina', 'F', '1.6m', 'Short'], ['Jim', 'M', '2m', 'Tall'], ['Maggie', 'F', '1.9m', 'Medium'], ['Martha', 'F', '1.88m', 'Medium'], ['Stephanie', 'F', '1.7m', 'Short'], ['Bob', 'M', '1.85m', 'Medium'], ['Kathy', 'F', '1.6m', 'Short'], ['Dave', 'M', '1.7m', 'Short'], ['Worth', 'M', '2.2m', 'Tall'], ['Steven', 'M', '2.1m', 'Tall'], ['Debbie', 'F', '1.8m', 'Medium'], ['Todd', 'M', '1.95m', 'Medium'], ['Kim', 'F', '1.9m', 'Medium'], ['Amy', 'F', '1.8m', 'Medium'], ['Wynette', 'F', '1.75m', 'Medium']]

for data in trainingData:
  data[2] = data[2][:-1]
  # remove last 'm' from height
  data[2] = float(data[2])

# print(trainingData)

trainingData.sort(key = lambda x: (x[2])) 

# print(trainingData)

# now it is sorted ! just going to binarysearch 
# for each value in classifier! and find closest 
# points to it above and below!!!

print("where is 1.7?")
position = lowerBound(trainingData, 1.7)
print(position)
# should return index of 1.7 in trainingData?

knn = kClosest(position, 1.7, 3 ,trainingData)

print('for 1.7 we have class = ')
print(majority(knn, trainingData))

while 1:
  print('Now you enter a persons height(0 to 3 meters)\n and I will classify!')

  h = float(input())
  print("where is ",h)
  position = lowerBound(trainingData, h)
  print(position)
  # should return index of h in trainingData?

  knn = kClosest(position, h, 3 ,trainingData)
  print(h,' neighbors are ' , knn)

  print('for ',h,' we have class = ')
  print(majority(knn, trainingData))






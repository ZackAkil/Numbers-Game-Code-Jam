# solution to numbers game puzzle from code jam Round 1A 2010
# pass command line parameters of input file name and output file name
# By Zack Akil 26/05/2016 

import sys
import math
import time

# problem logic

# intial (brute force) solution suitable for small data set

def runGame(a,b):
  outcome = 0
  myTurn = False
  roundOutcome = []

  while(outcome == 0):
    myTurn = not myTurn
    [a,b,outcome] = round(a,b)

  win = True  
  if(((outcome==2)and(myTurn))
    or((outcome ==1)and(not myTurn))):
    win = False

  return win

def round(a,b):
  if(a<b): 
    t = b
    b = a
    a = t

  if(a==b):
    return [a,b,2]
  elif( ( ((a-b)-((a-b)%b))/b ) > 0 ): #winning choice logic
    return [a,b,1]
  else:
    return [a-b,b,0] #else play the forced move

def gameRange(a1,a2,b1,b2):
  output = 0
  for x in xrange(a1,a2+1):
    for y in xrange(b1,b2+1):
      if(runGame(x,y)==True):
        output += 1
  return output 

# final optimised solution for large data set 

def subtractRange(a1,a2,b1,b2): # find losing intersection with the game range
  if( ( a1>b2 )or( a2<b1 ) ): # no intersection
    return a2-a1+1
  elif( ( a1 <= b1 )and( a2 >= b2 ) ):# complete internal intersection
    return (a2-a1)-(b2-b1)
  elif( ( a1 >= b1 )and( a2 <= b2 ) ):# complete outer intersection
    return 0
  elif( ( a1 > b1 )and( a2 > b2 ) ):# left hand partial intersect
    return (a2-a1)-( (b2-b1)-(a1-b1) )
  elif( ( a1 < b1 )and( a2 < b2 ) ):# right hand partial intersect
    return (a2-a1)-( (b2-b1)-(b2-a2) )

  print("not ready for this a - {},{} b - {},{} "
    .format(a1,a2,b1,b2))
  return 0

def losingRange(val):
  a1 =  math.ceil(val * (golden - 1))
  a2 = a1 + val -1
  return [a1,a2]

# optimise order of values for newGameRange
def optimalChoice(a1,a2,b1,b2):
  if((b2-b1)>(a2-a1)):
    return [b1,b2,a1,a2]
  else:
    return [a1,a2,b1,b2]

def newGameRange(a1,a2,b1,b2):
  output = 0
  [a1,a2,b1,b2] = optimalChoice(a1,a2,b1,b2)
  assert ((b2-b1)<=(a2-a1)),"Inefficent range order"

  for x in xrange(b1,b2+1):
      [s1,s2] = losingRange(x)
      output += subtractRange(a1,a2,s1,s2)
  return int(output)    

# golden ratio global constant definition for optimised solution

golden = (1 + 5 ** 0.5) / 2

# file reading/writing logic

if len(sys.argv) >=3:
  inputFile = sys.argv[1]
  outputFile = sys.argv[2]
else:
  inputFile = input('Enter input file name: ')
  outputFile = input('Enter output file name: ')

f = open(inputFile, 'r')
rows = int(f.readline())

outputs = []
start = time.time()
for x in xrange(0,rows):
  nums = f.readline().split(' ')
  print('doing test {}'.format( x+1))
  outputs.extend([ newGameRange(int(nums[0]),int(nums[1]),int(nums[2]),int(nums[3])) ])
print ('finished in {} seconds'.format( time.time()-start))
w = open(outputFile, 'w')
for x in xrange(0,rows):
  w.write('Case #{}: {}'.format(x+1,outputs[x] ))
  if x < rows - 1:
     w.write('\n')

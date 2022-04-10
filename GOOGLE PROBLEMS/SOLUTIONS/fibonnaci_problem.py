"""
So here is a sample problem that we tried last night,
I think the difficulty is probably just about correct for a STEP interview question.

Problem  #1: Write a Fibonacci() function which, given an integer N,
 returns the Nth number in the Fibonacci sequence beginning with [0, 1].
This should take you NO LONGER than maybe 3-4 minutes to crank out. You should be able to write this one in your sleep.

Problem #2: Extend your function to instead add the three most recent values instead
of the two most recent values in a sequence beginning with [0, 0, 1].
You should be able to do this in another minute.

Problem #3: Write a general solution to Fibonacci(N,k) where the function returns
the Nth number in the sequence where each new value is the sum of the previous k values.
So, a standard Fib would be the k=2 case. This is the real, actual problem - the first two parts were just warmup,
and ideally you should have nearly 40 minutes remaining in which to solve it.

"""

# One which has an answer for each problem:
#Answer 1
def Fibonacci(idx):
  sqc = [0,1]
  if idx < 2:
    pass
  else:
    for cnt in range(2,idx+1):
      sqc.append((sqc[-1] + sqc[-2]))
  return sqc[idx]

#Answer 2
def Threebonacci(idx):
  sqc = [0,0,1]
  if idx < 3:
    pass
  else:
    for cnt in range(3,idx+1):
      sqc.append((sqc[-1] + sqc[-2] + sqc[-3]))
  return sqc[idx]

#Answer 3
def Nbonacci(idx,smn=2):
  sqc = []
  skl = 0
  for i in range (1,smn):
    sqc.append(0)
  sqc.append(1)
  if idx < smn:
    pass
  else:
    for cn1 in range(smn,idx+1):
      for cn2 in range(-1, -smn-1, -1):
        skl += sqc[cn2]
      sqc.append(skl)
      skl = 0
  return sqc[idx]
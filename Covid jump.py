#5
t = int(input("Enter the number of cases:"))
N=[]
K=[]
X=[]
Y=[]
while (t > 100 or t <= 0):
  t = int(input("Upto 100 cases are accpeted. Enter again :"))
print("Type each case details one after one while pressing 'ENTER' in between..\neach case must have number of cities, size of jump,covid's current city and the city you live in")
print('Follow the constrains given below:\n * Upto 100 cities(N) are allowed\n* Cities are numbered from 0 to N-1\n* The maximum limit of jump is 1000')
print('Start entering cases...\n')
for i in range(t):
  N.append('')
  K.append('')
  X.append('')
  Y.append('')
  N[i],K[i],X[i],Y[i] = input().split()
  N[i],K[i],X[i],Y[i] = int(N[i]),int(K[i]),int(X[i]),int(Y[i])
  while (N[i] > 1000 or N[i] <= 0 or X[i] > N[i]-1 or X[i] < 0 or Y[i] > N[i]-1 or Y[i] < 0 or K[i] > 1000 or K[i] <= 0 ):
    N[i],K[i],X[i],Y[i] = input('Constrants were not followed please enter this case again')
for i in range(t):
  print(Case,i,':')
  jump = (K[i] % N[i])
  if N[i] % jump == 0 or N[i] % (N[i] - jump) == 0:
    if abs(X[i] - Y[i]) % K[i] != 0:
      print('NO, you are safe')
  else:
    print('YES, you will be affected')

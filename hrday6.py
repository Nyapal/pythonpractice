# def review(num, string):
#   lis = list(string)
#   even = []
#   odd = []
#   for i in lis:
#     if(lis.index(i) % 2 == 0):
#       even.append(i)
#     else:
#       odd.append(i)
#   return ''.join(even), ''.join(odd)

def review(num):
  for ind in range(num):
    lis = input()
    even = ''
    odd = ''

    for i in lis:
      if (lis.index(i) % 2 == 0):
        even += lis[i]
      else: 
        odd += lis[i]
    print('{} {}'.format(even,odd))

if __name__ == '__main__':
  num = int(input())

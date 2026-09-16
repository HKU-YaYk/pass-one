"""
for a in range(1,10):
    for b in range(1,a+1):
        print(f"{a}*{b}={a*b}",end="\t")
        print()
      """
"""
notice="12312412515"
c=0
for b in notice:
    if b=="1":
        c=c+1
print(c)
   """

while True:
    line = input()
    if line == "":
        break
    words = line.split()
    if words:
        print(len(words[-1]))
"""
import sys

s=sys.stdin.readline().strip()
c=sys.stdin.readline().strip()
if c.isalpha():
    s=s.lower()
    c=c.lower()
    print(s.count(c))
else:
    print(s.count(c))
"""

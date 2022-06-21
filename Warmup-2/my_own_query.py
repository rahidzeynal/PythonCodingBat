# Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. 
# So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in both strings.


def string_match(a, b):
  cnt = 0
  
  if len(a) >= 2 and len(b) >= 2:
    if len(a) >= len(b):
      for i in range(len(a)-1):
        s1 = a[i] + a[i+1]
        for j in range(len(b)-1):
          s2 = b[j] + b[j+1]
          if s1 == s2:
            cnt += 1
      return cnt
    else:
      for i in range(len(b)-1):
        s1 = b[i] + b[i+1]
        for j in range(len(a)-1):
          s2 = a[j] + a[j+1]
          if s1 == s2:
            cnt += 1
      return cnt
  else:
    cnt = 0
    return cnt

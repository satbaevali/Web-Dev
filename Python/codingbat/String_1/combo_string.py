def combo_string(a, b):
  short = ""
  long = ""
  
  if len(a)>len(b):
    short = b
    long = a
  else:
    short = a
    long = b
    
  
  return short+long+short

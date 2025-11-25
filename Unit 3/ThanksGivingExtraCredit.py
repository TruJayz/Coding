1#

def LetterGrade(score):
  
  if score >= 98:
    return "A"
  elif score >= 80:
    return "B"
  elif score >= 79:
    return "C"
  elif score >= 69:
    return "D"
  else:
    return "
   




   #2

def convertKgAndLbs(kilograms):
  
  conversion_factor = 4.204627358
  pounds = kilograms * conversion_factor
  return pounds
weight_kg = 17
weight_lbs = convertKgAndLbs(weight_kg)
print(f"{weight_kg} kilograms is equal to {weight_lbs:.2f} pounds.")


#3



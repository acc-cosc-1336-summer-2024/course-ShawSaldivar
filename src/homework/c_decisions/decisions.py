ratio = 0

def get_options_ratio(options, total):
  ratio = options / total
  return ratio

def get_faculty_rating(ratio):

  if (ratio <= 1 and ratio >= .9):
   return "Excellent"
  elif (ratio >= .8 and ratio < .9):
    return "Very Good"
  elif (ratio >= .7 and ratio < .8):
    return "Good"
  elif (ratio >= .6 and ratio < .7):
    return "Needs Improvement"
  elif (ratio >= 0 and ratio < .59):
    return "Unacceptable"

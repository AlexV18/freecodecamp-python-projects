import re

def arithmetic_arranger(problems, print_answers=False):

  # variable that stores problems
  arranged_problems = ""

  # error checking for too many problems
  if(len(problems) > 5):
    return "Error: Too many problems."

  # error checking loop
  #===========================================================================
  for i in problems:
    problem_sliced = i.split()
    # checks the operator
    if problem_sliced[1] != "-" and problem_sliced[1] != "+":
      return "Error: Operator must be '+' or '-'."
    # checks wether every number is indeed a number using regex
    if re.search('[a-zA-Z]+', problem_sliced[0]) or re.search('[a-zA-Z]+', problem_sliced[2]):
      return 'Error: Numbers must only contain digits.'
    # checks if numbers are longer than 4 digits
    if len(problem_sliced[0]) > 4 or len(problem_sliced[2]) > 4:
      return "Error: Numbers cannot be more than four digits."

  # get the contents for the first row
  #===========================================================================
  for i in problems:
    problem_sliced = i.split()
    # get the length of the longest string:
    longest_printable_length = len(max(problem_sliced, key=len)) + 2
    # we don't want to add any spaces for the final number
    if i == problems[-1]:
      arranged_problems += (longest_printable_length-len(problem_sliced[0]))*" " + problem_sliced[0]
    else:
      arranged_problems += (longest_printable_length-len(problem_sliced[0]))*" " + problem_sliced[0] + "    "

  arranged_problems += "\n"
  
  # get the contents for the second row
  #===========================================================================
  for i in problems:
    problem_sliced = i.split()
    # get the length of the longest string:
    longest_printable_length = len(max(problem_sliced, key=len)) + 2
    arranged_problems += problem_sliced[1]
    if i == problems[-1]:
      arranged_problems += (longest_printable_length-len(problem_sliced[2]) - 1)*" " + problem_sliced[2]
    else:
      arranged_problems += (longest_printable_length-len(problem_sliced[2]) - 1)*" " + problem_sliced[2] + "    "

  arranged_problems += "\n"

  # print the lines
  #===========================================================================
  for i in problems:
    problem_sliced = i.split()
    # get the length of the longest string:
    longest_printable_length = len(max(problem_sliced, key=len)) + 2
    arranged_problems += "-"*longest_printable_length
    if i == problems[-1]:
      break;
    else:
      arranged_problems += "    "

  # print the answers if you need to do so
  #===========================================================================
  if print_answers:
    arranged_problems += "\n"
    for i in problems:
      problem_sliced = i.split()
      longest_printable_length = len(max(problem_sliced, key=len)) + 2
      answer = 0
      if problem_sliced[1] == "+":
        answer = int(problem_sliced[0]) + int(problem_sliced[2])
      else:
        answer = int(problem_sliced[0]) - int(problem_sliced[2])

      if i == problems[-1]:
        arranged_problems += (longest_printable_length-len(str(answer)))*" " + str(answer)
      else:
        arranged_problems += (longest_printable_length-len(str(answer)))*" " + str(answer) + "    "

      
  return arranged_problems


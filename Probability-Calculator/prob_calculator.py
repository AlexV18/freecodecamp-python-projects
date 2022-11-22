import copy
import random
import collections
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    # data is a dict
    # loop used to make list of hats
    for i in kwargs:
      x = kwargs[i]
      for z in range(0,x):
        self.contents.append(i)
    print(self.contents)
        
  def draw(self, balls):
    new_contents = []
    if (balls > len(self.contents)):
      return self.contents
    for i in range(balls):
      selection = self.contents.pop(int(random.random() * len(self.contents)))
      new_contents.append(selection)
    return new_contents
    print(self.new_contents)
    
        
 
    
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  M = 0
  for a in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    expected_copy = copy.deepcopy(expected_balls)
    randomized_selection = hat_copy.draw(num_balls_drawn)

    for color in randomized_selection:
      if (color in expected_copy):
        expected_copy[color]-=1
      
    if(all(x <= 0 for x in expected_copy.values())):
      M += 1
    
  return M/num_experiments
      
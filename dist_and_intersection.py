def remove(string):
    return string.replace(" ", "")

def distance_iter_mat(x, d_min, d_max, a1_index, a2_index):

  #a1 index = line no of 1st atom in xmolout
  #a2 index = line no of 2nd atom in xmolout
  
  x_a1 = np.zeros(math.ceil(len(x)/76))
  y_a1 = np.zeros(math.ceil(len(x)/76))
  z_a1 = np.zeros(math.ceil(len(x)/76))
  x_a2 = np.zeros(math.ceil(len(x)/76))
  y_a2 = np.zeros(math.ceil(len(x)/76))
  z_a2 = np.zeros(math.ceil(len(x)/76))


  for i_x in range (0, math.floor(len(x)/76)):
  #print(i_x)
  #print(x[9+76*i_x])
  #print(x[9+76*i_x][4:12]) 
    x_a1[i_x] = float(x[a1_index+76*i_x][4:12])
    x_a2[i_x] = float(x[a2_index+76*i_x][4:12])

  for i_y in range (0, math.floor(len(x)/76)):
  #print(i_y)
  #print(x[9+76*i_y])
  #print(x[9+76*i_y][13:21]) 
    y_a1[i_y] = float(x[a1_index+76*i_y][13:21])
    y_a2[i_y] = float(x[a2_index+76*i_y][13:21])
  for i_z in range (0, math.floor(len(x)/76)):
  
  
  #print(x[9+76*i_z][13:21]) 
    z_a1[i_z] = float(x[a1_index+76*i_z][22:31])
    z_a2[i_z] = float(x[a2_index+76*i_z][22:31])




    x_diff = np.square(x_a1-x_a2)
    y_diff = np.square(y_a1-y_a2)
    z_diff = np.square(z_a1-z_a2)
    dist_a1_a2 = np.sqrt(x_diff + y_diff + z_diff)

  #print(dist_a1_a2)

  res_a1_a2 = np.where(np.logical_and(dist_a1_a2 >= d_min, dist_a1_a2 <= d_max))
  #print(res_a1_a2)
  print(type(res_a1_a2))
  return res_a1_a2#, dist_a1_a2

  #for i_ts in res_c1_n1:
    #print(i_ts)
    #print(dist_a1_a2[i_ts])



def common_member(a, b):
    a_set = set(a)
    b_set = set(b)
 
    if (a_set & b_set):
        print(a_set & b_set)
    else:
        print("No common elements")

def distance_check(dist_matrix, d_min, d_max): #not checking others as they are molecules themselves
 

  #dist_matrix -> the matrix calculated by dist function above
  c1_line = 59 #line nummer in xmolout counting from 0 onwards
  n1_line = 9
  o1_line = 60
  h1_line_1 = 20  #both h connected to n can react
  h1_line_2 = 21
  x_r = np.zeros(100,15,100)
  for i_dm in range(0, len(dist_matrix)):
    x_r = np.where(np.logical_and(dist_matrix >= d_min, dist_matrix <= d_max))
  
def contains(tuple, given_char):
    if given_char in tuple:
        print(given_char)
        return True
    return False   
  

def common(a,b): 
  c = [value for value in a if value in b] 
  return c

    t
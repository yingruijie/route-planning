import numpy 
import pickle

# correspond the number of the position to its name
pos_char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'Z']

# load data for pkl file
data = []
with open("data.pkl", "rb") as f:
    data = pickle.load(f)
connect = numpy.array(data['c'])
distance = numpy.array(data['d'])

curr_pos = 0
curr_g = 0
iterative = 0
path = []

# iterative algorithm
# limit the number of iterations
while (curr_pos != 1) & (iterative < 100):
    iterative = iterative + 1
    path.append(curr_pos)
    connect_with_curr = []
    for jj in range(20):
        if connect[curr_pos][jj] > 0:
            pos = {'p': 0,'f': 0, 'g': 0, 'h':0}
            pos['p'] = jj
            pos['g'] = curr_g + connect[curr_pos][jj]
            pos['h'] = distance[jj]
            pos['f'] = pos['g'] + pos['h']
            connect_with_curr.append(pos)
    if connect_with_curr:
        connect_with_curr = sorted(connect_with_curr, key=lambda x:x['f'])
        curr_pos = connect_with_curr[0]['p']
        curr_g = connect_with_curr[0]['g']
    else:
        print("error in while")
        break

# find a path
if curr_pos == 1:
    path.append(curr_pos)
    path_char = []
    for pos in path:
        path_char.append(pos_char[pos])
    print("path: ", path_char)
    print("distance: ", curr_g)
# failed
else:
    print('failed to find the path')

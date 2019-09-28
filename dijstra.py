import numpy
import pickle

pos_char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'Z']

# get the path of a node
def get_path(path, S, node):
    path.append(node['p'])
    if node['p'] != 0:
        for s in S:
            if s['p'] == node['f']:
                node_f = s
                break
        get_path(path, S, node_f)

# load data
data = []
with open("data.pkl", "rb") as f:
    data = pickle.load(f)
connect = numpy.array(data['c'])

# initialize the list
S = []
T = []
for ii in range(20):
    node = {'p': 0, 'd': 0, 'f': 0}
    node['p'] = ii
    node['d'] = -1
    node['f'] = -1
    T.append(node)

# node 0 init
node = {'p': 0, 'd': 0, 'f': 0}
node['p'] = 0
node['d'] = -1
node['f'] = -1
T.remove(node)
node['d'] = 0
S.append(node)
iterative = 0

# iterative algorithm
# limit the number of iterations
while T:
    if iterative == 100:
        break
    iterative = iterative + 1
    for s in S:
        for t in T:
            # connect
            if connect[s['p']][t['p']] > 0:
                dis = s['d'] + connect[s['p']][t['p']]
                if (t['d'] > dis) | (t['d'] < 0):
                    t['d'] = dis
                    t['f'] = s['p']
    # find the minimum distance
    T = sorted(T, key = lambda x:x['d'])
    for t in T:
        if t['d'] > 0:
            T.remove(t)
            S.append(t)
            break

S = sorted(S, key = lambda x:x['p'])

path = []
get_path(path, S, S[1])
path_char = []
for ii in range(len(path)):
    path_char.append(pos_char[int(path[len(path) - ii - 1])])
print("path: " , path_char)
print("distance: ", S[1]['d'])

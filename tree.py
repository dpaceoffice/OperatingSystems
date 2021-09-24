import pydot
import subprocess

#proc = subprocess.Popen(['fork', '5' '<'])
#proc.wait()

with open('output', "w") as outfile:
    subprocess.run(['fork', '5'], stdout=outfile)

'''
This was more challenging than I had thought
Time complexity is O(n)
Space complexity is O(n)
'''
def sort():
    file = open("output")
    data = dict()
    for line in file.readlines():
        line = line.strip()
        parent = line.split(',')[0].replace('PPID: ', '')
        child = line.split(',')[1].replace(' PID: ', '')

        if(child not in data.keys()):
            if(parent not in data.keys()):
                data[parent] = 0
                data[child] = 1
            else:
                data[child] = data[parent] + 1
            
        draw('PID:'+str(parent)+'\nLevel:'+str(data[parent])+'', 'PID:'+str(child)+'\nLevel:'+str(data[child])+'')

def draw(parent_name, child_name):
    edge = pydot.Edge(parent_name, child_name)
    graph.add_edge(edge)

graph = pydot.Dot(graph_type='graph')
sort()
graph.write_png('example1_graph.png') 
graph.show()


import pydot

def sort():
    file = open("test.txt")
    level = 0
    prev = None
    for line in file.readlines():
        line = line.strip()
        parent = line.split(',')[0].replace('PPID: ', '')
        child = line.split(',')[1].replace(' PID: ', '')
        if(prev != int(parent)):
            if(prev != None):
                level += 1
            prev = int(parent)
        
        draw('PID:'+parent+'\nLevel:'+str(level)+'', 'PID:'+child+'\nLevel:'+str(level+1)+'')

menu = {'dinner':
            {'chicken':'good',
             'beef':'average',
             'vegetarian':{
                   'tofu':'good',
                   'salad':{
                            'caeser':'bad',
                            'italian':'average'}
                   },
             'pork':'bad'}
        }

def draw(parent_name, child_name):
    edge = pydot.Edge(parent_name, child_name)
    graph.add_edge(edge)

def visit(node, parent=None):
    for k,v in node.items():
        if isinstance(v, dict):
            # We start with the root node whose parent is None
            # we don't want to graph the None node
            if parent:
                draw(parent, k)
            visit(v, k)
        else:
            draw(parent, k)
            # drawing the label using a distinct name
            draw(k, k+'_'+v)

graph = pydot.Dot(graph_type='graph')
#visit(menu)
sort()
graph.write_png('example1_graph.png') 
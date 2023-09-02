import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, state):
        self.state = state
        self.children = []
        self.siblings = []

def node_initialization():
    
    house = Node("Marie's House")
    lvr = Node("Living Room")
    br = Node("Bedroom")
    k = Node("Kitchen")
    btr = Node("Bathroom")
    bsm = Node("Basement")
    att = Node("Attic")

    # Child Nodes of Marie's House
    house.children = [lvr, br, k, btr, bsm, att]

    # Child nodes of Living Room
    coffee_table = Node("Coffee Table")
    decorations = Node("Decorations")
    sofa_cushions = Node("Sofa & Cushions")
    bookshelf = Node("Bookshelf")

    # Child nodes of Bedroom
    bed = Node("Bed")
    closet = Node("Closet")
    study_table = Node("Study Table")

    # Child nodes of Kitchen
    cabinets = Node("Cabinets")
    pantry = Node("Pantry")
    appliances = Node("Appliances")

    # Child nodes of Bathroom
    medicine_cabinet = Node("Medicine Cabinet")
    sink = Node("Sink")
    shower = Node("Shower")

    # Child nodes of Basement
    boxes = Node("Basement Boxes")
    shelves = Node("Shelves")
    utility = Node("Utility Area")

    # Child nodes of Attic
    trunks = Node("Trunks")
    boxes_2 = Node("Attic Boxes")

    # Define the graph structure
    lvr.children = [coffee_table, decorations, sofa_cushions, bookshelf]
    br.children = [bed, closet, study_table]
    k.children = [cabinets, pantry, appliances]
    btr.children = [medicine_cabinet, sink, shower]
    bsm.children = [boxes, shelves, utility]
    att.children = [trunks, boxes_2]

    # Define siblings 
    lvr.siblings = [br, k, btr, bsm, att]
    coffee_table.siblings = [decorations, sofa_cushions, bookshelf]
    bed.siblings = [closet, study_table]
    cabinets.siblings = [pantry, appliances]
    medicine_cabinet.siblings = [sink, shower]
    boxes.siblings = [shelves, utility]
    trunks.siblings = [boxes_2]
    
    graph_house = nx.Graph()
    H = nx.path_graph(25)
    
    """""
    lvr.children = [coffee_table, decorations, sofa_cushions, bookshelf]
    br.children = [bed, closet, study_table]
    k.children = [cabinets, pantry, appliances]
    btr.children = [medicine_cabinet, sink, shower]
    bsm.children = [boxes, shelves, utility]
    att.children = [trunks, boxes_2]
    
    """
    
    graph_house.add_edges_from([[house.state,lvr.state], [house.state,br.state], 
                          [house.state,k.state], [house.state,btr.state], 
                          [house.state,bsm.state], [house.state, att.state],
                          
                        [lvr.state,coffee_table.state], [lvr.state,decorations.state], 
                        [lvr.state,sofa_cushions.state], [lvr.state, bookshelf.state],
                        
                        [br.state, bed.state], [br.state,closet.state], [br.state,study_table.state],
                        [k.state, cabinets.state], [k.state,pantry.state], [k.state,appliances.state],
                        [btr.state, medicine_cabinet.state], [btr.state,sink.state], [btr.state,shower.state],
                        [bsm.state, boxes.state], [bsm.state,shelves.state], [bsm.state,utility.state],
                        [att.state, trunks.state], [att.state,boxes_2.state],
                        
                        [lvr.state,br.state], [br.state,k.state], [k.state,btr.state], 
                        [btr.state,bsm.state], [bsm.state,att.state], [att.state,lvr.state]])

    # Return initial and goal
    return house, boxes, graph_house

def search_dls(node, goal, depth_limit, current_depth, visited, steps, num):
    if node.state == goal.state:
        steps.append(node.state)
        print(f"Process #{num[0]} : Node @ {steps}")
        return [node.state]
        
    if current_depth >= depth_limit or node in visited:
        return None

    visited.add(node) # to keep track of visited nodes
    
    # Print out the process of DLS
    steps.append(node.state)
    print(f"Process #{num[0]} : Node @ {steps}")
    num[0] += 1
    
    # Search in children
    for child in node.children:
        result_path = search_dls(child, goal, depth_limit, current_depth + 1, visited,steps, num)
        if result_path:
            return [node.state] + result_path
    
    steps.pop()
    
    # Search in sibling nodes
    for sibling in node.siblings:
        result_path = search_dls(sibling, goal, depth_limit, current_depth, visited,steps, num)
        if result_path:
            return result_path
        
    return None

""" 
Marie needs to find the treasure in her house in 1 hour.

Marie has 15 minutes to search the entire living room,
13 minutes for the entire bedroom,
12 minutes for the entire kitchen,
10 minutes for the entire bathroom,
10 minutes for the entire attic,
and 12 minutes for the entire basement.

"""

initial, goal, graph_house = node_initialization()

# Plotting the nodes
pos = nx.kamada_kawai_layout(graph_house)
nx.draw(graph_house, pos, with_labels=True, node_color='lightblue', font_weight='bold', node_size=1000, font_size=8)
plt.show()


depth_limit = 3
visited_set = set()
steps = list()
num = [1]

# Perform depth-limited search
result_path = search_dls(initial, goal, depth_limit, 0, visited_set, steps, num)

if result_path:
    print("The treasure is in:", result_path)
else:
    print("No treasure has been found.")
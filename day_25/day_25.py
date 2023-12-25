#!/usr/bin/env python3

import networkx as nx

def read_wiring(filename):
    connections = []
    with open(filename, 'r') as f:
        while line := f.readline():
            line = line.strip()
            parts = line.split(': ')
            head = parts[0]
            subs = parts[1].split(' ')
            for s in subs:
                if head < s:
                    connections.append( (head, s) )
                elif head > s:
                    connections.append( (s, head) )
                else:
                    print('error: connection to itself', head)
                    exit(-1)
    return connections

def components_from_connections(conns):
    comps = set()
    for c in conns:
        left, right = c
        comps.add(left)
        comps.add(right)
    return comps

def build_group_around_component(start_compo, connections):
    i = 0
    group = [start_compo]
    # walk through each component of 
    # group (group grows!) and look
    # for any connection that has compo as either left or right.
    # pop that connection out of connections and add 
    # and append the other component to group (so group grows).
    while i < len(group):
        c = group[i]
        j = 0
        while j < len(connections):
            left, right = connections[j]
            if left == c:
                if not right in group:
                    group.append(right)
                connections.pop(j)
            elif right == c:
                if not left in group:
                    group.append(left)
                connections.pop(j)
            else:
                j += 1
        i += 1
    return group

def test_delete(connections):
    i = 0
    while i < len(connections):
        c = connections[i]
        if c == ('hfx','pzl') or c == ('bvb','cmg') or c == ('jqt','nvd'):
            print('popping', c)
            connections.pop(i)
        else:
            i += 1

def count_disparate_groups(connections):
    group = build_group_around_component(connections[0][0], connections)
    if len(connections) == 0:
        return 0
    val = len(group)
    group = build_group_around_component(connections[0][0], connections)
    if len(connections) == 0:
        return len(group) * val
    print('more than two groups')
    return 0

def remove_three_connections(wiring):
    origlen = len(wiring)
    for i in range(origlen):
        print('#',i)
        for j in range(i+1, origlen):
            for k in range(j+1, origlen):
                connections = wiring[:]
                connections.pop(k)
                connections.pop(j)
                connections.pop(i)
                val = count_disparate_groups(connections)
                if val > 0:
                    return val
    return 0
                    
def connection_strengths(connections):
    compos = {}
    for c in connections:
        left, right = c
        if left in compos:
            compos[left] += 1
        else:
            compos[left] = 1
        if right in compos:
            compos[right] += 1
        else:
            compos[right] = 1
    return compos

def main():
#    wiring = read_wiring('test.txt')
    wiring = read_wiring('input.txt')
#    result = remove_three_connections(wiring)
#    print(result)
#    strengths = connection_strengths(wiring)
#    print(strengths)
    graph = nx.from_edgelist(wiring)
    betweenness = nx.edge_betweenness_centrality(graph)
    most_important_connections = sorted(betweenness, key=betweenness.get)
    connections_to_cut = most_important_connections[-3:]
    graph.remove_edges_from(connections_to_cut)
    groupsizes = [len(c) for c in nx.connected_components(graph)]
    if len(groupsizes) != 2:
        print('illegal number of groups')
        exit(-1)
    print(groupsizes[0] * groupsizes[1])


if __name__ == '__main__':
    main()

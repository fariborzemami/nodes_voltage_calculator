import numpy as np
from itertools import combinations

def nodal_analysis():
    node_count = int(input("Enter the number of nodes: "))
    current_sources = np.zeros(node_count, dtype=complex)
    admittance_matrix = np.zeros((node_count, node_count), dtype=complex)

    for i in range(node_count):
        current_sources[i] = complex(input(f"Enter current source at node {i+1} : "))

    for i in range(node_count):
        self_admittance = complex(input(f"Enter admittance at node {i+1} : "))
        admittance_matrix[i][i] = self_admittance

    asked_admittances = set()
    for i in range(node_count):
        for j in range(i+1, node_count):
            node_pair = (min(i+1, j+1), max(i+1, j+1))
            if node_pair not in asked_admittances:
                admittance = complex(input(f"Enter the admittance between nodes {node_pair[0]} and {node_pair[1]} : "))
                admittance_matrix[i][j] = -admittance
                admittance_matrix[j][i] = -admittance
                asked_admittances.add(node_pair)

    unused_admittances = len(set(combinations(range(node_count), 2)) - asked_admittances)

    node_voltages = np.linalg.solve(admittance_matrix, current_sources)
    for i in range(node_count):
        print(f"Voltage of node {i+1}: {node_voltages[i].real}")

nodal_analysis()

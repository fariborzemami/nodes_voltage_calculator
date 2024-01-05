def nodal_analysis():
    # Get the number of nodes from the user
    node_count = int(input("Enter the number of nodes: "))

    # Initialize lists to store current sources and admittances
    current_sources = []
    admittances = []

    # Get current sources and self-admittances for each node
    for i in range(node_count):
        current_sources.append(complex(input(f"Enter current source at node {i+1}: ")))
        admittances.append(complex(input(f"Enter admittance at node {i+1}: ")))

    # Initialize the admittance matrix with self-admittances
    admittance_matrix = [[0] * node_count for _ in range(node_count)]
    for i in range(node_count):
        admittance_matrix[i][i] = admittances[i]

    # Get admittances between nodes
    for i in range(node_count):
        for j in range(i + 1, node_count):
            admittance = complex(input(f"Enter the admittance between nodes {i+1} and {j+1}: "))
            admittance_matrix[i][j] = -admittance
            admittance_matrix[j][i] = -admittance

    # Solve for node voltages
    node_voltages = [0] * node_count  # Placeholder for node voltages
    for i in range(node_count):
        node_voltages[i] = sum(admittance_matrix[i][j] * current_sources[j] for j in range(node_count))

    # Print node voltages
    for i in range(node_count):
        print(f"Voltage of node {i+1}: {node_voltages[i].real}")

# Call the nodal_analysis function to perform the analysis
nodal_analysis()

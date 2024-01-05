
# Nodal Analysis

This is a Python program for performing nodal analysis on an electrical circuit. Nodal analysis is a method for determining the voltage at each node in an electrical circuit.

## How to Use

1. **Run the Program**: Run the `nodal_analysis` function in a Python environment. Upon execution, the program will prompt you to input the number of nodes, current sources at each node, and the admittances between nodes.

2. **Input Requirements**:
   - Number of nodes: Enter the total number of nodes in the circuit.
   - Current sources: For each node, enter the complex value of the current source.
   - Self-admittances: For each node, enter the complex value of the self-admittance.
   - Admittances between nodes: For each pair of nodes, enter the complex value of the admittance between them.

3. **Output**: The program will calculate and display the voltage at each node in the circuit.

## Example
```
Enter the number of nodes: 3
Enter current source at node 1: 5+2j
Enter current source at node 2: 3-1j
Enter current source at node 3: 1+4j
Enter admittance at node 1: 0.5-0.3j
Enter admittance at node 2: 0.6+0.2j
Enter admittance at node 3: 0.4-0.1j
Enter the admittance between nodes 1 and 2: 0.2-0.1j
Enter the admittance between nodes 1 and 3: 0.3+0.2j
Enter the admittance between nodes 2 and 3: 0.1-0.05j

Voltage of node 1: 2.917241379310345
Voltage of node 2: 2.2405172413793105
Voltage of node 3: 1.7862068965517242
```

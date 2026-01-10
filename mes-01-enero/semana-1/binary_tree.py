"""
Implementación de Árbol Binario.
Dia 2 - Enero 2026
"""

class Node:
    """
    Representa un nodo individual en el árbol.
    
    Atributos:
    data: valor almacenado en el nodo
    left: Referencia al hijo izquierdo (si lo tiene)
    right: Referencia al hijo derecho ( si lo tiene)
    """
    
    def __init__(self, data):
        """
        Inicializa un nodo con un valor.

        Args:
            data (int, str,): valor a almacenar ( puede ser int, str, etc.)
        """
        self.data = data
        self.left = None
        self.right = None
        
    def __str__(self):
        """Representación del un string del nodo."""
        return f"Node({self.data})"
    
    def __repr__(self):
        """Representación de un debugging"""
        return f"Node({self.data})"
    
'''# === TEST DE LA CLASE NODE ===
if __name__ == "__main__":
    print("===Testing Node Class ===")
    
    # Test 1: crear un nodo simple
    node = Node(5)
    print(f"Nodo creado: {node}")
    print(F"Data: {node.data}")
    print(f"Left: {node.left}")
    print(f"Rigth: {node.right}")
    
    # Test 2: agregar nodos manualmente
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    
    print(f"\nÁrbol simple:")
    print(f"Root: {root.data}")
    print(f"Left child: {root.left.data}")
    print(f"Right child: {root.right.data}")
    
    print("\n Node class funciona!")'''
    

class BinaryTree:
    """
    Árbol binario.
    
    Permite construir un árbol insertando hijos izquierdo/derecho en nodos específicos.
    """
    
    def __init__(self, root_data=None):
        """
        Inicializa el árbol.

        Args:
            root_data (_type_, optional): valor para el nodo raiz (None= árbol vacío)
        """
        if root_data is not None:
            self.root = Node(root_data)
        else:
            self.root = None
            
    def is_empty(self):
        """Verifica si el árbol está vacío."""
        return self.root is None
    
    def insert_left(self, parent_node, data):
        """
        Inserta un hijo izquierdo en el nodo dado.

        Args:
            parent_node (_type_): nodo padre donde insertar
            data (_type_): valor del nuevo nodo
            
        Returns:
            El nuevo nodo creado
        """
        if parent_node is None:
            raise ValueError("Parent node cannot be None")
        
        new_node = Node(data)
        parent_node.left = new_node
        return new_node
    
    def insert_right(self, parent_node, data):
        """
        Inserta un hijo derecho en el nodo dado.

        Args:
            parent_node (_type_): Padre donde insertar
            data (_type_): valor del nuevo nodo
        
        Returns:
            El nuevo nodo creado
        """
        if parent_node is None:
            raise ValueError("Parent node cannot be None")
        
        new_node = Node(data)
        parent_node.right = new_node
        return new_node
    
    def __str__(self):
        """Representación simple del árbol."""
        if self.is_empty():
            return "Empty Tree"
        return f"BinaryTree(root={self.root.data})"
    
# === TEST BINARY TREE ====
def test_binary_tree():
    """Test para la clase BinaryTree."""
    print("\n=== Testing BinaryTree Class ===")
    
    # Test 1: Árbol vacío
    tree = BinaryTree()
    print(f"Árbol vacío: {tree.is_empty()}") #True
    
    # Test2: Crear aŕbol con raíz
    tree = BinaryTree(1)
    print(f"\nAŕbol con raíz: {tree}")
    print(f"Root data: {tree.root.data}")
    
    # Test 3: Insertar hijos
    # Contruir el arbol:
    
    left_child = tree.insert_left(tree.root, 2)
    right_child = tree.insert_right(tree.root, 3)
    
    print(f"\nDespués de insertar hijos:")
    print(f"Root: {tree.root.data}")
    print(f"Left: {tree.root.left.data}")
    print(f"Right: {tree.root.right.data}")
    
    # Test 4: Construir u arbol mas complejo
    # Construir: 
    
    tree.insert_left(left_child, 4)
    
    print(f"\nÁrbol completo:")
    print(f"Root:{tree.root.data}")
    print(f"Root.left: {tree.root.left.data}")
    print(f"Root.right: {tree.root.right.data}")
    print(f"Root.left.left: {tree.root.left.left.data}")
    
    print("\nBinaryTree class funciona!")
   
# ===================================================================================   
def ejercicio_dia_2():
    """
    Construir el árbol:
        
    """
    print("\n===Ejercicio dia 2 ===")
    
    tree = BinaryTree("A")
    node_b = tree.insert_left(tree.root, "B")
    node_c = tree.insert_right(tree.root, "C")
    
    node_d = tree.insert_left(node_b, "D")
    node_e = tree.insert_right(node_b, "E")
    
    #insertar F hijo derecho de C
    node_f = tree.insert_right(node_c,"F")
    
    #Verificar
    print(f"Root:{tree.root.data}")
    print(f"Root.left (B): {tree.root.left.data}")
    print(f"Root.right (C): {tree.root.right.data}")
    print(f"Root.left.left (D): {tree.root.left.left.data} ")
    print(f"Root.right: (E): {tree.root.left.right.data}")
    print(f"Root.right,right (F): {tree.root.right.right.data}")
    
    print("\n Ejercicio completado!")
    
# ======================================================================================    
def evaluate_tree(node):
    
    if node is None:
        return 0
    
    # Si es numero (hoja) retornarlo
    if isinstance(node.data, (int,float)):
        return node.data
    
    # si es operador, evaluar hijos recursivamente
    left_val = evaluate_tree(node.left)
    right_val = evaluate_tree(node.right)
    
    #Aplicar operación
    if node.data == "+":
        return left_val + right_val
    elif node.data == "-":
        return left_val -right_val
    elif node.data == "*":
        return left_val * right_val
    elif node.data == "/":
        return left_val / right_val


def ejercicio_expresion():
    print("\n=== Ejercicio expresión ===")
    
    tree = BinaryTree("*")
    node_b = tree.insert_left(tree.root, "+")
    node_c = tree.insert_right(tree.root, "-")
    
    node_d = tree.insert_left(node_b, 5)
    node_e = tree.insert_right(node_b, 3)
    
    node_f = tree.insert_left(node_c, 8)
    node_g = tree.insert_right(node_c, 2)
    
    #Verificar
    print(f"Root (operator): {tree.root.data}")
    print(f"Left child of the root : {tree.root.left.data}")
    print(f"Right child of the root : {tree.root.right.data}")
    print(f"Leaf 1 : {tree.root.left.left.data}")
    print(f"Leaf 2 : {tree.root.left.right.data}")
    print(f"leaf 3 : {tree.root.right.left.data}")
    print(f"Leaf 4 : {tree.root.right.right.data}")
    
    resultado = evaluate_tree(tree.root)
    print(f"Resultado: {resultado}")
    print("\n Ejercicio completado")
        

# =====================================================================   
def ejercicio_bonus():
    print("\n=== Ejercicio BÓNUS ===")
    
    tree = BinaryTree("-")
    node_b = tree.insert_left(tree.root,"*")
    node_c = tree.insert_right(tree.root, "/")
    
    node_d = tree.insert_left(node_b, "+")
    node_e = tree.insert_right(node_b, 4)
    
    node_f = tree.insert_left(node_c, 6)
    node_g = tree.insert_right(node_c, 2)
    
    node_h = tree.insert_left(node_d, 2)
    node_i = tree.insert_right(node_d, 3)
    
    #Verificar
    print(f"Root (operator): {tree.root.data} ")
    print(f"Left child of the root: {tree.root.left.data}")
    print(f"Right child of the root: {tree.root.right.data}")
    print(f"left left child of the root: {tree.root.left.left.data}")
    print(f"left right child of the root: {tree.root.left.right.data}")
    print(f"Right left leaf of the root: {tree.root.right.left.data} ")
    print(f"Right right leaf of the root: {tree.root.right.right.data}")
    print(f"Left left left leaf of the root: {tree.root.left.left.left.data}")
    print(f"Left left right leaf of the root: {tree.root.left.left.right.data}")
    
    resultado = evaluate_tree(tree.root)
    print(f"Resultado: {resultado}")
    print("\n Ejercicio completado!")
      
       
if __name__ == "__main__":
    
    test_binary_tree()
    ejercicio_dia_2()
    ejercicio_expresion()
    ejercicio_bonus()
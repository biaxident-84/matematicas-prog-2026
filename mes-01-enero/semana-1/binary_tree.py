"""
Implementación de Árbol Binario.
Dia 2 - Enero 2026
"""

class Node:
    """
    Representa un nodo individual en el árrbol.
    
    Atributos:
    data: valor almacenado en el nodo
    left: Referencia al hijo izquierdo (si lo tiene)
    right: Refernecia al hijo derecho ( si lo tiene)
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
    
# === TEST DE LA CLASE NODE ===
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
    
    print("\n Node class funciona!")
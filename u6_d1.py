class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def edit_dna_sequence(dna_strand, m, n):
    ptr = dna_strand
    prev = None
    skipCtr, delCtr = 0, 0
    while ptr:
        if skipCtr <= m and delCtr == 0:
            prev = ptr
            ptr = ptr.next
            skipCtr += 1
            if skipCtr == m:
                delCtr = n
            continue
        else:
            skipCtr = 0
            delCtr -= 1
            prev.next = ptr.next
            ptr = ptr.next

    return dna_strand


# dna_strand = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10, Node(11, Node(12, Node(13)))))))))))))

# print_linked_list(edit_dna_sequence(dna_strand, 2, 3))

def cycle_length(protein):
    slow, fast = protein, protein.next
    while slow != fast:
        slow = slow.next
        fast = fast.next.next
    retList = []
    retList.append(slow.value)
    slow = slow.next
    while slow != fast:
        retList.append(slow.value)
        slow = slow.next
    return retList

# protein_head = Node('Ala', Node('Gly', Node('Leu', Node('Val'))))
# protein_head.next.next.next.next = protein_head.next 

# print(cycle_length(protein_head))

def split_protein_chain(protein, k):
    ptr = protein
    lenList = 0
    while ptr:
        lenList += 1
        ptr = ptr.next
    ptr = protein
    retList = []
    chunk = lenList // k
    chunks = [chunk for _ in range(k)]
    rem = lenList % k
    i = 0
    while rem != 0:
        chunks[i] += 1
        rem -= 1
        i += 1
    i = 0
    while ptr:
        dummy = Node(0)
        smPtr = dummy
        for j in range(chunks[i]):
            smPtr.next = Node(ptr.value)
            smPtr = smPtr.next
            ptr = ptr.next
        retList.append(dummy.next)
        i += 1

    return retList

protein1 = Node('Ala', Node('Gly', Node('Leu', Node('Val', Node('Pro', Node('Ser', Node('Thr', Node('Cys'))))))))
protein2 = Node('Ala', Node('Gly', Node('Leu', Node('Val'))))

parts = split_protein_chain(protein1, 3)
for part in parts:
    print_linked_list(part)

parts = split_protein_chain(protein2, 5)
for part in parts:
    print_linked_list(part)

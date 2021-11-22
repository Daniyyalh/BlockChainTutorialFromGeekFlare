import hashlib


class GeekCoinBlock:

    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = f"{' - '.join(transaction_list)} - {previous_block_hash}"
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

t1 = "Noah sends 5 GC to Mark"
t2 = "Mark sends 2.3 GC to James"
t3 = "James sends 4.2 GC to Alisson"
t4 = "Alisson sends 1.1 GC to Noah"


block1 = GeekCoinBlock('firstblock', [t1, t2])
block2 = GeekCoinBlock(block1.block_hash, [t3, t4])


print(f"Block 1 data: {block1.block_data}")
print(f"Block 1 hash: {block1.block_hash}")

print("")
print(f"Block 2 data: {block2.block_data}")
print(f"Block 2 hash: {block2.block_hash}")

# Prints
Block 1 data: Noah sends 5 GC to Mark - Mark sends 2.3 GC to James - firstblock
Block 1 hash: 01e4e15242a9601725f4a86ca01fbddaaec7105b442955bb0efcadbfc759806d

Block 2 data: James sends 4.2 GC to Alisson - Alisson sends 1.1 GC to Noah - 01e4e15242a9601725f4a86ca01fbddaaec7105b442955bb0efcadbfc759806d
Block 2 hash: 448c4306caf7f6937b0307f92f27fbea3bb73b3470363dee5026a1209dadcfa8



class Blockchain:
    def __init__(self):
        self.chain = []
        self.generate_genesis_block()

    def generate_genesis_block(self):
        self.chain.append(GeekCoinBlock("0", ['Genesis Block']))

    def create_block_from_transaction(self, transaction_list):
        previous_block_hash = self.last_block.block_hash
        self.chain.append(GeekCoinBlock(previous_block_hash, transaction_list))

    def display_chain(self):
        for i in range(len(self.chain)):
            print(f"Data {i + 1}: {self.chain[i].block_data}")
            print(f"Hash {i + 1}: {self.chain[i].block_hash}\n")

    @property
    def last_block(self):
        return self.chain[-1]

t1 = "George sends 3.1 GC to Joe"
t2 = "Joe sends 2.5 GC to Adam"
t3 = "Adam sends 1.2 GC to Bob"
t4 = "Bob sends 0.5 GC to Charlie"
t5 = "Charlie sends 0.2 GC to David"
t6 = "David sends 0.1 GC to Eric"

myblockchain = Blockchain()

myblockchain.create_block_from_transaction([t1, t2])
myblockchain.create_block_from_transaction([t3, t4])
myblockchain.create_block_from_transaction([t5, t6])

myblockchain.display_chain()

#prints
Data 1: Genesis Block - 0
Hash 1: 39331a6a2ea1cf31a5014b2a7c9e8dfad82df0b0666e81ce04cf8173cc5aed3e

Data 2: George sends 3.1 GC to Joe - Joe sends 2.5 GC to Adam - 39331a6a2ea1cf31a5014b2a7c9e8dfad82df0b0666e81ce04cf8173cc5aed3e
Hash 2: 98cf363aecb33989aea0425a3c1287268bd86f63851bc08c0734a31db08506d5

Data 3: Adam sends 1.2 GC to Bob - Bob sends 0.5 GC to Charlie - 98cf363aecb33989aea0425a3c1287268bd86f63851bc08c0734a31db08506d5
Hash 3: 6f1cfcc3082488b97db8fdf8ed33f9ac7519be3e285a37a6fcc2f1904f373589

Data 4: Charlie sends 0.2 GC to David - David sends 0.1 GC to Eric - 6f1cfcc3082488b97db8fdf8ed33f9ac7519be3e285a37a6fcc2f1904f373589
Hash 4: 869df2f03c9860767d35b30a46233fbeea89a3000ae5019d1491e3829d1ab929
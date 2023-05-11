# Build_Blockchain_in_Python

This repo is a learning path of creating a blockchain in terms of POW (Prove-of-Work) from scratch to a simple chain by using Python.

There are two parts of the repo:

1. Algorithms of Encryption

   1.1 [Simple Hash](./Simple_Hash.py) <br/>
   1.2 [Caesar Encrypt](./Caesar_Encrypt.py) <br/>
   1.3 [Monoalphabetic Encryption](./Monoalphabetic_Encryption.py) <br/>
   1.4 [XOR Cipher](./XOR_Cipher.py) <br/>
   1.5 [SPN Cipher](./SPN_Cipher.py) <br/>

2. Building a simple blockchain step by step

   2.1 [Fundamental structure of a blockchain](./2-1.py)
   <br/>
   2.2 [Create genesis block and mining new blocks](/2-2.py)
   <br/>
   2.3 [Adjust difficulty and confirm hash chain](/2-3.py) <br/>
   2.4 [Public key, Private key, and Sign](/2-4.py) <br/>
   2.5 [Stream Socket](/2-5_server.py) (server) / [Client](/2-5_client.py) <br/>
   2.6 [Clone blocks and Broadcast between nodes](/2-6_server.py) <br/>

<br/>

# Get Started

## Part 1 - Testing functions

Now, we can test transaction funtion by running blockchain server and client.

1. Open a new Terminal and run blockchain server with port. You may see a pair of publick address and private key. These are Miner's info.

```Python
Python 2-5_server.py PORT_NUMBER
# e.g. server running 127.0.0.1:1111
```

2. Open a new Terminal and run blockchain client with the port as same as the server's port.

```Python
Python 2-5_client.py PORT_NUMBER
# e.g. client running 127.0.0.1:1111
```

3. Now, you may see the Command list in the client terminal.

```
Command list:
1. generate_address
2. get_balance
3. transaction
```

4. Enter 1 to create a pair of public address and private key which have been encrypted with RSA algorithm. These are User's info.
5. Enter 2 to check balance within the address.
6. Enter 3 to start a transaction by entering Miner's public address (sender), private key, User's address (receiver), amount and fee to complete a transaction.
7. Enter 2 to check balance. (need to wait for a while during mining...)

<br/>

## Part 2 - Decentralisation

Now, after testing and completing function codes, we can optimise our codes by adding broadcasting and verification.

1. Open a new Terminal and run blockchain server with port. This is the first node running, e.g. `127.0.0.1:1111`.

```Python
Python 2-6_server.py PORT_NUMBER
```

2. Open a new Terminal and run the seconde node with a new port in order to connect to the first node, e.g. `127.0.0.1:1112`.

```Python
Python 2-6_server.py NEW_PORT_NUMBER
# Python 2-6_server.py 1112 127.0.0.1:11
```

3. Now, you may observe how the simple blockchain broadcasts and synchronise transactions between to different nodes.

<br/>

# Reference

[區塊鏈生存指南](https://www.books.com.tw/products/0010931871) (Traditional Chinese)

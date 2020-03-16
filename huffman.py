import heapq
import functions

# Reading and Defining Files
import sys
command = sys.argv[1]
src = open(sys.argv[2], "r")
arr = src.read()
src.close()

# Frequency Dictionary
freq = functions.build_freq_dict(arr)

# Building Huffman Tree
root = functions.build_huffman_tree(freq)

# Build Encoding Dictionary
encoding_dict = dict()
functions.dfs(root, '', encoding_dict)

# Build Decoding Dictionary
decoding_dict = functions.build_decoding_dict(encoding_dict)

# encode file
if (command == 'encode') :
    target = open(sys.argv[3], "w")
    functions.encode(arr, target, encoding_dict)
    target.close()

# decode file
elif (command == 'decode') :
    target = open(sys.argv[3], "r")
    decode_target = open(sys.argv[4], "w")
    functions.decode(target.read(), decode_target, decoding_dict)
    target.close()
    decode_target.close()

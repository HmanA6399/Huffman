from Node import Node

def build_freq_dict(arr) :
    freq = dict()
    for ch in arr:
        if (ch not in freq.keys()):
            freq[ch] = Node(1, ch)
        else:
            freq[ch].value += 1
    return freq

def build_huffman_tree(freq_arr) :
    heap = [v for v in freq_arr.values()]
    while (len(heap) > 1) :
        heap.sort()
        first = heap.pop(0)
        second = heap.pop(0)
        new = first + second
        new.left  = first
        new.right = second
        heap.insert(0, new)
    return heap[0]

def dfs(curr, code, codeDict):
    if (curr is None) : # Protection
        return

    if (curr and curr.char != None): # Leaf
        # print("%c : %d"%(curr.char, curr.value))
        codeDict[curr.char] = code
        return
    # print("None : %d"%(curr.value))
    dfs(curr.left, code + '0', codeDict)
    dfs(curr.right, code + '1', codeDict)

def build_decoding_dict(enc_dict):
    dec_dict = dict()
    for k,v in enc_dict.items() :
        dec_dict[v] = k
    return dec_dict

def encode(src, targetFile, enc_dict) :
   for e in src :
        targetFile.write(enc_dict[e])


def decode(src, targetFile, dec_dict) :
    code = ''
    for ch in src :
        code += ch
        if code in dec_dict.keys() :
            print(code)
            print(dec_dict[code])
            targetFile.write(dec_dict[code])
            code = ''
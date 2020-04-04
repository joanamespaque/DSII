f = input("digita uma frase ai:")
def inverte(frase):
    nova = ""
    c = len(frase)-1
    while c >= 0:
        nova = nova+frase[c]
        c = c-1
    return nova
print(inverte(f))
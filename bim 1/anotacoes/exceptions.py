#  exceptions: 
#     -> tratamento de erros
#     -> trecho de código crítico 
#         ex: entrada e saída de dados
    
#     SINTAXE: (PYTHON)
#     try:
#         <código crítico>
#     except <tipo excpetion 1> as e1:
#         <tratamento 1>
#     except <tipo exception 2> as e2:
#         <tratamento 2>
    

def divisao(x,y):
    try:
        return float(x)/float(y)
    except ValueError as vr:
        print("erro: deve digitar numeros")
        raise vr
    except ZeroDivisionError as zde:
        print("erro: sem divisoes por zero")
        raise zde 

def main():
    while True:
        print("algoritmo de divisao")
        x = input("digite um numero")
        y = input("digite outro numero")
        try:
            z = divisao(x,y)
        except BaseException:
            print("tente de novo!/n")
        else:
            print(z)
            break

if __name__ == '__main__':
    main()
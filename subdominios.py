import dns.resolver
from os import path

def main():
    if path.exists('./subdominios.txt'):
        wordlist = open('./subdominios.txt','r')
        wordlist = wordlist.read().split('\n')
        lista = []
        try:
            for sub in wordlist:
                resolve = dns.resolver.resolve( f'{sub}.google.com', 'A' )
                lista.append(f'{sub}.google.com')
        except:
            long_list = len(lista)
            if long_list > 0:
                print(f'numero de subdominios posibles es igual a {long_list}')
                for e in lista:
                    print(e)
            else:
                print('no se encontraron subdominios')
    else:
        print('no existe el archivo')
        if __name__ == '__main__':
            try:
                main()
            except KeyboardInterrupt:
                exist()

main()
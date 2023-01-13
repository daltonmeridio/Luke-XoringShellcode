from distutils.log import error
import sys
import argparse

def banner():
    print ("""
                 _______________
                / \     / \     / \/
                |------------------|======|
                | --    --    --    |==============llll----i++
                |__________________|======|
                |             |
                |             |
                |             |
                |             |
                |             |
                |             |
                /`~\   /~~\   \  /~~\              
                /   ~~`~    \ /~~~~   \      
                /             \         \/
    """)
    print("\t\t\t\tby Dalt0x6e")

def Xor_encode(shellcode, key):
    shell_encode = ""

    print ("[+] Cifrando shellcode... ")

    for nop in shellcode:
        nop = int(nop, 16)

        if nop == 0:
            print("[*] Limpiando byte null...")
            #nop += 1
        
        key_xor = nop ^ key 
        shell_encode += "\\x"
        shell_encode += "%02x" % key_xor

    return shell_encode 



def error():
    parser.print_help()
    exit(1)


if __name__ == '__main__':

    banner()

    parser = argparse.ArgumentParser(description='[+] Sifrado de ShellCode')
    parser.add_argument('-s', '--shellcode', help='\t ShellCode para sifrar')
    parser.add_argument('-k', '--key', help='\tLlave XOR')
    args, unknown = parser.parse_known_args()
  

    shellcode = args.shellcode if args.shellcode != None else error()
    shellcode = shellcode[2:]   
    shellcode = shellcode.split("\\x")

    key = args.key if args.key != None else error()
    key = int(key, 16)
    shell = Xor_encode(shellcode, key)
    
    print(f'{shell}')

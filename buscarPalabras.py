arch = open("palabras.txt",'r')
import re
referencias = { 0: '(r|rr)',
                1: '(d|t)',
                2: '(n|ñ)',
                3: '(m|w)',
                4: '(c|q|k)',
                5: '(l|ll)',
                6: '(s|z)',
                7: '(j|f)',
                8: '(ch)',
                9: '(v|b|p)'}

diez_primeros = ['00','01','02','03','04','05','06','07','08','09']

def convertir_regex(numero):
    numero1 = int(numero[0:1])
    numero2 = int(numero[1:])
    return '^(a|e|i|o|u|y|h)*' + referencias[numero1] + '(a|e|i|o|u|y|h)*' + referencias[numero2] + '(a|e|i|o|u|y|h)*\n'

def num_regex():
    retorno = []
    for i in diez_primeros:
        retorno.append({i:convertir_regex(i)})
    for j in range(10,100):
        j = str(j)
        retorno.append({j:convertir_regex(j)})
    return retorno

palabras = arch.readlines()
arch.close()

def palabras_por_regex(regex):
    retorno = []
    for palabra in palabras:
        if re.match(regex,palabra): retorno.append(palabra)
    return retorno

def proceso():
    num_regexs = num_regex()
    arch = open("palabrasfiltradas.txt",'w')
    for num_regexx in num_regexs:
        for num, regex in num_regexx.items():
            arch.write(str(num) + " : " + str(palabras_por_regex(regex)))
    arch.close()

proceso()





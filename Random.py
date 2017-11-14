import random

DesafioWeb = str(input('Escolha o número da opção que deseja ver: 1- Bullet Point. 2- Seleção por número. 3- Random. '))

if DesafioWeb == '1':
    print("Aqui estão todas as frases:",
        "\n1 - Beautiful is better than ugly.",
        "\n2 - Explicit is better than implicit.",
        "\n3 - Simple is better than complex.",
        "\n4 - Complex is better than complicated.",
        "\n5 - Flat is better than nested.",
        "\n6 - Sparse is better than dense.",
        "\n7 - Readability counts.",
        "\n8 - Special cases aren't special enough to break the rules.",
        "\n9 - Although practicality beats purity.",
        "\n10 - Errors should never pass silently.",
        "\n11 - Unless explicitly silenced.",
        "\n12 - In the face of ambiguity, refuse the temptation to guess.",
        "\n13 - There should be one-- and preferably only one --obvious way to do it.",
        "\n14 - Although that way may not be obvious at first unless you're Dutch.",
        "\n15 - Now is better than never.",
        "\n16 - Although never is often better than *right* now.",
        "\n17 - If the implementation is hard to explain, it's a bad idea.",
        "\n18 - If the implementation is easy to explain, it may be a good idea.",
        "\n19 - Namespaces are one honking great idea -- let's do more of those!")
elif DesafioWeb == '2':
    DesafioWebNumérico = str(input("Selecione um número entre 1 e 19: "))
    if DesafioWebNumérico == '1':
        print("1 - Beautiful is better than ugly.")
    elif DesafioWebNumérico == '2':
        print("2 - Explicit is better than implicit.")
    elif DesafioWebNumérico == '3':
        print("3 - Simple is better than complex.")
    elif DesafioWebNumérico == '4':
        print("4 - Complex is better than complicated.")
    elif DesafioWebNumérico == '5':
        print("5 - Flat is better than nested.")
    elif DesafioWebNumérico == '6':
        print("6 - Sparse is better than dense.")
    elif DesafioWebNumérico == '7':
        print("7 - Readability counts.")
    elif DesafioWebNumérico == '8':
        print("8 - Special cases aren't special enough to break the rules.")
    elif DesafioWebNumérico == '9':
        print("9 - Although practicality beats purity.")
    elif DesafioWebNumérico == '10':
        print("10 - Errors should never pass silently.")
    elif DesafioWebNumérico == '11':
        print("11 - Unless explicitly silenced.")
    elif DesafioWebNumérico == '12':
        print("12 - In the face of ambiguity, refuse the temptation to guess.")
    elif DesafioWebNumérico == '13':
        print("13 - There should be one-- and preferably only one --obvious way to do it.")
    elif DesafioWebNumérico == '14':
        print("14 - Although that way may not be obvious at first unless you're Dutch.")
    elif DesafioWebNumérico == '15':
        print("15 - Now is better than never.")
    elif DesafioWebNumérico == '16':
        print("16 - Although never is often better than *right* now.")
    elif DesafioWebNumérico == '17':
        print("If the implementation is hard to explain, it's a bad idea.")
    elif DesafioWebNumérico == '18':
        print("18 - If the implementation is easy to explain, it may be a good idea.")
    elif DesafioWebNumérico == '19':
        print("19 - Namespaces are one honking great idea -- let's do more of those!")
    else:
        print('Número informado inválido.')

elif DesafioWeb == '3':
    n1 = ("1 - Beautiful is better than ugly.")
    n2 = ("2 - Explicit is better than implicit.")
    n3 = ("3 - Simple is better than complex.")
    n4 = ("Complex is better than complicated.")
    n5 = ("Flat is better than nested.")
    n6 = ("Sparse is better than dense.")
    n7 = ("Readability counts.")
    n8 = ("Special cases aren't special enough to break the rules.")
    n9 = ("Although practicality beats purity.")
    n10 = ("Errors should never pass silently.")
    n11 = ("Unless explicitly silenced.")
    n12 = ("In the face of ambiguity, refuse the temptation to guess.")
    n13 = ("There should be one-- and preferably only one --obvious way to do it.")
    n14 = ("Although that way may not be obvious at first unless you're Dutch.")
    n15 = ("Now is better than never.")
    n16 = ("Although never is often better than *right* now.",)
    n17 = ("If the implementation is hard to explain, it's a bad idea.")
    n18 = ("If the implementation is easy to explain, it may be a good idea.")
    n19 = ("Namespaces are one honking great idea -- let's do more of those!")
    listan = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15, n16, n17, n18, n19]
    nescolhido = random.choice(listan)
    print("A mensagem escolhida foi: "+nescolhido)
else:
# while DesafioWeb != range('1', '2', '3'):
        print('Por favor escolha 1, 2 ou 3.')


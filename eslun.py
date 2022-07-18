def perimetro ():
        print("il programma calcola il perimetro di una figura geometrica")
        print(""" 
        - Quadrato>>1
        - Rettangolo >>2
        - Cerchio >>3
        - Triangolo Rettangolo >>4 """)

        print('Inserire la scelta: ')
        scelta = int(input(">>>")) 
        if scelta == 1: 
           print("Hai selezionato il perimetro Quadrato")
           lato = float (input("Inserisci il valore del lato del quadrato")) 
           print("Il perimetro del Quadrato, avente lato", lato, "e:" , lato *4) 
        elif scelta == 2: 
             print("Hai selezionato il perimetro del Rettangolo") 
             base = float(input("Inserisci il valore della base")) 
             altezza = float (input("Inserisci il valore dell altezza")) 
             print("Il perimetro del Rettangolo, avente base" , base, "e altezza" ,altezza, "e: ", base*2 + 2*altezza)
        elif scelta == 3:
             print("Hai scelto il perimetro del Cerchio")
             diametro = float(input("Inserisci il valore del diametro"))
             print("Il perimetro del Cerchio, avente diametro", diametro, "e PIGreco", 3.14,"e:" , diametro * 3.14)
        elif scelta == 4:
             print("Hai selezionato il perimetro del Triangolo Equilatero")
             lato = float (input("Inserisci il valore del lato del triangolo"))
             print("Il perimetro del triangolo equilatero, avente lato", lato, "e: ", 3*lato)
        else:
            print ("Inserire scelta valida") 
perimetro();


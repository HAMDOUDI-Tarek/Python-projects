import random    #pour la fonction de Mutation

def complement (ADN):       #fonction de complement d'ADN
    transcript = {"A":"T", "T":"A", "G":"C", "C":"G"}        #dictionnaire de complementarité
    return "".join([transcript[letter] for letter in ADN.upper()])


def transcription(ADN):       #fonction de la traduction
    return ADN.replace("T", "U")

def traduction(ADN):
    
    code_genetique = {
                "UUU":"F","UUC":"F",
                "CUU":"L","CUC":"L","CUA":"L","CUG":"L","UUA":"L","UUG":"L",
                "AUU":"I","AUC":"I","AUA":"I",
                "AUG":"M",
                "GUU":"V","GUC":"V","GUA":"V","GUG":"V",
                "UCU":"S","UCC":"S","UCA":"S","UCG":"S","AGU":"S","AGC":"S",
                "CCU":"P","CCC":"P","CCA":"P","CCG":"P",
                "ACU":"T","ACC":"T","ACA":"T","ACG":"T",
                "GCU":"A","GCC":"A","GCA":"A","GCG":"A",
                "UAA":"*","UAG":"*","UGA":"*",
                "UAU":"Y","UAC":"Y",
                "CAU":"H","CAC":"H",
                "CAA":"Q","CAG":"Q",
                "AAU":"N","AAC":"N",
                "AAA":"K","AAG":"K",
                "GAU":"D","GAC":"D",
                "GAA":"E","GAG":"E",
                "UGU":"C","UGC":"C",
                "UGG":"W",
                "CGU":"R","CGC":"R","CGA":"R","CGG":"R","AGA":"R","AGG":"R",
                "GGU":"G","GGC":"G","GGA":"G","GGG":"G"
                }
    
    return "".join([code_genetique[ADN[i:i+3]] for i in range(0, len(ADN), 3)])
    


def Mutation(ADN):  #mutation (on ne l'utilise pas dans notre programme)
    seq = ''
    choix = random.randint(1,3)     #choisir une motation aléatoire
    print("Choice: ", choix)
    if choix == 1:
        print('Substitution')       #le premier type de mutation est la substitution
        
        mutatedSeq = [c for c in ADN]       #un liste contenant les bases nucléotidiques
        
        position = random.randint(0,len(ADN)-1)     #choisir un posistion aléatoire
        c = random.choice(["A", "T", "C", "G"])     #choisir une lettre aléatoire
        while c == mutatedSeq[position]:
            c = random.choice(["A", "T", "C", "G"])     #choisir un lettre differérente que celle existant dans la position précise
        mutatedSeq[position] = c        #remplacer la position avec la nouvelle lettre
        
        for c in mutatedSeq:
            seq += c
    
    elif choix == 2:
        print('Deletion')       #the 2ème type de mutation est la délétion
        position = random.randint(1,len(ADN)-1)     #choisir un posistion aléatoire
        mutatedSeq = []
        i = 1
        
        for c in ADN:
            if  i != position:
                mutatedSeq.append(c)        #ajouter les lettre à la nouvelle liste jusqu'a ce qu'on atteigne la position désirée, on ne l'ajoute pas
                i = i+1
            else:
                i = i+1
        for c in mutatedSeq:
            seq += c
            
    elif choix == 3:
        print('Insertion')      #le 3ème type de mutation est l'insertion
        position = random.randint(1,len(ADN)-1)     #choisir un posistion aléatoire
        mutatedSeq = []
        m = random.choice(["A", "T", "C", "G"])     #choisir une lettre aléatoire à inserer dans la séquence
        i = 1
        
        for c in self.sequence:
            if i == position:       #si on est à la position désirée
                mutatedSeq.append(m)        #ajouter la lettre aléatoire
                mutatedSeq.append(c)        #ajouter la lettre suivante de la séquence
            else:
                mutatedSeq.append(c)        #ajouter les lettre normalement
            i = i+1
            
        for c in mutatedSeq:
            seq += c
    return seq          #la séquence resultante


def LireSequenceFasta(chemain):     #parcourir le chemain donné
    return SeqIO.read(chemain, 'fasta').seq         #retourner la séquence protéique trouvée

def ScanSequence(seq):      #rechercher les motifs d'une séquence protéique
    return [motif["signature_ac"] for motif in ScanProsite.read(ScanProsite.scan(seq))]         #retourner les motifs trouvés
    

def aff(acc_numbers):       #afficher les information des motifs
    inf = Prosite.read(ExPASy.get_prosite_raw(acc_numbers))         #créer un objet contenant les informations des motifs
    for info in [inf.description, inf.accession, inf.nr_positive, inf.nr_false_pos, inf.nr_false_neg]:
        print(info)     #afficher les motifs précisés
    print("_"*10)       #séparer avec des traits
    
if __name__ == "__main__":
    
    fichier = open('séquences.txt', 'w')        #créer un fichier avec le nom "séquences" et l'ouvrir en mode écriture

    for i in range(1,4):       #damander 10 fois à l'utilisateur d'entrer une séquence
        seq=input("Entrez la séquence n°" + str(i) + ": ")       #écrire la séquence ADN
        fichier.write(seq + '\n')       #ajouter la séquence au fichier .txt
        fichier.flush()

    fichier = open('séquences.txt')       #ouvrir le fichier en mode lecture
    i=1         #indice utilisé pour distinguer entre les fichiers

    for line in fichier:        #accéder les séquence une par une dans le premier fichier
        file_name = input("Fichier et numéro: ")       #pour ne pas utiliser le même nom d'ouverture, chaque fois l'utilisateur entre un nom different
        file_name = open(str(i)+'ème sequence.txt', 'w')      #ouvrir un fichier different à chaque fois
        file_name.write(line)       #écrire une séquence dans un fichier .txt séparé

        for char in range(len(line)-1):
            file_name.write("|")        #ajouter les batonnêts de correspondance
            
        file_name.write('\n' + complement(line) + '\n')          #écrir la séquence complémentaire en dessous

        for char in range(len(line)-1):
            file_name.write("|")

        file_name.write("\n" + transcription(line) + "\n")      #écrire la séquence ARN correspondante
        file_name.flush()

        file
        i+=1

        file_name.write(traduction(line))
        file_name = flush()
        
    file.close()
    
    for motif in ScanSequence(LireSequenceFasta(input("Entrer le chemain de vos motifs: ")):      #scanner les motifs existant dans le fichier donné
        aff(motif)      #afficher les informations des motifs trouvés



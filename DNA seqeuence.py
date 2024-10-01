import tkinter as tk
from tkinter import filedialog, messagebox

# Fonctions de complément, transcription et traduction d'ADN
def complement(ADN):
    transcript = {"A": "T", "T": "A", "G": "C", "C": "G"}
    ADN = ADN.upper()
    
    # Vérifier que la séquence contient uniquement des bases ADN valides
    for letter in ADN:
        if letter not in transcript:
            messagebox.showerror("Erreur", f"Base non valide trouvée : {letter}")
            return ""
    
    return "".join([transcript[letter] for letter in ADN])

def transcription(ADN):
    return ADN.replace("T", "U")

def traduction(ADN):
    code_genetique = {
        "UUU":"F","UUC":"F","CUU":"L","CUC":"L","CUA":"L","CUG":"L","UUA":"L","UUG":"L",
        "AUU":"I","AUC":"I","AUA":"I","AUG":"M","GUU":"V","GUC":"V","GUA":"V","GUG":"V",
        "UCU":"S","UCC":"S","UCA":"S","UCG":"S","AGU":"S","AGC":"S","CCU":"P","CCC":"P","CCA":"P","CCG":"P",
        "ACU":"T","ACC":"T","ACA":"T","ACG":"T","GCU":"A","GCC":"A","GCA":"A","GCG":"A",
        "UAA":"*","UAG":"*","UGA":"*","UAU":"Y","UAC":"Y","CAU":"H","CAC":"H","CAA":"Q","CAG":"Q",
        "AAU":"N","AAC":"N","AAA":"K","AAG":"K","GAU":"D","GAC":"D","GAA":"E","GAG":"E","UGU":"C","UGC":"C","UGG":"W",
        "CGU":"R","CGC":"R","CGA":"R","CGG":"R","AGA":"R","AGG":"R","GGU":"G","GGC":"G","GGA":"G","GGG":"G"
    }
    return "".join([code_genetique[ADN[i:i+3]] for i in range(0, len(ADN), 3)])

# Interface Graphique
def ouvrir_fichier():
    filename = filedialog.askopenfilename(title="Choisir un fichier texte", filetypes=(("Fichiers texte", "*.txt"),))
    with open(filename, 'r') as file:
        seq_entry.delete(1.0, tk.END)
        seq_entry.insert(tk.END, file.read())

def enregistrer_fichier(seq):
    filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("Fichiers texte", "*.txt"),))
    if filename:
        with open(filename, 'w') as file:
            file.write(seq)

def traiter_sequence():
    ADN = seq_entry.get(1.0, tk.END).strip()  # Nettoyer les espaces et nouvelles lignes
    print(f"Séquence entrée : {ADN}")  # Diagnostic
    if not ADN:
        messagebox.showerror("Erreur", "Veuillez entrer une séquence d'ADN.")
        return

    comp = complement(ADN)
    if not comp:  # Si une erreur est survenue dans le complément, on arrête ici.
        return
    
    arn = transcription(ADN)
    prot = traduction(arn)

    result_text = f"Séquence complémentaire : {comp}\nSéquence ARN : {arn}\nChaîne protéique : {prot}"
    result_label.config(text=result_text)

def sauvegarder_resultat():
    result = result_label.cget("text")
    enregistrer_fichier(result)

# Configuration de l'interface
root = tk.Tk()
root.title("Analyse de séquences ADN")

# Création des composants
seq_label = tk.Label(root, text="Entrer une séquence ADN :")
seq_label.pack()

seq_entry = tk.Text(root, height=4, width=50)
seq_entry.pack()

ouvrir_btn = tk.Button(root, text="Ouvrir un fichier", command=ouvrir_fichier)
ouvrir_btn.pack()

traiter_btn = tk.Button(root, text="Traiter la séquence", command=traiter_sequence)
traiter_btn.pack()

result_label = tk.Label(root, text="", wraplength=400)
result_label.pack()

sauvegarder_btn = tk.Button(root, text="Sauvegarder les résultats", command=sauvegarder_resultat)
sauvegarder_btn.pack()

# Lancer l'application
root.mainloop()

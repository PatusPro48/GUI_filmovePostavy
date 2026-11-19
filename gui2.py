import tkinter as tk

postavy = []

try:
    with open("postavy.txt", "r", encoding="utf-8") as soubor:
        for radek in soubor:
            radek = radek.strip()

            if not radek:
                continue

            casti = radek.split("#")

            if len(casti) != 6:
                continue

            try:
                postava = {
                    "jmeno": casti[0],
                    "vek": int(casti[1]),
                    "pohlavi": casti[2],
                    "zvire": casti[3],
                    "datum": casti[4],
                    "oblibenost": float(casti[5]),
                    "moje_oblibena": False
                }

                postavy.append(postava)

            except ValueError:
                continue

except FileNotFoundError:
    print("Soubor postavy.txt nebyl nalezen!")
print(postavy)

if len(postavy) == 0:
    print("Žádné postavy nebyly načteny!")
    exit()

okno = tk.Tk()
okno.title("Filmové postavy")
okno.geometry("400x300")
okno.configure(bg="lightblue")

index = 0

text = tk.Label(okno, text=postavy[index]["jmeno"])
text.pack()


udaje = tk.Label(okno, text=
    f"Věk: {postavy[index]['vek']}\n"
    f"Pohlaví: {postavy[index]['pohlavi']}\n"
    f"Zvíře: {postavy[index]['zvire']}\n"
    f"Datum: {postavy[index]['datum']}\n"
    f"Oblíbenost: {postavy[index]['oblibenost']}"
)
udaje.pack()

def dalsi():
    global index

    if index < len(postavy) - 1:
        index = index + 1

    text.config(text=postavy[index]["jmeno"])

    udaje.config(text=
        f"Věk: {postavy[index]['vek']}\n"
        f"Pohlaví: {postavy[index]['pohlavi']}\n"
        f"Zvíře: {postavy[index]['zvire']}\n"
        f"Datum: {postavy[index]['datum']}\n"
        f"Oblíbenost: {postavy[index]['oblibenost']}"
    )

def predchozi():
    global index

    if index > 0:
        index = index - 1

    text.config(text=postavy[index]["jmeno"])

    udaje.config(text=
        f"Věk: {postavy[index]['vek']}\n"
        f"Pohlaví: {postavy[index]['pohlavi']}\n"
        f"Zvíře: {postavy[index]['zvire']}\n"
        f"Datum: {postavy[index]['datum']}\n"
        f"Oblíbenost: {postavy[index]['oblibenost']}"
    )

def kontrola():
    if oblibena.get():
        vysledek.config(text="Moje oblíbená postava")
    else:
        vysledek.config(text="Moje neoblíbená postava")

def dalsi():
    global index

    postavy[index]["moje_oblibena"] = oblibena.get()

    if index < len(postavy) - 1:
        index = index + 1

    oblibena.set(postavy[index]["moje_oblibena"])

    text.config(text=postavy[index]["jmeno"])

    udaje.config(text=
        f"Věk: {postavy[index]['vek']}\n"
        f"Pohlaví: {postavy[index]['pohlavi']}\n"
        f"Zvíře: {postavy[index]['zvire']}\n"
        f"Datum: {postavy[index]['datum']}\n"
        f"Oblíbenost: {postavy[index]['oblibenost']}"
    )

tlacitko = tk.Button(okno, text="Další", command=dalsi)
tlacitko.pack(pady=5)

tlacitko2 = tk.Button(okno, text="Předchozí", command=predchozi)
tlacitko2.pack(pady=5)

oblibena = tk.BooleanVar()

checkbox = tk.Checkbutton(
    okno,
    text="Moje oblíbená postava",
    variable=oblibena
)
checkbox.pack(pady=10)

vysledek = tk.Label(okno, text="")
vysledek.pack()

tlacitko3 = tk.Button(okno, text="Zkontrolovat", command=kontrola)
tlacitko3.pack(pady=15)

okno.mainloop()
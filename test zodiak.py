import tkinter as tk

window = tk.Tk()
window.title("Cek Zodiak")

lbl = tk.Label(window, text= "Tentukan Zodiakmu")
lbl.grid(column=0, row=0)

lbl1 = tk.Label(window, text = "Masukkan Tanggal Lahir : ")
lbl1.grid(column=1, row=1)
entry1 = tk.Entry(window, width=10)
entry1.grid(column=2, row=1)

lbl2 = tk.Label(window, text = "Masukkan Bulan Lahir : ")
lbl2.grid(column=1, row=2)
entry2 = tk.Entry(window, width=10)
entry2.grid(column=2, row=2)

lbl3 = tk.Label(window, text = "Zodiak Anda Adalah : ")
lbl3.grid(column=1, row=3)

zodiak_saya = tk.Entry(window, width=10)
zodiak_saya.grid(column=2, row=3)

Tanggal = entry1.get()
Bulan = entry2.get()

get_button = tk.Button(window,text = "TES", anchor=tk.CENTER,command=lambda:get_zodiak(Tanggal,Bulan),height=2,width=20,bg = "black", fg="white")


def get_zodiak(Tanggal,Bulan):
    global zodiak_saya
    zodiak_saya.grid_forget()
    Tanggal = int(entry1.get())
    Bulan = entry2.get()
    if Bulan == "desember"or "Desember":
        zodiak_saya.insert(0, "Sagittarius") if (Tanggal < 22) else zodiak_saya.insert(0, 'Capricorn') 
        zodiak_saya.grid(column=2, row=3)
    elif Bulan == 'januari' or 'Januari':
        zodiak_saya.insert(0, 'Capricorn') if (Tanggal < 20) else zodiak_saya.insert(0, 'Aquarius')
        zodiak_saya.grid(column=2, row=3)
    elif Bulan == 'februari' or 'Februari':
        zodiak_saya.insert(0, 'Aquarius') if (Tanggal < 19) else zodiak_saya.insert(0, 'Pisces')
        zodiak_saya.grid(column=2, row=3)
    elif Bulan == 'maret' or 'Maret':
        zodiak_saya.insert(0, 'Pisces') if (Tanggal < 21) else zodiak_saya.insert(0, 'Aries')
        zodiak_saya.grid(column=2, row=3)
    elif Bulan == 'april' or 'April':
        zodiak_saya.insert(0, 'Aries') if (Tanggal < 20) else zodiak_saya.insert(0, 'Taurus')
        zodiak_saya.grid(column=2, row=3)
    elif Bulan == 'mei' or 'Mei':
        zodiak_saya.insert(0, 'Taurus') if (Tanggal < 21) else zodiak_saya.insert(0, 'Gemini')
        zodiak_saya.grid(column=2, row=3)
    elif Bulan == 'juni' or 'Juni':
        zodiak_saya.insert(0, 'Gemini') if (Tanggal < 21) else zodiak_saya.insert(0, 'Cancer')
        zodiak_saya.grid(column=2, row=3)
    elif Bulan == 'juli' or 'Juli':
        zodiak_saya.insert(0, 'Cancer') if (Tanggal < 23) else zodiak_saya.insert(0, 'Leo')
        zodiak_saya.grid(column=2, row=3)
    elif Bulan == 'agustus' or 'Agustus':
        zodiak_saya.insert(0, 'Leo') if (Tanggal < 23) else zodiak_saya.insert(0, 'Virgo')
        zodiak_saya.grid(column=2, row=3)
    elif Bulan == 'september' or 'September':
        zodiak_saya.insert(0, 'Virgo') if (Tanggal < 23) else zodiak_saya.insert(0, 'Libra')
        zodiak_saya.grid(column=2, row=3)
    elif Bulan == 'oktober' or 'Oktober':
        zodiak_saya.insert(0, 'Libra') if (Tanggal < 23) else zodiak_saya.insert(0, 'scorpio')
        zodiak_saya.grid(column=2, row=3)
    elif Bulan == 'november' or 'November':
        zodiak_saya.insert(0, 'scorpio') if (Tanggal < 22) else  zodiak_saya.insert(0, "Sagittarius")
        zodiak_saya.grid(column=2, row=3)


get_button.grid(row = 4,column = 0,columnspan=2)
window.mainloop()
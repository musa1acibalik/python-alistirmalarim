import customtkinter as ctk   # Modern Tkinter kütüphanesi

# =========================
# TEMA AYARLARI
# =========================
ctk.set_appearance_mode("dark")  # Koyu tema
ctk.set_default_color_theme("blue")  # Renk teması

# =========================
# HESAPLAMA MOTORU (senin kodun)
# =========================
def parcala(ifade):
    tokens = []
    sayi = ""

    for karakter in ifade:
        if karakter.isdigit():
            sayi += karakter
        else:
            tokens.append(int(sayi))
            tokens.append(karakter)
            sayi = ""

    tokens.append(int(sayi))
    return tokens


def hesapla(tokens):
    i = 0
    while i < len(tokens):
        if tokens[i] == "*":
            sonuc = tokens[i-1] * tokens[i+1]
            tokens[i-1:i+2] = [sonuc]
            i = 0

        elif tokens[i] == "/":
            sonuc = tokens[i-1] / tokens[i+1]
            tokens[i-1:i+2] = [sonuc]
            i = 0
        else:
            i += 1

    sonuc = tokens[0]
    i = 1

    while i < len(tokens):
        if tokens[i] == "+":
            sonuc += tokens[i+1]
        elif tokens[i] == "-":
            sonuc -= tokens[i+1]
        i += 2

    return sonuc


# =========================
# BUTONLARIN ÇALIŞMA FONKSİYONU
# =========================
def butona_bas(deger):
    mevcut = entry.get()  # Ekrandaki yazıyı al

    if deger == "=":  # Eğer = tuşuna basıldıysa
        try:
            tokens = parcala(mevcut)
            sonuc = hesapla(tokens)
            entry.delete(0, "end")  # Ekranı temizle
            entry.insert(0, str(sonuc))  # Sonucu yaz
        except:
            entry.delete(0, "end")
            entry.insert(0, "Hata")

    elif deger == "C":  # Temizleme tuşu
        entry.delete(0, "end")

    else:  # Normal sayı veya operatör
        entry.insert("end", deger)


# =========================
# PENCERE OLUŞTURMA
# =========================
app = ctk.CTk()
app.title("Telefon Hesap Makinesi")
app.geometry("320x450")

# =========================
# EKRAN (GÖSTERGE)
# =========================
entry = ctk.CTkEntry(
    app,
    height=60,
    font=("Arial", 28),
    justify="right"  # Yazıyı sağa yasla (telefon gibi)
)
entry.pack(fill="x", padx=10, pady=10)

# =========================
# BUTONLARIN DÜZENİ
# =========================
butonlar = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

# Butonları ekrana yerleştir
for satir in butonlar:  # Her satırı dolaş
    frame = ctk.CTkFrame(app)  # Satır için çerçeve
    frame.pack(expand=True, fill="both")

    for tus in satir:  # Satırdaki her tuş
        btn = ctk.CTkButton(
            frame,
            text=tus,
            font=("Arial", 20),
            command=lambda x=tus: butona_bas(x)  # Tıklanınca fonksiyon çalışır
        )
        btn.pack(side="left", expand=True, fill="both", padx=5, pady=5)

# =========================
# PROGRAMI BAŞLAT
# =========================
app.mainloop()

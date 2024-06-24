import tkinter as tk
from tkinter import ttk

import chrome
import ilce_mahalle_listeleri
from tasinmazAdiOlustuma import tasinmazAdi  # doğru sınıfı import ediyoruz

# Ana pencereyi oluştur
root = tk.Tk()
root.geometry("600x400")
root.title("Açılır Listeler ile Taşınmaz Adı Oluşturma Örneği")

# İlk combobox oluştur
ilceCombobox = ttk.Combobox(root, values=ilce_mahalle_listeleri.ilceler)
ilceCombobox.set("İlçe Seçin")

# İkinci combobox oluştur
mahalleCombobox = ttk.Combobox(root)
mahalleCombobox.set("Mahalle seçin")

# İlk combobox'tan seçim yapıldığında çağrılacak fonksiyon
def mahalleGuncelleme(event):
    selected_category = ilceCombobox.get()
    new_options = ilce_mahalle_listeleri.mahalleler.get(selected_category, [])
    mahalleCombobox['values'] = new_options
    mahalleCombobox.set("Mahalle Seçin")

# İlk combobox'a seçim yapıldığında tetiklenecek bir olay ekle
ilceCombobox.bind("<<ComboboxSelected>>", mahalleGuncelleme)

# Placeholder Ada No
def set_placeholder_ada(event):
    if adaNo.get() == '':
        adaNo.insert(0, 'Ada numarasını giriniz')
        adaNo.config(fg='grey')

def clear_placeholder_ada(event):
    if adaNo.get() == 'Ada numarasını giriniz':
        adaNo.delete(0, tk.END)
        adaNo.config(fg='black')

# Placeholder Parsel No
def set_placeholder_parsel(event):
    if parselNo.get() == '':
        parselNo.insert(0, 'Parsel numarasını giriniz')
        parselNo.config(fg='grey')

def clear_placeholder_parsel(event):
    if parselNo.get() == 'Parsel numarasını giriniz':
        parselNo.delete(0, tk.END)
        parselNo.config(fg='black')

# Ada ve Parsel alanı
adaNo = tk.Entry(root)
adaNo.insert(0, 'Ada numarasını giriniz')
adaNo.config(fg='grey')
adaNo.bind("<FocusIn>", clear_placeholder_ada)
adaNo.bind("<FocusOut>", set_placeholder_ada)

parselNo = tk.Entry(root)
parselNo.insert(0, 'Parsel numarasını giriniz')
parselNo.config(fg='grey')
parselNo.bind("<FocusIn>", clear_placeholder_parsel)
parselNo.bind("<FocusOut>", set_placeholder_parsel)

# Butona basıldığında taşınmaz adını oluştur ve etikete yazdır
def tasinmaz_adi_olustur():
    ilce = ilceCombobox.get()
    mahalle = mahalleCombobox.get()
    ada = adaNo.get()
    parsel = parselNo.get()

    # Sınıf örneği oluştur
    tasinmaz = tasinmazAdi(ilce, mahalle, ada, parsel)
    tasinmazEtiket.config(text=f"Oluşturulan Taşınmaz Adı: {tasinmaz.olusanTasinmazAdi}")

# Buton
button = tk.Button(root, text="Doğal Sit Durumunu Sorgula", command=lambda: chrome.parsel_sorguyu_ac(ilceCombobox.get(), mahalleCombobox.get(), adaNo.get(), parselNo.get()))

# Taşınmaz adı için etiket
tasinmazEtiket = tk.Label(root, text="")

# Bileşenleri pencereye yerleştir
ilceCombobox.pack(pady=20)
mahalleCombobox.pack(pady=20)
adaNo.pack(pady=20)
parselNo.pack(pady=5)
button.pack(pady=20)
tasinmazEtiket.pack(pady=10)

# Ana döngüyü başlat
root.mainloop()
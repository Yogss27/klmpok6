import streamlit as st
import math

st.title ("OKE Kalku")
st.subheader ("Pengertian")
st.write ("pH mengukur konsentrasi ion hidrogen dalam suatu larutan, yang menentukan apakah larutan tersebut bersifat asam, basa, atau netral. Nilai pH berada pada skala 0-14, dengan pH 7 dianggap netral, pH kurang dari 7 dianggap asam, dan pH lebih dari 7 dianggap basa.")
st.write ("molaritas adalah konsentrasi jumlah zat terlarut per satuan volume. Molaritas menunjukan berapa banyak mol zat terlarut dalam satu liter zat pelarut (mol/liter). Pada umumnya jumlah zat pelarut akan lebih besar disbanding jumlah zat terlarut.")
st.subheader ("Rumus Konsentrasi dan pH")
st.write ("Konsentrasi = Jumlah zat / Voume")
st.write ("pH = -log10 (Konsentrasi ion)")

st.subheader ("keterangan")
st.write ("0 - 7  larutan termasuk dalam asam")
st.write ("7      larutan bersifat netral")
st.write ("7 - 14 larutan termasuk dalam basa")

def calculate_ph(concentration):
    # Menghitung pH berdasarkan konsentrasi molar
    ph = -math.log10(concentration)
    return ph

def calculate_concentration(volume, amount):
    # Menghitung konsentrasi berdasarkan volume dan jumlah zat
    concentration = amount / volume
    return concentration

def main():
    st.subheader ("Kalkulator pH dan Konsentrasi")
    
    # Memasukkan volume dan jumlah zat
    volume = st.number_input("Masukkan volume (dalam liter):",min_value=0.01, format = "%.6f")
    amount = st.number_input("Masukkan jumlah zat:",min_value=0.01,format = "%.6f")
    
    # Memanggil fungsi untuk menghitung konsentrasi
    concentration = calculate_concentration(volume, amount)
    st.success(f"Konsentrasi: {concentration:.2f} M")
    
    # Memanggil fungsi untuk menghitung pH
    ph = calculate_ph(concentration)
    st.success(f"pH: {ph:.2f}")
    
    if ph<7:
        st.write ("larutan termasuk dalam asam")
    elif ph>7:
        st.write ("larutan termasuk dalam basa")
    else:
        st.write ("larutan bersifat netral")

if __name__ == "__main__":
    main()

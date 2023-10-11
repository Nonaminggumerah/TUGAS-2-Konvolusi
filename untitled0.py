# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 11:27:02 2023

@author: nadya
"""

print ("Naive implementation of convolution")
print ("Nadya Putri Arisni")
print ("NRP = 5009211079")

def convolution(signal1, signal2):
    len1 = len(signal1)
    len2 = len(signal2)

# Konvolusi adalah fungsi yang mengambil dua sinyal 1D disini ada signal 1 dan signal 2

    # Panjang sinyal keluaran
    len_out = len1 + len2 - 1

    # Inisialisasi sinyal keluaran
    result = [0] * len_out

#len adalah panjang sinyal dari kata "length"
#len out adalah panjang sinyal keluaran yang merupakan pengurangan panjang kedua sinyal dikurangi 1

    # Konvolusi
    for i in range(len1):
        for j in range(len2):
            result[i + j] += signal1[i] * signal2[j]
            
#dilakukan loop melalui dua sinyal untuk menghitung konvolusi
#di dalam i dan j ada setiap elemen dalam kedua sinyal dan elemen2 tersebut dikalikan
#hasilnya ditambahkan ke posisi yang benar dalam sinyal keluaran

    return result

#result akan menginisialisasi panjang len_out dan diisi dengan nol

# Contoh penggunaan
signal1 = [1, 2, 3]
signal2 = [0.5, 1, 0.5]

convolution_result = convolution(signal1, signal2)
print("Hasil konvolusi:", convolution_result)

# Validasi hasil dengan NumPy Convolve
import numpy as np
 
numpy_convolution_result = np.convolve(signal1, signal2, mode='full')
print("Hasil konvolusi NumPy:", numpy_convolution_result.tolist())

# Memeriksa apakah hasil konvolusi sesuai
if convolution_result == numpy_convolution_result.tolist():
    print("Hasil konvolusi sesuai dengan NumPy Convolve.")
else:
    print("Hasil konvolusi tidak sesuai dengan NumPy Convolve.")

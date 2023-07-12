# UAS_Pengolahan_Citra

Dosen Pengampu   : Muhammad Najamuddin Dwi Miharja, S.Kom, M.Kom
Mata Kuliah      : Pengolahan Citra
Nama             : Nurul Fajri
Nim              : 312110506
Kelas            : TI.21.C.1

## Berikut adalah penjelasan langkah langkah mengenai komponen utama dalam program
- Pertama, kita mengimpor beberapa library yang akan digunakan dalam program ini, yaitu cv2 (OpenCV) untuk operasi pemrosesan gambar, numpy untuk manipulasi array, math untuk perhitungan matematis, dan matplotlib.pyplot untuk menampilkan gambar. <br>
Kemudian, kita mengimport beberapa modul dari library tkinter, yaitu Tk untuk membuat jendela aplikasi, Button untuk membuat tombol, dan askopenfilename dari filedialog untuk membuka dialog file. <br>
- Setelah itu, kita mendefinisikan fungsi median_filter, mse, dan psnr untuk melakukan pemrosesan gambar dan menghitung metrik MSE dan PSNR. <br>
Fungsi select_and_process_image akan dipanggil saat tombol "Select Gambar" diklik. Fungsi ini akan membuka dialog file untuk memilih gambar, kemudian memuat gambar tersebut, menerapkan filter median, dan menghitung MSE dan PSNR. Selanjutnya, gambar asli dan hasil prosesnya akan ditampilkan dalam jendela menggunakan matplotlib.
- Pada bagian utama program, kita membuat jendela tkinter dengan menggunakan objek Tk. <br>
- Kita memberikan judul "Image Processing" untuk jendela tersebut menggunakan method title. <br>
- Kita menggunakan method geometry untuk mengatur ukuran jendela dengan argumen "800x400" yang mengindikasikan lebar 800 piksel dan tinggi 400 piksel. <br>
- Kemudian, kita membuat tombol "Select Gambar" menggunakan objek Button dengan teks "Select Gambar" dan command yang menunjuk ke fungsi select_and_process_image. <br>
- Tombol tersebut ditempatkan dalam jendela menggunakan method pack. <br>
- Terakhir, program memulai event loop tkinter dengan method mainloop, yang akan menjalankan jendela dan menangani interaksi pengguna. <br>

## Berikut adalah hasilnya
Ini setelah di run
![Screenshot (386)](https://github.com/NFajri11/UAS_Pengolahan_Citra/assets/92937310/03a99f77-8c59-45b1-b39a-7f42398462ba)
Pilih gambar yang akan di proses
![Screenshot (384)](https://github.com/NFajri11/UAS_Pengolahan_Citra/assets/92937310/115df9fc-6220-46b5-903b-a8513742a9c0)
Hasil nya <br>
Pada pojok kiri bawah ada fitur untuk mendownload gambar yang sudah di proses<br>
![Screenshot (385)](https://github.com/NFajri11/UAS_Pengolahan_Citra/assets/92937310/115a4b29-a9a1-4a7b-804e-0bd3f8590b0b)



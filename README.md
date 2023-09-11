1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- Yang pertama saya lakukan adalah membaut repository baru di github dan folder baru untuk local saya dan menyambungkannya satu dengan yang lain. 
- langkan kedua saya adalah menambahkan requirements.txt yang telah ditentukan sebelumnya
- setelah itu saya install django dan membuat projek bernama inventory, dan konfigurasi sehingga server bisa jalan
- setelah itu saya test terlebih dahulu apakah server sudah bisa jalan atau belum
- jika sudah, saya selanjutnya menambah berkas .gitignore
- selanjutnya, saya membuat projek lagi bernama main, dan masukannya di aplikasi yang ada di settings.py
- setelah itu, saya membuat html file bernama main di folder baru bernama templates
- setelah itu saya bikin back-end di models.py untuk handle data yang akan ditampilkan
- setelah itu, saya migrasikan agar kelihatan perubahannya
- setelah itu, saya membuat test case agar mengetahui error-error yang ditest

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, 
models.py, dan berkas html.
![IMG_20230911_231729](https://github.com/Not0nline/Tugas_PBP/assets/80256853/5645122c-4a10-4650-b98a-0cf87cfb7006)


3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Iya, django bisa jalan dengan tidak adanya virtual envorinment, tapi sebaiknya kita menggunakan virtual environment karena beberapa alesan :
- agar setiap projek mempunyai lingkungan yang terisolasi satu dari yang lain dengan versi python berbeda-beda
- agar lebih mudah menginstal dan managemen dependensi (requirements.txt) untuk replikasi yang konsisten
- bisa menghapus suatu virtual environment tanpa mengefek projek lain
- agar versi software konsisten jika kerja dalam tim
- agar mencegah masalah keamanan dengan auto update python


4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

- Model-View-Controller (MVC):
    Definisi: Sebuah arsitektur perangkat lunak yang memisahkan komponen Model (manajemen data), View (tampilan pengguna), dan Controller (logika aplikasi).
    Perbedaan Utama: Model, View, dan Controller terpisah dan berkomunikasi melalui hubungan yang jelas.

- Model-View-Template (MVT):
    Definisi: Digunakan oleh framework web Django, dengan Model (manajemen data), View (tampilan), dan Template (logika tampilan terpisah).
    Perbedaan Utama: Template memisahkan logika tampilan dari kode Python dalam Django, sedangkan View mirip dengan MVC.

- Model-View-ViewModel (MVVM):
    Definisi: Arsitektur perangkat lunak yang memisahkan Model (data), View (tampilan), dan ViewModel (perantara antara Model dan View).
    Perbedaan Utama: MVVM menekankan penggunaan ViewModel sebagai perantara untuk mengikuti perubahan dalam Model tanpa berkomunikasi langsung dengan Model.

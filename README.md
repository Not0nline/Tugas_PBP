I. Tugas 2
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


II. Tugas 3
1. Apa perbedaan antara form POST dan form GET dalam Django?
- POST bersifat aman dan dapat digunakan untuk digunakan untuk mengirim data rahasia, seperti kata sandi, yang tidak tampil di URL
- GET bersifat sederhana dan dapat digunakan untuk mengambil data dari URL, cocok untuk pencarian dan tautan berbagi

2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
- XML adalah format struktur data yang fleksibel dan digunakan untuk penukaran data
- JSON adalah format data sederhana yang mudah dibaca oleh manusia dan digunakan untuk API
- HTML adalah bahasa markup untuk tampilan web yang digunakan untuk menampilkan web

3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
- JSON mudah dibaca oleh manusia, bersifat ringan dan mudah diproses oleh komputer
- Formatnya mendukung struktur data yang fleksibel, cocok untuk RESTful API, dan kompatibel dengan banyak bahasa pemrograman
- membuatnya komunikasi antara klien dan server dalam aplikasi web lebih mudah

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- membuat base.html
- membuat create_page.html sebagai page baru yang diakses jika button pada main.html diclick
- masukan button create_product yang akan membuka create_product.html pada main.html
- buatlah fungsi baru untuk view menggunakan XML, JSON, XML by ID, JSON by ID dalam views.py
- import dan masukan fungsi XML, JSON, XML by ID, JSON by ID pada urlpatterns yang ada di urls.py
- menambah django-environment pada requirements.txt
- membuat berkas baru (Procfile, pbp-deploy.yml, .dockerignore, Dockerfile)
- import environ dan os serta fungsi-fungsi mereka pada settings.py untuk dapat menggunakan environ pada web ini
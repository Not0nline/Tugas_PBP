I. Tugas 2
=======  
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
    Perbedaan Utama: MVVM menekankan penggunaan ViewModel sebagai perantara untuk mengikuti perubahan dalam Model tanpa berkomunikasi langsung dengan Model.4
    
II. Tugas 3
=======  
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
![image](https://github.com/Not0nline/Tugas_PBP/assets/80256853/ad5d7569-c62e-42ff-bbec-98d6b8fb42bc)
![image](https://github.com/Not0nline/Tugas_PBP/assets/80256853/1dfc7deb-1a9b-4764-8b91-f37265a6971f)
![image](https://github.com/Not0nline/Tugas_PBP/assets/80256853/2c5e6928-0cbe-4a04-b59d-dfa610b39f25)
![image](https://github.com/Not0nline/Tugas_PBP/assets/80256853/9511f422-282c-4d45-a776-cb4e68a76db6)
![image](https://github.com/Not0nline/Tugas_PBP/assets/80256853/a4142b61-4fd8-47f7-8336-3cdb5d8bea66)    



III. Tugas 4
=======   
1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
Django UserCreationForm adalah formulir bawaan yang disediakan oleh Django yang mengumpulkan data yang diperlukan saat mendaftarkan pengguna baru, seperti username, password, dan email agar pembuatan pengguna dalam aplikasi lebih gampang

a. Kelebihan:
- Mudah Digunakan
  Library Django sudah dibuat dan hanya perlu digunakan tanpa perlu menulis kode, sehingga gampang untuk digunakan

- Keamanan Terintegrasi
  Sudah mempunyai fitur keamanan bawaan seperti hash password dan otentikasi password dan user, sehingga mengurangi kemungkinan kena hack

b. Kekurangan:
- Sistemnya kaku
  Jika ingin melakukan kustomisasi seperti ingin memasukan informasi tambahan, keamanan tambahan, mengubah tampilan secara UI/UX, akan susah karena merupakan kerangka yang monolitik dan mendorong kita untuk menggunakan pola tertentu sudah 

2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?

- Autentikasi adalah proses verifikasi identitas pengguna, sehingga kita dapat memastikan bahwa pengguna adalah orang yang mempunyai akun. Autentikasi melibatkan pengguna memberi beberapa kredensial seperti nama akun dan kata santi untuk akun tersebut

- Otorisasi menentukan apa yang dapat dilakukan oleh pengguna yang sudah terautentikasi. Otorisasi melibatkan penentuan hak akses atau perizinan pengguna.

- Autentikasi dan Otorisasi penting dalam menjaga keamanan aplikasi web. Autentikasi membantu dalam mencegah akses yang tidak sah untuk masuk dengan akun orang lain dengan memastikan bahwa hanya pengguna yang memiliki kredensial yang valid yang dapat masuk. Setelah pengguna masuk, otorisasi digunakan untuk mengendalikan hal yang dapat lakukan pengguna berdasarkan perizinan yang telah ditentukan. Kedua hal ini bantu mencegah penyalahgunaan aplikasi dengan cara membatasi hal yang dapat dilakukan oleh setiap pengguna.

3.  Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
- Cookies adalah kumpulan informasi yang berisi rekam jejak dan aktivitas pengguna ketika mengunjkungi sebuah website, dan cookies dapat membuat menelusuri laman-laman di sebuah website menjadi lebih mudah.

- cara Django mengelola cookies :
i. Django akan menyimpan data sesi seorang pengguna berdasarkan username atau credential lainnya dalam bentuk cookie yang akan dibuat pada server sebelum dikirim ke perangkat pengguna sehingga dapat di-track device mana yang digunakan pengguna aplikasi
ii. Selanjutnya pengguna tersebut dapat mengakses data orang yang login jika sudah terdaftar dalam data sistem
iii. setelah user selesai menggunakan aplikasi (atau jika pengguna tidak aktif dalam jangka waktu yang panjangnya dapat diatur oleh programmer), django akan menghapus cookies pengguna sehingga perlu masuk lagi jika ingin mengakses data yang sebelumnya diakses

4.  Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
i.  Secara deafult, penggunaan cookies tidak terlalu aman. Walaupun cookies adalah cara penyimpanan data yang aman, seberapa aman cookies tersebut tergantung dengan konfigurasi yang dilakukan aplikasi yang dibuat. 

ii. Resiko yang harus diwaspadai :
- Cookies secara default tidak dienkripsi sehingga jika terdapat data yang disimpan dalam cookies yang tidak dienkripsi oleh server, seluruh data pengguna dapat dicuri dan dibaca oleh orang lain
- Jika aplikasi tersebut support beberapa platform, cookies dapat dicuri jika keamanan tidak ketat akibat penyisipkan kode skrip ke halaman web oleh pengguna
- hal yang terjadi belakangan ini juga dapat terjadi yaitu session highjacking yaitu dimana seseorang mencuri cookie seseorang dalam aplikasi sehingga tidak perlu masuk aplikasi menggunakan email, username, ataupun password

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- membaut form registrasi dengan menggunaan UserCreationForm yang disediakan oleh django dan redirect ke halaman html untuk register (di aplikasi bernama register.html) dalam fungsi yang gunanya adalah save data orang yang baru register pada data sistem yang ditulis pada views.py.
- membuat halaman html untuk registrasi (register.html) untuk redirect tersebut jika pengguna ingin membuat akun baru
- menghubungkan register tersebut pada urls.py agar ada dalam sistem
- pada views.py membuat fungsi login dan menggunakan django untuk autheticate agar pengguna dapat login jika dan hanya jika pengguna user tersebut telah membuat akun dan password pengguna tersebut benar, jika sudah benar maka pengguna dapat masuk ke halaman utama aplikasi
- membuat halaman login.html halaman pertama yang dilihat user ketika masuk ke website dan hanya bisa ke halaman utama       (main.html) ketika sudah benar informasi login
- masukan cookies sebagai salah satu variabel yang ada pada context
- menghubungkan login papda urls.py
- membuat fungsi logout pada views.py sehingga cookies dapat dihapus ketika user telah logout
- membuat button logout pada main.html sehingga dapat melakukan fungsi logout ketika sudah selesai 
- hubungkan logout pada urls.py
- membuat setiap barang pada inventory terhubung dengan setiap user sehingga hanya menampilkan inventory yang ada pada suatu orang tersebut

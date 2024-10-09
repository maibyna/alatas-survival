Nama     : Maibyna Khairanisya
NPM      : 2306165723

README TUGAS 6
Menjawab Pertanyaan:
1. Manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web:

JavaScript sangat penting dalam pengembangan aplikasi web modern karena memiliki banyak manfaat:
>>Interaktivitas: JavaScript memungkinkan pengembang untuk membuat halaman web yang interaktif, seperti memperbarui konten tanpa harus memuat ulang seluruh halaman. Hal ini akan sangat membantu meningkatkan pengalaman pengguna.
>>Kecepatan: Karena JavaScript dijalankan di sisi klien (browser), banyak tugas dapat dilakukan lebih cepat tanpa menunggu server merespons, seperti validasi form atau animasi.
>>Asynchronous programming: JavaScript mendukung pengembangan aplikasi dengan asinkronisasi, misalnya menggunakan fetch() untuk mengambil data dari server tanpa mengganggu halaman utama.
>>Cross-browser compatibility: JavaScript berjalan di hampir semua browser modern, sehingga aplikasi web bisa diakses dari berbagai perangkat.
Komunitas yang besar: Banyak pustaka dan framework yang tersedia, seperti React, Vue, dan Angular, yang memudahkan pengembang membuat aplikasi web skala besar dengan fitur canggih.


2. Fungsi dari penggunaan await ketika menggunakan fetch():
>>await digunakan dalam JavaScript untuk menghentikan eksekusi program sementara hingga suatu Promise selesai. Saat kita menggunakan fetch() untuk mengambil data dari server, operasi ini mengembalikan Promise yang belum diselesaikan (pending), karena permintaan HTTP membutuhkan waktu. Dengan await, kita memastikan bahwa kode menunggu hingga respons diterima sebelum melanjutkan ke perintah berikutnya.

Contoh: let response = await fetch(url);

Jika kita tidak menggunakan await, kode akan terus berjalan meskipun permintaan belum selesai, yang bisa menyebabkan masalah karena kode di bawahnya mungkin membutuhkan hasil dari fetch(). Tanpa await, kita harus menggunakan .then() untuk menangani hasil secara manual, yang bisa lebih sulit dipahami.


3. Mengapa kita perlu menggunakan csrf_exempt pada view yang akan digunakan untuk AJAX POST?

>>csrf_exempt digunakan untuk menonaktifkan perlindungan Cross-Site Request Forgery (CSRF) pada view tertentu. CSRF adalah serangan di mana pengguna yang sudah login disuruh mengirimkan request yang tidak sah dari situs lain, dan Django melindungi dari serangan ini dengan token CSRF.
Namun, ketika kita menggunakan AJAX POST, seringkali lebih sulit untuk menyertakan token CSRF secara manual dalam permintaan, terutama jika request tidak diawali oleh formulir yang dihasilkan Django. Oleh karena itu, kita menggunakan csrf_exempt untuk menonaktifkan pemeriksaan CSRF di view tersebut.


4. Mengapa pembersihan data input pengguna dilakukan di backend juga, bukan hanya di frontend?

Melakukan validasi hanya di frontend tidak cukup aman karena:
>>Front-end bisa dimanipulasi: Pengguna bisa mengubah atau memodifikasi kode JavaScript di browser mereka, sehingga bisa melewati validasi yang ada di frontend.
>>Keamanan data: Validasi di backend memastikan data yang masuk aman dan sesuai dengan yang diharapkan, melindungi aplikasi dari serangan injeksi atau input yang tidak valid.
>>Consistency: Backend harus bertanggung jawab memastikan semua data yang diterima dalam format yang benar, terlepas dari apakah input sudah divalidasi di frontend.

Oleh karena itu, validasi di backend wajib dilakukan untuk menjamin keamanan dan integritas aplikasi.


5. Implementasi step-by-step checklist di atas secara detail:
Garis Besar Implementasi Fitur Mood dengan AJAX

  1.) Mengambil data "Survival Entry atau product" dengan AJAX GET. Ini terlihat dari pembuatan function dalam views yang mengakses data product, dan mengembalikannya dalam JSON.
>>Buat Endpoint:
Siapkan route di backend untuk mengambil data mood pengguna yang sedang login.
Buat fungsi di backend yang akan mengembalikan data mood dalam format JSON.

>>AJAX GET:
Di frontend, gunakan AJAX untuk melakukan permintaan ke endpoint yang sudah dibuat saat halaman dimuat.
Tampilkan data mood yang diterima ke dalam tampilan kartu di halaman utama.


  2.) Menambahkan Mood Baru dengan AJAX POST
Buat Tombol dan Modal:
Buat tombol di halaman utama untuk membuka modal yang berisi form untuk menambahkan "Survival Entry". Ini sama persis dengan form yang tanpa ajax, yaitu di create_mood_entry.html

Form di Modal:
Dalam modal, buat form dengan input untuk menuliskan product isi tadi dan tombol untuk mengirimkan data.

AJAX POST:
Saat form disubmit, gunakan AJAX untuk mengirimkan data ke endpoint yang dituju  path('create-survival-entry-ajax', add_survival_entry_ajax, name='add_survival_entry_ajax').
Pastikan data dikirim dengan format yang tepat dan sertakan token CSRF untuk keamanan.

Tanggapan dari Server:
Jika penambahan berhasil, tutup modal dan bersihkan form dari input yang ada.
Panggil kembali fungsi untuk mengambil data survival entry terbaru dan memperbarui tampilan tanpa memuat ulang halaman.
Jika terjadi kesalahan saat penambahan, tampilkan pesan error kepada pengguna. <namun tidak tahu kenapa pesan errornya tidak muncul-muncul>

  3.) Mengelola Data di Backend
Fungsi untuk Menambahkan Product/Survival Entry.
Buat fungsi di backend untuk menangani permintaan POST dan menyimpan data baru ke dalam basis data.
Validasi:
Pastikan data masukan "survival entry" yang diterima valid dan milik pengguna yang sedang login. 

==============================================================================================================================================================================================

README TUGAS 5
A. Menjawab Pertanyaan Tugas:
1) Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

CSS selector, merupakan bagian dari bahasa CSS yang digunakan untuk menunjuk atau memilih elemen HTML tertentu yang ingin diubah gaya tampilannya. 
Dan ketika terdapat beberapa CSS selector yang menargetkan elemen HTML yang sama, browser akan mengikuti aturan prioritas tertentu untuk menentukan gaya mana yang akan diterapkan. Aturan ini dikenal sebagai CSS Cascade.

Faktor-Faktor yang Mempengaruhi Prioritas
>>dari yang terendah menuju yang tertinggi
a. Selector Universal (*): Memilih semua elemen.
b. Selector Tag (misalnya div, p, h1): Memilih elemen berdasarkan nama tag.
c. Selector Kelas (.classname): Memilih elemen dengan kelas tertentu.
d. Selector ID (#idname): Memilih elemen berdasarkan ID.
e. Inline Styles: Gaya yang diterapkan langsung pada elemen menggunakan atribut style.
f. !important: Meskipun bukan bentuk spesifisitas, aturan ini memiliki prioritas tertinggi, dan akan mengoverride semua yang lainnya jika ada.

Atau dapat juga dinyatakan dengan:
Spesifisitas: ID Selector>>Class Selector>>Combinator
Kepentingan: Inline styles, important declaration
Urutan Penulisan:-

2) Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design
>>Responsive design adalah pendekatan dalam pengembangan web untuk membuat halaman web terlihat baik di berbagai ukuran layar dan perangkat. Design yang resposive membawa berbagai keuntungan, yaitu: 

Pengalaman Pengguna: Lebih mudah bagi pengguna untuk menggunakan (userfriendly) serta memastikan pengguna mendapatkan pengalaman yang baik, terlepas dari perangkat yang digunakan.
SEO: Mesin pencari lebih menyukai situs yang responsif. Hal ini membawa peluang bagi sistem menjadi rekomendasi urutan top dalam pelayanan pengguna internet.
Ketersediaan: Meningkatkan aksesibilitas untuk semua pengguna.

Contoh Aplikasi yang Sudah Menerapkan Responsive Design:
Google: Halaman pencariannya dapat beradaptasi dengan ukuran layar.
Twitter: Aplikasi webnya mengubah tampilan berdasarkan perangkat yang digunakan. 
YouTube: Platform berbagi video ini juga memiliki desain yang sangat responsif. Video akan secara otomatis menyesuaikan ukurannya agar sesuai dengan layar perangkat, dan pengguna dapat dengan mudah mengontrol pemutaran video.


3) Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Margin: Ruang di luar elemen. Margin dapat digunakan untuk menciptakan jarak antar elemen. Ini berguna untuk memberikan jarak yang rapi dalam web yang kita gunakan.
>>Contoh:
.box {
  margin: 20px;
}

Border: Garis yang mengelilingi elemen. Border dapat disesuaikan dengan lebar, jenis garis, dan warna.
>>Contoh:
.box {
  border: 2px solid black;
}

Padding: Ruang di dalam elemen, antara konten dan batas elemen. Padding menciptakan ruang di dalam elemen itu sendiri.
>>Contoh
.box {
  padding: 10px;
}

Ilustrasi Perbedaan:

Margin: Jarak antara elemen.
Border: Bingkai yang mengelilingi elemen.
Padding: Jarak antara konten elemen dan bingkainya.


4)  Jelaskan konsep flex box dan grid layout beserta kegunaannya!
>>Flexbox: Model layout termasuk model yang cocok untuk layout satu dimensi (baris atau kolom) yang memungkinkan elemen didistribusikan dengan lebih efisien di dalam kontainer.
Kegunaan: Membuat layout responsif, membuat elemen mudah diatur dalam baris atau kolom, dan menyelaraskan dan mendistribusikan ruang.

>>Grid Layout: Model layout dua dimensi memungkinkan pembuatan grid kompleks. Ini memudahkan penataan elemen secara bersamaan dalam baris dan kolom, dengan ekspansi baris yang bisa dikustomisasi.
Kegunaan: Sangat cocok untuk layout yang lebih kompleks, seperti dashboard dengan elemen yang diatur secara bebas dalam grid.

5)  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!


B. Penjelasan Tutorial Pengerjaan
1. Laman Registrasi
![image](https://github.com/user-attachments/assets/2eb0be01-0692-4b51-8f7b-3326412dcb35)
Salah satu implementasi yang saya terapkan adalah membuat laman register, sebagaimana proses menerima informasi/data user, sebelum menjadi terdaftar dalam sistem dan diarahkan ke bagian login kembali. Dengan tema Alatas Survival ini, saya memilih warna putih gading dan biru tua.
Selain itu, saya juga menambahkan picture 'darkvibes' sebagai background centernya. Background ini sama dengan proses main, juga register berikut.

Bagian register ini otomatis menawarkan untuk kembali ke show-bagian login.

3. Proses Login
![image](https://github.com/user-attachments/assets/36300865-35e6-442b-9560-f6a15fbe94a7)


4. Homepage ketika user masuk ke dalam proses
![image](https://github.com/user-attachments/assets/c3798259-604f-4a9c-9c05-a2a40a93d72e)
Dalam tampilan ini, data user berupa username dan kelas akan ditampilkan. Ada dua layar sekaligus yang ditampilkan yaitu bagian awal, berupa data product masuk yang disajikan dalam list, serta card di bagian bawah untuk memberi viusalisasi yang lebih baik. Dalam laman ini juga telah include sistem navigasi bar paling atas, yang menampilkan Aplikasi main, welcoming user serta logout. Dalam adaptasinya telah ditampilkan sebagai responsive terhadap mobile dan juga dekstop.

![image](https://github.com/user-attachments/assets/23d411e0-ec30-4a32-8a7b-4c1fb154278c)

5. Bagian untuk menambahkan Product
![image](https://github.com/user-attachments/assets/9cda6285-761b-4d25-9861-7ea3fba06ff2)
Sebelum product ditampilkan, tentu harus ada data yang masuk. Nah bagian ini yang menerima untuk memasukkan nama product, price serta description

6. Bagian Edit
![image](https://github.com/user-attachments/assets/41042ae8-1d64-4e98-9637-19ea08e8e82f)
Ini ditujukan untuk mengedit product yang telah masuk. Namun edit ini hampir mirip dengan menambahkan, karena semua unit sifatnya diisi ulang, namun boleh dibatalkan.

7. Sesi Bagian Bawah yang menampilkan card
![image](https://github.com/user-attachments/assets/143fbcd6-29c2-452f-a9dd-3a0f09c26281)
Jika memungkinkan, nantinya user akan diusahakan bisa mengedit foto productnya sendiri. Karena masih dalam perkembangan, dan mengangkat tema magical, maka sementara menyajikan card default, yang bisa diubah  hanya key umumnya seperti nama, price, dan description.



==============================================================================================================================================================================================

README TUGAS 4
 1. Apa perbedaan antara HttpResponseRedirect() dan redirect()
Keduanya sama-sama library langsung Django yang di-import, namun perbedaannya terdapat pada hierarki penggunaan. HttpResponseRedirect() secara penggunaan, mewajibkan developer untuk menyebutkan secara eksplisit link/url/atau tautan yang ingin disambungkan. Dalam program saya biasa digunakan untuk ke situs peramban html yang saya buat.

Sedangkan pada redirect() ini dapat berupa string, suatu arah yang masih di dalam program dan kelas/aplikasi. Contoh sederhana yang paling sering digunakan dalam program saya adalah “main: show_menu”

2. Jelaskan cara kerja penghubungan model Product dengan User!
Dalam aplikasi alatas-survival ini, user dihubungkan dengan dua kelas yaitu kelas SurvivalEntry dan kelas Purchase. Kedua fungsi ini memiliki tujuan yang hampir sama, namun saling melengkapi. Dalam SurvivalEntry ini, terdapat pengelolaan dari bagaimana saya membuat product-product (dalam bentuk objek, yang masing-masing dibawa oleh identitas ID, nama produk, harga, dan deskripsi. User, yang diambil dari ForeignKey ini, berfungsi untuk membantu pengarahan program product ini juga bisa menjadi objek yang terhubung dengan User.

Sedangkan dalam Purchase, orientasinya lebih untuk menyajikan history, dan membantu pada proses penyajian opsi ketika user akan memilih barang.

3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
Authentication didapat dari jawaban “siapakah yang login”, ini dimaksudkan memverifikasi identitas pengguna. Termasuk tentang ID/perihal kredensial yang melekat pada pengguna tersebut. Namun dalam case authorization, adalah untuk menjawab pertanyaan “apa kebebasan yang diberikan kepada pihak-pihak tersebut”. 

Di dalam aplikasi alatas-survival, bentuk authentication itu terletak pada awal login, saat pengguna diminta untuk memasukkan username dan password. Sedangkan untuk authorization, itu terletak di bagian setiap pengguna yang hanya mampu mengakses historynya masing-masing.

4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Session di server menyimpan informasi siapa pengguna yang masuk, sedangkan Cookie di browser menyimpan session ID, yang server gunakan untuk mengidentifikasi pengguna. Django menggunakan kombinasi session dan cookies untuk mengingat pengguna yang sudah login.

Untuk cookies tentu memiliki tantangan tersendiri karena berpotensi di salah gunakan oleh pihak lain untuk menyerang menggunakan cookie yang teridentifikasi tersebut. 

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Pertama, saya terlebih dahulu membuat produk lebih lanjut terkait barang yang ada di e-commerse saya. Lalu, saya menghadapi error saat data tersebut harus saya simpan dalam bentuk object, bukan sekadar list. Lalu, saya memadu padankan, bagaimana sebaiknya saya hanya menampilkan barang yang saya miliki (dengan objek tadi saya sajikan dalam tabel) lalu user hanya perlu memilih menggunakan selection form, tentang barang yang di-purchase, beserta kuantitasnya. Untuk harga dan deskripsi, itu langsung tertera di tabel informasi. Setelah memastikan objek bisa diakses (barang dalam e-commerse) barulah saya memproses pembuatan kedua pengguna dummy, sebagai uji coba.

Dalam kasus ini, karena pada pemprosesan mempersiapkan history purchase pengguna, ternyata saya telah mengimplementasikan ForeignKey, dan dapat berlanjut langsung ke tahap terakhir sebelum push github.


==============================================================================================================================================================================================

README TUGAS 3
1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
   Data delivery dalam eksistensinya sendiri, itu ditujukan untuk membantu proses pengiriman data dari satu sistem, aplikasi, atau perangkat ke sistem lainnya melalui jaringan. Secara tidak langsung, data delivery (dengan berbagai format yang ada) itu menjadi kebutuhan penting dalam penyampaian informasi. Jika dikaitkan dengan pengimplementasian data delivery dalam sebuah platform, data delivery akan sangat membantu menghubungkan antar server/jaringan/client terkait, dan dibantu koneksi berbagai format, delivery ini memberikan kemampuan interoperabilitas. Di sisi lain, karena terkait jaringan, data delivery membantu informasi didistribusikan secara real-time dan kompatibel di aplikasi mobile maupun pihak ketiga.
    
2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
   Bersumber dari AWS, kedua format tersebut baik dikategorinya masing-masing. Setelah merangkum informasi terkait kedua format tersebut, saya mengambil kesimpulan bahwa JSON lebih populer dan dikenal lebih baik karena keberadaannya yang lebih baru dan sederhana. JSON menawarkan keamanan yang lebih baik dibanding XML, dan didukung dengan ukuran file yang lebih kecil dan transmisi data yang lebih cepat. Penampilan sintaksis dari JSON yang lebih padat, dan on-point membuat JSON lebih mudah dipahami dan dianggap lebih mudah. Sehingga, keberadaan JSON ini cocok untuk penggunaan API, aplikasi seluler, dan penyimpanan data.
   Di sisi lain, XML juga memiliki keunggulan dalam struktur terperinci yang mendukung penyimpanan kompleks dalam mesin. XML akan sangat cocok bagi pengembang yang ingin menyimpan beberapa tipe data yang berbeda dengan banyak variabel,. XML memeriksa kesalahan dalam data kompleks secara lebih efisien daripada JSON karena XML berfokus pada penyimpanan data dengan cara yang mudah untuk dapat dibaca mesin. Secara tipe data, XML juga mendukung tipe data yang lebih kompleks, hingga mampu mendukung data biner dan stempel waktu. Sehingga secara keseluruhan, hal ini bergantung pada penggunaan praktek. Dari saya sendiri seperti merasa lebih mudah membaca format JSON.
   
3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
   is_valid() pada form Django digunakan untuk memvalidasi data yang diinputkan ke dalam form. Fungsi ini memeriksa apakah semua data sesuai dengan aturan validasi yang ditetapkan di form, seperti tipe data, panjang teks, dan format email. Jika data valid, maka is_valid() akan mengembalikan nilai True, dan form dapat diproses lebih lanjut.
  Kita membutuhkan is_valid() untuk memastikan bahwa data yang dimasukkan pengguna benar dan aman sebelum disimpan ke database atau diproses lebih lanjut. Ini juga mencegah input yang salah atau berbahaya (seperti injection) agar tidak merusak aplikasi. Ini merupakan bentuk kesadaran di tengah teknologi yang berkembang, dengan intensi berbahaya pengguna internet. Dengan menyaring input pengguna sedari awal, kita membantu menangani kasus di dalam program beserta output program, sesuai, dengan ekspektasi awal keberadaan program.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
   csrf_token digunakan untuk melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF). CSRF terjadi ketika seorang penyerang memanfaatkan sesi aktif pengguna dengan mengirimkan permintaan yang tidak sah ke server (misalnya, transaksi tanpa sepengetahuan pengguna). Jika form tidak dilengkapi dengan csrf_token, seorang penyerang dapat membuat form palsu yang di-submit atas nama pengguna yang sudah login ke aplikasi, tanpa sepengetahuan mereka. Hal ini bisa dimanfaatkan untuk melakukan tindakan berbahaya, seperti memodifikasi data atau melakukan transaksi yang tidak diinginkan.
   
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
   Checklist untuk tugas ini adalah sebagai berikut.
>>Membuat input form untuk menambahkan objek model pada app sebelumnya.
---> Setelah kemarin membangun dasar proyek, saya ingin membuat dekorasi atau bentuk (form) utuh dari aplikasi alatas-survival milik saya. Maka dari itu ada forms.py, yang mengakses atribute (yang sebelumnya telah saya buat dalam model.py). Lalu di dalam views, saya buat suatu fungsi untuk memvalidasi input (ekspektasi) serta menambahkan beberapa input. Baru menerapkan beberapa pembangunan html dan penyesuaian agar nantinya mulai terdapat kolom input untuk menerima masukkan, dll.
>>Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
--->Pada bagian ini, saya menyesuaikan serta menghubungkan form/views berisi atribute dan bentuk field- tampilannya, di dalam satu html create_survival_entry.html, sebelum bagan ini dihubungkan juga ke fungsi format XML, JSON, XML by ID, dan JSON by ID. Dari penambahan fungsi ini, saya tidak hanya menampilkan dan menyediakan kolom input dalam html format, tapi juga dapat mengelola informasi dalam XML, JSON, XML by ID, dan JSON by ID.
>> Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
--->Saya mengimplemetasikan ini dengan cara menbangun path dari URL untk mengakses ke runserver dll. Ketika di akhir, setelah ada input yang masuk pun, itu dikelola, direkam dalam jejak JSON/XML, sebelum dari POSTMAN kits ajukan perminta untuk melihat history masukan input.
>>Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
>>![image](https://github.com/user-attachments/assets/fcb86f54-030b-4afd-8c92-e7a8b99e2cbd)
>>![image](https://github.com/user-attachments/assets/9c52aacb-a04b-4622-8c79-db1dac54faf9)
>>![image](https://github.com/user-attachments/assets/8f2db3f8-2092-4680-9520-c27b3337a2ad)

==============================================================================================================================================================================================

README TUGAS 2
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
 >Membuat sebuah proyek Django baru.
 ->Dalam tahap ini, dalam internal penyimpanan membuat direktori Django untuk e-commerse
 >Membuat aplikasi dengan nama main pada proyek tersebut.
 ->Setelah proyek dibuat, mulai mengaktifkan (env) dan membuat aplikasi main. Main ini meliputi pembuatan template, templates ini merupakam alur html.
 ->Selanjutnya perlu mengadaptasikan model dengan migrasi dari proses
 >Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
 ->Ini dilakukan dengan menghubungkan antara urls yang ada di main, dan urls yang ada di direktori besar alatas-survival
 >Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut.
name
price
description
 >Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
 >Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
=> Link menuju bagan
https://www.canva.com/design/DAGQRwUZLK8/-XVRJPy2eF4oP4DcGNvCNQ/edit?utm_content=DAGQRwUZLK8&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton


3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
>Version Control: Git memungkinkan user/pengakses untuk melacak progress dari setiap perubahan kode, termasuk revisi, commit, dan perubahan file.
Hal ini tentunya akan berguna untuk melihat riwayat bug dan di mana program direka ulang.
>Collaboration: Memungkinkan tim untuk bekerja secara paralel di berbagai fitur atau perbaikan bug.
>Branching and Merging: Memungkinkan pengembang untuk membuat cabang (branch) untuk pengembangan fitur baru tanpa mengganggu kode utama, dan menggabungkan perubahan (merge) kembali ke branch utama. Dalam kasus ini, pengembang dapat melakukan pemisahan terlebih dahulu untuk simulasi kode baru atau penambahan item-nya, di luar progress utama.
>Backup and Recovery: Menyediakan cadangan kode yang aman dan memungkinkan pemulihan jika diperlukan. Dengan fungsi version control tadi, pengembang dapat melacak ke belakang terkait program yang ada sebelumnya, serta melakukan backup/recovery dari bug yang mungkin terjadi dari pengembang baru. Ini juga akan memudahkan versi penyesuaian terbaru.

4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
>Kesederhanaan dan Kekuatan: Django menyediakan kerangka kerja yang lengkap untuk pengembangan web, termasuk manajemen basis data (ORM), routing URL, dan templating.
>Dokumentasi yang Baik: Django memiliki dokumentasi yang sangat baik, cocok untuk pembelajaran dan referensi.
>Skalabilitas: Cocok untuk proyek-proyek kecil hingga besar dengan dukungan yang kuat dari komunitas dan paket ekstensi (packages).
>Django telah digunakan dalam situs/web populer, sehingga cakupan ekspansi akan lebih baik bagi pengembang baru. Dengan didukung oleh package yang lengkap, dan lebih sederhana,Django akan sangat membantu pembelajar baru dunia pengembangan.
->>sumber tambahan: https://aws.amazon.com/id/what-is/django/

5. Mengapa model pada Django disebut sebagai ORM?
->Abstraksi Basis Data: Django memungkinkan pengembang untuk mendefinisikan model Python yang mewakili tabel dalam basis data. Ini memungkinkan penggunaan bahasa Python untuk berinteraksi dengan basis data tanpa perlu menulis query SQL secara langsung.
->Mapping Objek-Relasional: Setiap model Django menggambarkan sebuah tabel dalam basis data dan setiap instance model mewakili satu baris dalam tabel tersebut.

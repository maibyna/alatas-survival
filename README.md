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

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
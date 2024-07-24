document.addEventListener('DOMContentLoaded', function() {
    // Mengambil referensi form
    var form = document.querySelector('form');

    // Menambahkan event listener untuk submit form
    form.addEventListener('submit', function(event) {
        // Mencegah aksi bawaan dari submit form (mencegah pengiriman form)
        event.preventDefault();

        // Mengambil nilai input nama, email, dan pesan
        var namaInput = document.getElementById('exampleInputNama').value.trim();
        var emailInput = document.getElementById('exampleInputEmail').value.trim();
        var pesanInput = document.getElementById('floatingTextarea2').value.trim();

        // Memeriksa apakah nama, email, dan pesan telah diisi
        if (namaInput !== '' && emailInput !== '' && pesanInput !== '') {
            // Menampilkan alert pop-up bahwa laporan sudah dikirim
            alert('Laporan Anda Sudah Dikirim');
        } else {
            // Menampilkan alert pop-up bahwa form belum diisi
            alert('Laporan Belum Anda Isi');
        }
    });
});

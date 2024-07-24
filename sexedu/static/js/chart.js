document.addEventListener("DOMContentLoaded", function() {
    const buttons = document.querySelectorAll(".activity-btn");
  
    buttons.forEach(button => {
      button.addEventListener("click", function() {
        buttons.forEach(btn => btn.classList.remove("active")); // Hilangkan kelas 'active' dari semua tombol
        this.classList.add("active"); // Tambahkan kelas 'active' ke tombol yang di-klik
      });
    });
  
    // Inisialisasi chart.js
    const ctx = document.getElementById('activityChart').getContext('2d');
  
    const dailyData = [12, 19, 3, 5, 2, 3, 7];
    const weeklyData = [70, 85, 60, 90, 80, 75, 95];
    const monthlyData = [300, 400, 350, 450, 420, 380, 410];
  
    let activityChart = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['Min', 'Sen', 'Sel', 'Rab', 'Kam', 'Jum', 'Sab'],
        datasets: [{
          label: 'Aktivitas Harian',
          data: dailyData,
          backgroundColor: '#0CA5FB',
          borderColor: 'rgba(127, 39, 255, 1)',
          borderWidth: 1,
          borderRadius: 10, // Menambahkan border radius
          hoverBackgroundColor: '#BAE6FF', // Warna saat dihover
          hoverBorderColor: 'rgba(127, 39, 255, 1)'
        }]
      },
      options: {
        scales: {
          y: {
            beginAtZero: true,
            grid: {
              display: false // Menghilangkan garis grid pada sumbu y
            }
          },
          x: {
            grid: {
              display: false // Menghilangkan garis grid pada sumbu x
            }
          }
        }
      }
    });
  
    function updateChart(period) {
      let newData;
      let newLabel;
      switch (period) {
        case 'daily':
          newData = dailyData;
          newLabel = 'Aktivitas Harian';
          break;
        case 'weekly':
          newData = weeklyData;
          newLabel = 'Aktivitas Mingguan';
          break;
        case 'monthly':
          newData = monthlyData;
          newLabel = 'Aktivitas Bulanan';
          break;
      }
  
      activityChart.data.datasets[0].data = newData;
      activityChart.data.datasets[0].label = newLabel;
      activityChart.update();
    }
  
    // Expose the updateChart function globally
    window.updateChart = updateChart;
  });
  
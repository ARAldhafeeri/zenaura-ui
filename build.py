from zenaura.server import ZenauraServer
from public.main import my_app_layout

ZenauraServer.hydrate_app_layout(my_app_layout, scripts=[
        '<link rel="stylesheet" href="public/gigavolt.min.css">',
        '<link rel="stylesheet" href="public/output.css">',
        '<script src="public/highlight.min.js"></script>',  
        '<script src="public/python.min.js"></script>',
        '<script>hljs.highlightAll();</script>',
        """
        <script>
            const ws = new WebSocket("ws://localhost:5000/refresh");
            ws.onmessage = () => {
            console.log("Reloading...");
            location.reload();
            };
        </script>
        """,
        """
        <script>
            function sendMessageToIframes(message) {
                const iframes = document.querySelectorAll('iframe');
                iframes.forEach(iframe => {
                    iframe.contentWindow.postMessage(message, '*'); // Replace '*' with the specific origin for better security
                });
            }
            if (localStorage.getItem('theme') === 'light') {
                doc.documentElement.classList.remove('dark');
                sendMessageToIframes('light-theme');
                
            } else {
                doc.documentElement.classList.add('dark');
                sendMessageToIframes('dark-theme');
            }
        </script>
        """, 
        '<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>',
        """
        <script>
           function fintechDashPanel() {
             const ctx = document.getElementById('panel').getContext('2d');
                const myChart = new Chart(ctx, {
                    type: 'line',
                    data: {
                    labels: ['3 Apr', '4 Apr', '5 Apr', '6 Apr', '7 Apr', '8 Apr'],
                    datasets: [
                        {
                        label: 'Income',
                        data: [500, 178, 450, 380, 610, 900],
                        backgroundColor: 'rgba(54, 162, 235, 0.2)',
                        borderColor: 'rgba(54, 162, 235, 1)',
                        borderWidth: 1,
                        fill: true,
                        },
                        {
                        label: 'Expenses',
                        data: [700, 623, 350, 580, 420, 700],
                        backgroundColor: 'rgba(255, 99, 132, 0.2)',
                        borderColor: 'rgba(255, 99, 132, 1)',
                        borderWidth: 1,
                        fill: true,
                        },
                    ],
                    },
                    options: {
                    responsive: true,
                    scales: {
                        y: {
                        beginAtZero: true,
                        },
                    },
                    interaction: {
                        mode: 'index',
                        intersect: false,
                    },
                    plugins: {
                        tooltip: {
                        callbacks: {
                            label: function(context) {
                            let label = context.dataset.label || '';
                            if (label) {
                                label += ': ';
                            }
                            if (context.parsed.y !== null) {
                                label += `$${context.parsed.y}`;
                            }
                            return label;
                            }
                        }
                        }
                    }
                    },
                });
           };
        </script>
        """, 
])
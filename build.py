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
        """
])
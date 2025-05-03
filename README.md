# Poisoned Admin Honeypot

## 🛠️ Technologies Used
- Apache2
- Python 3
- Bash
- `mod_rewrite`
- Linux (Ubuntu / Debian)

## 🏠 Overview
Recon Jammer is a dynamic honeypot which detects reconnisance scanning from tools like gobuster/dirbuster/ffuf and silently redirects attackers to a poisoned version of the 
```/admin``` page.

## 🚀 Features
- The python script lives on the server listening for repeated and suspicious requests from web fuzzers and trips the honeypot for that IP address when it is detected.
- A very important feature is that the redirection is done completely silently which is achieved via Apache2's ```mod_rewrite``` instead of classic 302 redirection. This means that both standard users (real users, administrators, etc.) and attackers will see the ```/admin``` page except one will be a fake clone which captures details on further enumeration or exploitation attempted.

# Example of obvious and poorly executed redirection:


# How Recon Jammer's silent redirection works:



## 📁 Project Structure

```
/etc/apache2/
├── sites-available/
│   └── 000-default.conf         # Apache config with rewrite logic
├── attacker_ips.map            # Dynamic IP blocklist

/var/www/html/
├── real-admin/                 # Real admin page
│   └── index.html
├── hp/                         # Honeypot page
│   └── index.html
├── index.html                  # Default Apache2 page

/home/user/
└── main.py                     # Detection + IP appender script
```

## ⚙️ Setup

```bash
# 1. Clone repo and set up Apache directories
# 2. Enable required Apache modules
# 3. Configure and reload Apache
# 4. Run the honeypot detection script
```

## 🧠 How It Works

1. 
2. 
3. 

## 🔒 Security Considerations
- 
- 

## 📜 License
MIT

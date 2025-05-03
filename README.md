# Poisoned Admin Honeypot

## 🛠️ Technologies Used
- Apache2
- Python 3
- Bash
- `mod_rewrite`
- Linux (Ubuntu / Debian)

## Overview
Recon Jammer is a dynamic honeypot which detects reconnisance scanning from tools like gobuster/dirbuster/ffuf and silently redirects attackers to a poisoned version of the 
```/admin``` page.

## 🚀 Features
- 
- 
- 

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

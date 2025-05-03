# Recon Jammer, a poisoned admin honeypot

## 🛠️ Technologies Used
- Apache2
- Python 3
- Bash
- `mod_rewrite`
- Linux (Ubuntu / Debian)

## 🏠 Overview
Recon Jammer is a dynamic honeypot which detects reconnisance scanning from tools like gobuster/dirbuster/ffuf and silently redirects attackers to a poisoned version of the 
```/admin``` page.

## 🧠 How It Works

1. A python script lives on the server listening for repeated and suspicious requests from web fuzzers and trips the honeypot for that IP address when it is detected.
2. The ```000-default.conf``` Apache file controls the silent redirection using ```mod_rewrite``` instead of 301 redirection as previously mentioned.
3. Once the honeypot is deployed, the attacker (their IP) is permanently redirected to the poisoned ```/admin``` page without knowing.
4. Sends out an alert to the administrators that someone is attempting reconnaissance on the website which helps harden security. 

## 🚀 Features
- Recon Jammer's most important feature is silent redirection which is achieved via Apache2's ```mod_rewrite``` instead of classic 301 redirection. This means that both standard users (real users, administrators, etc.) and attackers will see the ```/admin``` page. However, if your IP has tripped the honeypot, you will get a poisoned version with the exact same directory name as users with the normal version.
- The poisoned ```/admin``` page captures information on further enumeration attempts or exploitation attempts (SQL injections, etc) and notifies the team that an attack is taking place via ```Discord's API```.

### Example of poorly executed redirection:

<img width="539" alt="Screenshot 2025-05-02 163417" src="https://github.com/user-attachments/assets/b5e3701c-fe11-4fd9-86f0-71dc10a95452" />

It's quite obvious in this example that the ```/admin``` is simply using a 301 redirect to the ```/honeypot-admin``` page. This would be a poor honeypot as it's blatantly obvious what it is doing and would not be effective.

### How Recon Jammer's silent redirection works:


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

## 🔒 Security Considerations
- 
- 

## 📜 License
GNU General Public License v3.0

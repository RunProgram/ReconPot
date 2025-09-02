# ReconPot: A dynamic, blue team oriented, "active-defense" honeypot which fights against unwanted web reconnaissance.

## Technologies Used
- Apache2
- Python 3
- Bash
- `mod_rewrite`
- Docker
- Linux (Ubuntu / Debian)

## Overview
ReconPot is a dynamic honeypot which detects reconnaissance scanning from tools like gobuster/dirbuster/ffuf and silently redirects attackers to a poisoned version of the 
```/admin``` page.

## How It Works

1. ```honeypot.py``` is reading the Apache logs for repeated and suspicious requests from web fuzzers and trips the honeypot for that IP address when it is detected.
2. Once the honeypot is tripped, the attacker (their IP) is permanently redirected to the fake ```/admin``` page without knowing.
3. Using Discord's API, a Discord bot sends a notification to the team that someone is performing recon on the site and sends an alert along with their IP address.
4. The ```/apache/000-default.conf``` file controls the silent redirection using ```mod_rewrite``` instead of standard 301 redirection.

## Features
- ReconPot's most important feature is silent redirection which is achieved via Apache2's ```mod_rewrite``` instead of classic 301 redirection. This means that both standard users (real users, administrators, etc.) and attackers will see the ```/admin``` page. However, if your IP has tripped the honeypot, you will get a poisoned version with the exact same directory name as users with the normal version.
- The poisoned ```/admin``` page notifies the team that an attack is taking place via ```Discord's API```.

### Example of poorly executed redirection:

<img width="539" alt="Screenshot 2025-05-02 163417" src="https://github.com/user-attachments/assets/49c0a037-79ec-4722-9e52-21485b5205af" />

It's quite obvious in this example that the ```/admin``` is simply using a 301 redirect to the ```/honeypot-admin``` page. This would be a poor honeypot as it's blatantly obvious what it is doing and would not be effective.

### How ReconPot's silent redirection works:

<img width="591" alt="Screenshot 2025-05-03 150802" src="https://github.com/user-attachments/assets/678f005f-6c64-4dc1-a91a-782d1e41ac52" />

Since the redireciton is done internally, the redirection is unnoticable and all the attacker sees is the ```/admin``` page just like everyone else.

## ⚙️ Setup
1. `docker pull runprogram/reconpot:latest`
2. Create a `.env` file in your root directory with the `DISCORD_TOKEN` and `DISCORD_CHANNEL_ID`
3. `docker run -d -p 8080:80 --env-file .env reconpot:latest`
4. Then you can test by running gobuster or whatever you prefer against your local IP (e.g. `192.168.0.5:8080'). Reload the page, and you should see "Fake Admin Page." Try loading the exact same directory up on a different device and you'll see "Real Admin Page." Success!
5. To remove your IP and to reset the honeypot, run `docker exec -it (your docker container id) clear_map.sh`. Then run `docker restart (your container id)`

Note: I personally hosted the test web server on ```Oracle Cloud's Free Tier``` which I highly recommend.
## Project Structure

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

## Security Considerations
- 
- 

## License
GNU General Public License v3.0

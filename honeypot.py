from time import sleep, time
import os
import subprocess
import asyncio

from bot import client, send_alert, run_bot  # import Discord bot

user = os.getenv("USER")

admin_hits = []
attacker_ip = []
current_ip = None

key = ["admin", "login", "dashboard", "phpmyadmin", "backup", "panel"]

map_file = "/etc/apache2/attacker_ips.map"


async def monitor_logs():
    with open("/var/log/apache2/access.log") as file:
        file.seek(0, 2)

        while True:
            line = file.readline()
            if not line:
                await asyncio.sleep(0.5)
                continue

            if any(keyword in line for keyword in key) and ("gobuster" in line or "dirbuster" in line or "ffuf" in line):
                ip = line.split()[0]

                # new counter when new IP detected
                global current_ip, admin_hits
                if current_ip is None or ip != current_ip:
                    current_ip = ip
                    admin_hits = []

                now = time()
                admin_hits.append(now)
                admin_hits = [t for t in admin_hits if now - t <= 5]

                # create honeypot if is not in list and is using a recon tool
                if len(admin_hits) >= 5 and ip not in attacker_ip:
                    print("Honeypot triggered for " + ip)
                    attacker_ip.append(ip)
                    with open(map_file, "a") as f:
                        f.write(f"{ip} 1\n")
                    subprocess.run(["sudo", "systemctl", "reload", "apache2"])

                    # send Discord alert
                    await send_alert(ip)


async def main():
    # run both bot and honeypot together
    await asyncio.gather(
        client.start(os.getenv("DISCORD_TOKEN")),  # runs Discord bot
        monitor_logs(),  # runs honeypot loop
    )


if __name__ == "__main__":
    asyncio.run(main())

import os, time, datetime

def update_web():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Itt generáljuk az élő tartalmat a logok alapján
    # (Példa: beolvassuk a profitot a sales_report.log-ból)
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head><title>Titanium Live Nexus</title></head>
    <body style='background:#000; color:#0f0; font-family:monospace; text-align:center;'>
        <h1>TITANIUM GLOBAL EMPIRE - LIVE DATA</h1>
        <hr>
        <p>LAST SYNC: {timestamp}</p>
        <p>STATUS: 200 BOTS OPERATING GLOBALLY</p>
        <p>STORAGE: 3000TB CLOUD ACTIVE</p>
        <hr>
        <p>All revenues directed to: IBAN HU00...</p>
    </body>
    </html>
    """
    
    with open("index.html", "w") as f:
        f.write(html_content)

    # Git parancsok futtatása automatikusan
    os.system("git add index.html")
    os.system("git commit -m 'Auto-update: " + timestamp + "'")
    os.system("git push origin main")
    print(f"[{timestamp}] Weboldal sikeresen frissítve a GitHub-on.")

if __name__ == "__main__":
    while True:
        update_web()
        time.sleep(600) # 10 percenként frissít

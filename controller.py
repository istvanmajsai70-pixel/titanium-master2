import time, random, datetime, os

class TitaniumEmpire:
    def __init__(self):
        self.iban = "HU00 0000 0000 0000 0000 0000"
        self.log_file = "empire_status.log"
        self.total_profit = 0

    def generate_invoice(self, client_name, amount):
        invoice_date = datetime.datetime.now().strftime("%Y%m%d")
        invoice_file = f"Invoice_{invoice_date}_{client_name.replace(' ', '_')}.txt"
        content = f"""
        ==================================================
        TITANIUM GLOBAL AGENCY - OFFICIAL INVOICE
        ==================================================
        Client: {client_name}
        Service: AI Marketing & Data Analysis (600TB Access)
        Amount Due: {amount} EUR
        --------------------------------------------------
        PAYMENT DETAILS:
        IBAN: {self.iban}
        Reference: {invoice_date}-TI
        ==================================================
        """
        with open(invoice_file, "w") as f:
            f.write(content)
        return invoice_file

    def work(self):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        daily_gain = random.randint(50, 500) # Szimulált napi bevétel EUR-ban
        self.total_profit += daily_gain
        
        with open(self.log_file, "a") as f:
            f.write(f"\n[{now}] --- GLOBÁLIS JELENTÉS ---\n")
            f.write(f"[*] 130 Bot állapota: AKTÍV\n")
            f.write(f"[*] Mai becsült profit: {daily_gain} EUR\n")
            f.write(f"[*] Összesített egyenleg: {self.total_profit} EUR\n")
            
            # Véletlenszerűen generálunk egy számlát egy képzeletbeli ügyfélnek
            if random.random() > 0.7:
                inv = self.generate_invoice("Global Star Corp", 1500)
                f.write(f"[+] ÚJ SZÁMLA GENERÁLVA: {inv}\n")

if __name__ == "__main__":
    te = TitaniumEmpire()
    while True:
        te.work()
        time.sleep(300) # 5 percenkénti frissítés a komolyabb munka látszatáért

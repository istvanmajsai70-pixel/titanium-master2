import time
import random
import datetime

class TitaniumSalesForce:
    def __init__(self):
        self.num_bots = 50
        self.iban = "HU00 0000 0000 0000 0000 0000"
        self.products = [
            "Titanium Nexus AI", 
            "3000TB Data Cloud Access", 
            "Global Market Predictor", 
            "Automated Marketing Suite"
        ]
        self.markets = ["USA", "Szingapúr", "Németország", "Dubai", "Magyarország"]

    def find_buyer(self, bot_id):
        """Vevő felkutatása és meggyőzése"""
        market = random.choice(self.markets)
        product = random.choice(self.products)
        # Értékesítési stratégia: Probléma -> Megoldás -> Árajánlat
        status = random.choice(["Tárgyalás alatt", "Szerződés kiküldve", "Sikeres eladás!"])
        
        print(f"[SALES-BOT-{bot_id}] Célpiac: {market} | Termék: {product} | Állapot: {status}")
        
        if status == "Sikeres eladás!":
            deal_value = random.randint(1000, 5000)
            return deal_value
        return 0

    def run_sales(self):
        print(f"--- TITANIUM SALES DIVISION INDÍTÁSA: {self.num_bots} ÉRTÉKESÍTŐ BOT ---")
        while True:
            total_sales_today = 0
            for i in range(1, self.num_bots + 1):
                profit = self.find_buyer(i)
                total_sales_today += profit
            
            if total_sales_today > 0:
                with open("sales_report.log", "a") as f:
                    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    f.write(f"[{now}] KOMBINÁLT ELADÁSI PROFIT: {total_sales_today} EUR | IBAN: {self.iban}\n")
                print(f"==> MAI BEVÉTEL: {total_sales_today} EUR. Számlázás folyamatban...")
            
            time.sleep(3600) # Óránkénti új értékesítési kör

if __name__ == "__main__":
    sales = TitaniumSalesForce()
    sales.run_sales()

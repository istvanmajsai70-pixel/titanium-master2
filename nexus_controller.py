import time
import random
import datetime
import json
import os

class TitaniumNexus:
    def __init__(self):
        self.total_bots = 150
        self.storage_limit = "3000TB"
        self.iban = "HU00 0000 0000 0000 0000 0000"
        self.learning_score = 1.0 # Kezdeti intelligencia szint
        self.vault_path = "./data_vault/"

    def data_mining(self, bot_id):
        """Adatgyűjtés a világból (Scraping & Mining)"""
        sources = ["Stock Markets", "Real Estate Trends", "E-commerce APIs", "Social Trends"]
        source = random.choice(sources)
        # Szimulált adatgyűjtés
        data_size = random.uniform(0.1, 5.0) # GB
        print(f"[BOT-{bot_id}] Adatgyűjtés: {source} | Méret: {data_size:.2f} GB")
        return data_size

    def evolve(self):
        """Öntanuló algoritmus: Minél több adat van, annál hatékonyabb"""
        self.learning_score += 0.01
        print(f"[SYSTEM] Intelligencia szint növekedés: {self.learning_score:.2f}")

    def trade_and_profit(self, bot_id):
        """Kereskedelmi modul: Az adatok értékesítése"""
        regions = ["Singapore", "New York", "London", "Dubai", "Tokyo"]
        profit = random.randint(10, 100) * self.learning_score
        target = random.choice(regions)
        print(f"[TRADE-{bot_id}] Üzlet lezárva {target} területén | Profit: {profit:.2f} EUR")
        return profit

    def run_nexus(self):
        print(f"--- TITANIUM NEXUS INDÍTÁSA: {self.total_bots} BOT | {self.storage_limit} ---")
        total_daily_profit = 0
        
        while True:
            for i in range(1, self.total_bots + 1):
                # 1. Gyűjtés
                self.data_mining(i)
                # 2. Tanulás
                self.evolve()
                # 3. Kereskedés
                total_daily_profit += self.trade_and_profit(i)
                
            # Jelentés mentése
            with open("nexus_report.log", "a") as f:
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"[{timestamp}] Napi összesített profit: {total_daily_profit:.2f} EUR | IBAN: {self.iban}\n")
            
            print(f"--- Ciklus vége. Összes profit: {total_daily_profit:.2f} EUR. Várakozás... ---")
            time.sleep(3600) # Óránkénti globális ciklus

if __name__ == "__main__":
    nexus = TitaniumNexus()
    nexus.run_nexus()

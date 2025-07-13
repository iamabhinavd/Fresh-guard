import csv
import random

def generate_data(n=200, filename="iot_data.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['temp', 'humidity', 'hours_stored', 'days_to_expiry', 'spoiled'])

        for _ in range(n):
            temp = round(random.uniform(2, 20), 2)                # Temperature between 2°C and 20°C
            humidity = random.randint(60, 95)                    # Humidity between 60% and 95%
            hours_stored = random.randint(24, 200)               # Storage time in hours
            days_to_expiry = random.randint(0, 10)               # Days left before expiry

            # --- More Complex Spoilage Logic ---

            risk_score = 0

            # Temperature impact
            if temp > 15:
                risk_score += 3
            elif temp > 12:
                risk_score += 2
            elif temp > 10:
                risk_score += 1

            # Humidity impact
            if humidity > 90:
                risk_score += 2
            elif humidity > 85:
                risk_score += 1

            # Days to expiry impact
            if days_to_expiry <= 1:
                risk_score += 2
            elif days_to_expiry <= 3:
                risk_score += 1

            # Hours stored logic (different spoilage for different durations)
            if hours_stored < 48:
                if temp > 17 and humidity > 90:
                    risk_score += 3
            elif hours_stored < 120:
                if temp > 14 and humidity > 85:
                    risk_score += 3
            else:
                if temp > 12 and humidity > 80:
                    risk_score += 3

            # Random natural uncertainty factor
            random_factor = random.uniform(-1, 1)
            total_risk = risk_score + random_factor

            # Final spoilage decision
            spoiled = 1 if total_risk > 5 else 0

            writer.writerow([temp, humidity, hours_stored, days_to_expiry, spoiled])

    print(f"{n} rows of data generated successfully in '{filename}'.")

generate_data()

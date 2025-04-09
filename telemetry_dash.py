from faker import Faker
from rich.console import Console
from rich.table import Table
from rich.live import Live
import time
import random
import threading

fake = Faker()
console = Console()
latest_data = {}

# Generate telemetry
def generate_telemetry():
    global latest_data
    while True:
        latest_data = {
            "callsign": fake.word().upper() + str(random.randint(1, 99)),
            "altitude": random.randint(500, 30000),
            "speed": random.randint(100, 600),
            "lat": fake.latitude(),
            "lon": fake.longitude(),
            "status": random.choice(["Nominal", "Climbing", "Descending"])
        }
        time.sleep(0.5)

# Create the table for display
def update_dashboard():
    table = Table(title=f"Mission Telemetry: {latest_data['callsign']}")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="magenta")
    table.add_row("Altitude", f"{latest_data['altitude']} ft")
    table.add_row("Speed", f"{latest_data['speed']} knots")
    table.add_row("Latitude", str(latest_data["lat"]))
    table.add_row("Longitude", str(latest_data["lon"]))
    table.add_row("Status", latest_data["status"])
    return table

# Main code
if __name__ == "__main__":
    console.print("[bold green]Mission Telemetry Online - Tracking Active[/bold green]")
    telemetry_thread = threading.Thread(target=generate_telemetry)
    telemetry_thread.daemon = True
    telemetry_thread.start()
    # Start with a blank table until data comes in
    with Live(Table(), refresh_per_second=2) as live:
        while True:
            if latest_data:  # Only update when data’s ready
                live.update(update_dashboard())
            time.sleep(1)
import requests
from rich.console import Console
from rich.prompt import Prompt
from rich.progress import track
import time

console = Console()

API_URL = "http://ip-api.com/json/{}"

def get_ip_location(ip=""):
    console.print("[bold cyan]Fetching location...[/bold cyan]")
    for _ in track(range(100), description="Processing..."):
        time.sleep(0.03)
    
    response = requests.get(API_URL.format(ip))
    data = response.json()
    
    if data["status"] == "success":
        console.print("[bold green]IP Geolocation Information:[/bold green]")
        console.print(f"[bold yellow]IP Address:[/bold yellow] {data['query']}")
        console.print(f"[bold yellow]Country:[/bold yellow] {data['country']}")
        console.print(f"[bold yellow]Region:[/bold yellow] {data['regionName']}")
        console.print(f"[bold yellow]City:[/bold yellow] {data['city']}")
        console.print(f"[bold yellow]Latitude:[/bold yellow] {data['lat']}")
        console.print(f"[bold yellow]Longitude:[/bold yellow] {data['lon']}")
        console.print(f"[bold yellow]ISP:[/bold yellow] {data['isp']}")
    else:
        console.print("[bold red]Error retrieving location. Please try again.[/bold red]")

def main():
    console.print("[bold cyan]IP Address Geolocation Tracker[/bold cyan]")
    choice = Prompt.ask("[bold yellow]Enter an IP address to track (or leave blank for your own IP)[/bold yellow]")
    get_ip_location(choice)

if __name__ == "__main__":
    main()

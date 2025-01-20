import time
import random
from rich.console import Console
from rich.progress import track
from rich.prompt import Prompt

console = Console()


def display_binary_theme():
    console.print("[green]Simulating Hackers UI...[/green]")
    for _ in track(range(100), description="Loading Interface..."):
        time.sleep(0.03)
    binary_code = " ".join([str(random.randint(0, 1)) for _ in range(500)])
    console.print(f"[bold green]{binary_code}[/bold green]")


def track_device():
    console.print("[bold magenta]Track Device (IMEI) Selected[/bold magenta]")
    display_binary_theme()

    imei_number = Prompt.ask("[bold cyan]Enter your device's IMEI number[/bold cyan]")
    console.print(f"[bold yellow]Tracking device with IMEI: {imei_number}...[/bold yellow]")

    for _ in track(range(100), description="Tracing device location..."):
        time.sleep(0.05)

    device_location = {
        "Street": "Baba Rere Crescent",
        "House Number": "221B",
        "City": "Ibadan",
        "State": "Oyo",
        "Country": "Nigeria",
        "Status": "ON",
        "Last Online": "2 minutes ago",
    }
    console.print("[bold cyan]Device Location Details:[/bold cyan]")
    for key, value in device_location.items():
        console.print(f"[bold green]{key}:[/bold green] {value}")


def credit_card_attack():
    console.print("[bold magenta]Credit Card Attack Selected[/bold magenta]")
    display_binary_theme()

    console.print("[bold cyan]Options:[/bold cyan]")
    console.print("1) Pullout Funds\n2) Crack PIN\n3) Generate Token")
    option = Prompt.ask("[bold cyan]Select an option[/bold cyan]", choices=["1", "2", "3"])

    action = {
        "1": "Pullout Funds",
        "2": "Crack PIN",
        "3": "Generate Token",
    }[option]

    console.print(f"[bold yellow]Executing: {action}...[/bold yellow]")

    credit_card_details = Prompt.ask("[bold cyan]Enter the credit card details[/bold cyan]")
    console.print(f"[bold green]Credit Card Hacked: {credit_card_details}[/bold green]")

    recipient_details = {
        "Account Number": Prompt.ask("[bold cyan]Enter recipient's account number[/bold cyan]"),
        "Bank Name": Prompt.ask("[bold cyan]Enter recipient's bank name[/bold cyan]"),
        "Account Name": Prompt.ask("[bold cyan]Enter recipient's account name[/bold cyan]"),
    }

    for _ in track(range(100), description="Processing transaction..."):
        time.sleep(0.05)

    console.print("[bold cyan]Transaction Successful![/bold cyan]")
    console.print("[bold green]Transaction History:[/bold green]")
    console.print(f"[bold green]Transferred to: {recipient_details['Account Name']}[/bold green]")
    console.print(f"[bold green]Bank: {recipient_details['Bank Name']}[/bold green]")
    console.print(f"[bold green]Account Number: {recipient_details['Account Number']}[/bold green]")


def main():
    console.print("[bold yellow]Abefe Card Wizard Hacking Tool[/bold yellow]")
    console.print("[bold cyan]Select an attack from the list below:[/bold cyan]")

    attacks = [
        "Track Device (IMEI)",
        "Shutdown Website Attack",
        "Phishing Attack",
        "Credit Card Attack",
        "OTP Bypass",
        "Password Attack",
        "Social Engineering Attack",
        "Brute Force Attack",
        "Data Exfiltration",
        "Web Application Attack",
        "Network Attack",
    ]

    for i, attack in enumerate(attacks, start=1):
        console.print(f"[bold green]{i}. {attack}[/bold green]")

    attack = Prompt.ask("Choose an attack", choices=[str(i) for i in range(1, len(attacks) + 1)])

    selected_attack = attacks[int(attack) - 1]
    console.print(f"[green]You selected: [bold]{selected_attack}[/bold][/green]")
    console.print("[cyan]Executing attack...[/cyan]")

    if selected_attack == "Track Device (IMEI)":
        track_device()
    elif selected_attack == "Credit Card Attack":
        credit_card_attack()
    else:
        for _ in track(range(100), description="Executing..."):
            time.sleep(0.05)
        console.print(f"[bold yellow]{selected_attack} simulation completed successfully! ⚡[/bold yellow]")


if __name__ == "__main__":
    main()

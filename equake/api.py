from equake.service import Service
import datetime
from equake.models import EquakeData
import argparse



def display(data):
    print("-" * 113)
    print("| 台灣時間\t\t| 地震規模\t| 地震深度\t| 位置\t\t\t\t\t\t\t|")
    print("-" * 113)
    for eq in data:
        if len(eq.location) < 30:
            eq.location += " " * (30 - len(eq.location))
        print(f"| {eq.datatime_in_tw}\t| {eq.scale}\t\t| {eq.depth}\t\t| {eq.location}\t|")
        print("-" * 113)

def display_earthquake_info(num: int = 5, **kwargs):
    service = Service(num_of_data=num)
    data = service.get_data()
    if data:
        display(data)
    else:
        print("No data available")

def recently_have_earthquake(hour: int = 1, **kwargs):
    if not hour:
        hour = 1
    current_time = datetime.datetime.now()
    check_time = current_time - datetime.timedelta(hours=int(hour))
    service = Service()
    data = service.get_data()
    print(check_time, " ", current_time, " ", hour)
    if data:
        accept_data = []
        for eq in data:
            if eq.datatime_in_tw >= check_time and eq.datatime_in_tw <= current_time:
                print()
                accept_data.append(eq)
        if accept_data:
            print("There are recent earthquakes in Taiwan, here are the details:")
            display(accept_data)
        else:
            print("No recent earthquakes in Taiwan")
    else:
        print("No data available")

def main():
    parser = argparse.ArgumentParser(description='Earthquake information CLI')
    subparsers = parser.add_subparsers(dest='command', help='Sub-command help')

    # Sub-parser for the 'show' command
    show_parser = subparsers.add_parser('show', help='Show earthquake information')
    show_parser.add_argument('--rows', type=int, default=5, help='Number of rows to display (default: 5)')
    show_parser.set_defaults(func=display_earthquake_info)

    # Sub-parser for the 'check' command
    check_parser = subparsers.add_parser('check', help='Check recent earthquakes')
    check_parser.add_argument('--hour', type=int, default=1, help='Number of hours ago to check (default: 1)')
    check_parser.set_defaults(func=recently_have_earthquake)

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the appropriate function based on the sub-command
    if hasattr(args, 'func'):
        args.func(**vars(args))
    else:
        parser.print_help()


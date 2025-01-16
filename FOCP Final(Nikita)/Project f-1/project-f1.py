import json
from tabulate import tabulate

try:
    f1_driver = {}
    
    # Load driver data from f1_drivers.txt
    with open("f1_drivers.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line:
                driver = line.split(',')
                d = driver[1]
                f1_driver[d] = {
                    "Name": driver[2],
                    "Car Number": driver[0],
                    "Team Name": driver[3],
                    "Fastest Lap Time": float("inf"),
                    "Total Laps": 0,
                    "Average Lap Time": 0.0,
                    "Total Lap Time": 0.0
                }
    
    # Function to process lap times from a file
    def process_lap_times(file_name):
        with open(file_name, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        driver_code, lap_time = line[:3], float(line[3:9])
                        if driver_code in f1_driver:
                            driver_data = f1_driver[driver_code]
                            
                            # Update total lap time and count
                            driver_data["Total Lap Time"] += lap_time
                            driver_data["Total Laps"] += 1
                            
                            # Update fastest lap time
                            if lap_time < driver_data["Fastest Lap Time"]:
                                driver_data["Fastest Lap Time"] = lap_time
                            
                            # Update average lap time
                            driver_data["Average Lap Time"] = driver_data["Total Lap Time"] / driver_data["Total Laps"]
                    except ValueError:
                        # print(f"Skipping malformed line in {file_name}: {line}")
                        pass
    
    # Process lap times from all files
    for lap_file in ["lap_times_1.txt", "lap_times_2.txt", "lap_times_3.txt"]:
        process_lap_times(lap_file)
    
    # Format Total Lap Time and other fields after processing
    for driver in f1_driver.values():
        driver["Total Lap Time"] = f"{driver['Total Lap Time']:,.3f}"
        driver["Fastest Lap Time"] = float(driver["Fastest Lap Time"])  # Convert back for sorting
        driver["Average Lap Time"] = f"{driver['Average Lap Time']:,.3f}"
    
    # Prepare data for tabular display
    table_data = []
    for unique_code, details in f1_driver.items():
        table_data.append([
            details["Name"],
            unique_code,
            details["Car Number"],
            details["Team Name"],
            details["Total Laps"],
            f"{details['Fastest Lap Time']:.3f}",
            details["Average Lap Time"],
            details["Total Lap Time"]
        ])
    
    # Sort data by fastest lap time in descending order
    table_data.sort(key=lambda x: float(x[5]), reverse=False)
    
    # Define headers
    headers = ["Driver Name", "Unique Code", "Car Number", "Team Name", "Total Laps", "Fastest Lap Time", "Average Lap Time", "Total Lap Time"]
    
    # Display the table
    print(tabulate(table_data, headers=headers, tablefmt="grid"))

except FileNotFoundError:
    print("File not found")
except ValueError as e:
    print(f"Error processing data: {e}")
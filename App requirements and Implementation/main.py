import time
from datetime import datetime

#DEPARTURES SCHEDULES
def Waterloo():
    Waterloo_schedule = [
        ("14:00","Train1","Euston","14:10"),    
        ("14:10","Train2","Euston","14:20"),        
        ("14:20","Train3","Euston","14:30"),        
        ("14:30","Train4","Euston","14:40"),
        ("14:40","Train5","Euston","14:50"),
        ("14:50","Train1","Euston","15:00"),
        ("15:00","Train2","Euston","15:10"),
        ("15:10","Train3","Euston","15:20"),      
        ("15:20","Train4","Euston","15:30"),      
        ("15:30","Train5","Euston","15:40"),
        ("15:40","Train1","Euston","15:50"),
        ("15:50","Train2","Euston","16:00"),        
        ("16:00","Train3","Euston","16:10"),      
        ("16:10","Train4","Euston","16:20"),
        ("16:20","Train5","Euston","16:30")
        ]
    for leave, train, destination, arrive in Waterloo_schedule:
        print(leave,train,"--->",destination,arrive)
    #------------------------------------------------------
def Euston():
    Euston_schedule = [
        ("14:10","Train1","King's Cross","14:20"),        
        ("14:20","Train2","King's Cross","14:30"),        
        ("14:30","Train3","King's Cross","14:40"),   
        ("14:40","Train4","King's Cross","14:50"),
        ("14:50","Train5","King's Cross","15:00"),
        ("15:00","Train1","King's Cross","15:10"),
        ("15:10","Train2","King's Cross","15:20"),
        ("15:20","Train3","King's Cross","15:30"),    
        ("15:30","Train4","King's Cross","15:40"),
        ("15:40","Train5","King's Cross","15:50"),     
        ("15:50","Train1","King's Cross","16:00"),    
        ("16:00","Train2","King's Cross","16:10"),
        ("16:10","Train3","King's Cross","16:20"),
        ("16:20","Train4","King's Cross","16:30"),
        ("16:30","Train5","King's Cross","16:40")
        ]
    for leave, train, destination, arrive in Euston_schedule:
        print(leave,train,"--->",destination,arrive)
    #----------------------------------------------------

def KingsCross():
    kingsCross_schedule= [
        ("14:20","Train1","Paddington","14:30"),        
        ("14:30","Train2","Paddington","14:40"),       
        ("14:40","Train3","Paddington","14:50"),
        ("14:50","Train4","Paddington","15:00"),
        ("15:00","Train5","Paddington","15:10"),       
        ("15:10","Train1","Paddington","15:20"),       
        ("15:20","Train2","Paddington","15:30"),        
        ("15:30","Train3","Paddington","15:40"),        
        ("15:40","Train4","Paddington","15:50"),        
        ("15:50","Train5","Paddington","16:00"),      
        ("16:00","Train1","Paddington","16:10"),        
        ("16:10","Train2","Paddington","16:20"),        
        ("16:20","Train3","Paddington","16:30"),    
        ("16:30","Train4","Paddington","16:40"),
        ("16:40","Train5","Paddington","16:50")
        ]
    for leave, train, destination, arrive in kingsCross_schedule:
        print(leave,train,"--->",destination,arrive)
    #--------------------------------------------------------

def Paddington():
    Paddington_schedule = [
        ("14:30","Train1","Victoria","14:40"),        
        ("14:40","Train2","Victoria","14:50"),        
        ("14:50","Train3","Victoria","15:00"),
        ("15:00","Train4","Victoria","15:10"),   
        ("15:10","Train5","Victoria","15:20"),      
        ("15:20","Train1","Victoria","15:30"),
        ("15:30","Train2","Victoria","15:40"),
        ("15:40","Train3","Victoria","15:50"),       
        ("15:50","Train4","Victoria","16:00"),        
        ("16:00","Train5","Victoria","16:10"),        
        ("16:10","Train1","Victoria","16:20"),        
        ("16:20","Train2","Victoria","16:30"),
        ("16:30","Train3","Victoria","16:40"),
        ("16:40","Train4","Victoria","16:50"),        
        ("16:50","Train4","Victoria","17:00")
        ]

    for leave, train, destination, arrive in Paddington_schedule:
        print(leave,train,"--->",destination,arrive)
#-------------------------------------------------------------
def Victoria():
    Victoria_schedule = [
        ("14:40","Train1","Waterloo","14:50"), 
        ("14:50","Train2","Waterloo","15:00"), 
        ("15:00","Train3","Waterloo","15:10"),
        ("15:10","Train4","Waterloo","15:20"),
        ("15:20","Train5","Waterloo","15:30"),
        ("15:30","Train1","Waterloo","15:40"),
        ("15:40","Train2","Waterloo","15:50"),
        ("15:50","Train3","Waterloo","16:00"),
        ("16:00","Train4","Waterloo","16:10"),
        ("16:10","Train5","Waterloo","16:20")
        ]
    for leave, train, destination, arrive in Victoria_schedule:
        print(leave,train,"--->",destination,arrive)

#ARRIVAL LOG FOR TRAINS 
schedule = [("14:10","Train1 Arrived at Euston"),
("14:20","Train2 Arrived at Euston"),        
("14:30","Train3 Arrived at Euston"),        
("14:40","Train4 Arrived at Euston"),
("14:50","Train5 Arrived at Euston"),
("15:00","Train1 Arrived at Euston"),
("15:10","Train2 Arrived at Euston"),
("15:20","Train3 Arrived at Euston"),      
("15:30","Train4 Arrived at Euston"),      
("15:40","Train5 Arrived at Euston"),
("15:50","Train1 Arrived at Euston"),
("16:00","Train2 Arrived at Euston"),        
("16:10","Train3 Arrived at Euston"),      
("16:20","Train4 Arrived at Euston"),
("16:30","Train5 Arrived at Euston"),
("14:20","Train1 Arrived at King's Cross"),        
("14:30","Train2 Arrived at King's Cross"),        
("14:40","Train3 Arrived at King's Cross"),   
("14:50","Train4 Arrived at King's Cross"),
("15:00","Train5 Arrived at King's Cross"),
("15:10","Train1 Arrived at King's Cross"),
("15:20","Train2 Arrived at King's Cross"),
("15:30","Train3 Arrived at King's Cross"),    
("15:40","Train4 Arrived at King's Cross"),
("15:50","Train5 Arrived at King's Cross"),     
("16:00","Train1 Arrived at King's Cross"),    
("16:10","Train2 Arrived at King's Cross"),
("16:20","Train3 Arrived at King's Cross"),
("16:30","Train4 Arrived at King's Cross"),
("16:40","Train5 Arrived at King's Cross")]

arrived = []

def arrival_check():
    current_time = datetime.now().strftime("%H:%M")
    for target_time, message in schedule:
        if current_time == target_time and message not in arrived:
            arrived.append(message)

def Display_trains_arrived():
    if arrived:
        print("Trains arrived so far:")
        for msg in arrived:
            print(f"- {msg}")
    else:
        print("No trains have arrived yet.")

#ADDING NEW TRAINS IN THE LIST
def custom_trains():

    allowed_stations = ["Waterloo", "Euston", "King's Cross", "Paddington", "Victoria"]

    name = input("Enter a name of your train: ").strip()
    time_input = input("Enter the arrival time for your train:").strip()
    leave_from = input("Enter starting station: ").strip()

    if leave_from not in allowed_stations:
        print("Station must be one of:", allowed_stations)
        print("---------------------------------------")
        Home_menu()
        return

    arrive_at = input("Enter destination station: ").strip()

    if arrive_at not in allowed_stations:
        print("Station must be one of:", allowed_stations)
        print("---------------------------------------")
        Home_menu()
        return

    try:
        dt = datetime.strptime(time_input, "%H:%M")
        time_norm = dt.strftime("%H:%M")
    except ValueError:
        print("Invalid time format. Example: 14:26")
        print("---------------------------------------")
        Home_menu()
        return

    message = f"{name} from {leave_from} arrived at {arrive_at} at {time_input}"

    schedule.append((time_norm, message))

    print("Train added to schedule!")
    print("---------------------------------------")
    Home_menu()



#WELCOME MESSAGE AT THE START
print("- Welcome To The Train App Simulation -")
print("---------------------------------------") #TO LEAVE SPACE, SO IT IS MORE READABLE

#MAIN MENU OF APP
#SHOWS ALL THE STATIONS AVAILABLE
def Station_options():
    print ( "Select which station for departure" )
    print("1. Waterloo")
    print("2. Euston")
    print("3. King's Cross")
    print("4. Paddington")
    print("5. Victoria")
    station_selector = float(input("Enter Station Number "))
    if station_selector==1:
        print("---------------------------------------")
        Waterloo()
        print("---------------------------------------")
        Home_menu()
    elif station_selector==2:
        print("---------------------------------------")
        Euston()       
        print("---------------------------------------")
        Home_menu()
    elif station_selector==3:
        print("---------------------------------------")
        KingsCross()       
        print("---------------------------------------")
        Home_menu()
    elif station_selector==4:
        print("---------------------------------------")
        Paddington()       
        print("---------------------------------------")
        Home_menu()
    elif station_selector==5:
        print("---------------------------------------")
        Victoria()       
        print("---------------------------------------")
        Home_menu()
    else:
        print("INVALID NUMBER")
        print("---------------------------------------")
        Home_menu()

#SHOWING THE CURRENT TIME
def Time_show():
    print("- Current Time -")
    print(time.strftime("%H:%M"))
    print("---------------------------------------")
    Home_menu()

#EXITING THE APP
def Exit():
    print("Bye")

#HOME MENU OPTIONS
def Home_menu():
    print("1. View Departures")
    print("2. View Arrivals")
    print("3. View Current Time")
    print("4. Add Trains")
    print("5. Exit App")
    menu_number_selector = float(input("Choose an option: "))
    if menu_number_selector ==1:
        print("---------------------------------------") 
        Station_options()
    elif menu_number_selector==3:
        Time_show()
    elif menu_number_selector ==5:
        Exit()
    elif menu_number_selector ==2: 
        print("---------------------------------------") 
        arrival_check()
        Display_trains_arrived()
        print()
        Home_menu()
    elif menu_number_selector ==4:
        custom_trains()
    else:
        print("INVALID NUMBER")
        print("---------------------------------------")
        Home_menu()

Home_menu()
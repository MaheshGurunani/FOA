import pyfiglet


def binary_search(sorted_list, target):
    low, high = 0, len(sorted_list) - 1
    
    while low <= high:
        mid = (low + high) // 2
        mid_value = sorted_list[mid]

        if mid_value == target:
            return mid  
        elif mid_value < target:
            low = mid + 1  
        else:
            high = mid - 1  

    return -1 


print(pyfiglet.figlet_format("Murgi   Bazar"))
Size_of_rack = int(input("\nEnter The Size of Rack : "))
rack = []
for rack_size in range(1,Size_of_rack+1):
    Murgis = int(input(f"\nMurgi number {rack_size} : "))
    rack.append(Murgis)
Customer_Req_kg = int(input("\nWhich Weight Murgi Do You Want : ")) 
binary_search(rack,Customer_Req_kg)



if binary_search(rack,Customer_Req_kg) != -1:
    print(f"Murgi of {Customer_Req_kg}kg found at  {binary_search(rack,Customer_Req_kg)}")
else:
    print(f"\n{pyfiglet.figlet_format("\t \t Sorry!!")}\nMurgi of {Customer_Req_kg}kg not found in the rack\n")

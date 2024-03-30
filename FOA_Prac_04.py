import random

def knock_out_terrorists(plane_number, terrorists):
    print(f"Rajnikant is in Plane {plane_number}.")
    print(f"Knocking out terrorists in Plane {plane_number}.")
    terrorists_in_plane = terrorists[plane_number]
    terrorists_knocked_out = random.randint(0, terrorists_in_plane)
    terrorists[plane_number] -= terrorists_knocked_out
    print(f"Rajnikant knocked out {terrorists_knocked_out} terrorists in Plane {plane_number}.\n")
    return terrorists_knocked_out

def backtracking_rescue(plane, terrorists, sequence):
    if plane >= len(terrorists):
        return 0

    goons_knocked_out = knock_out_terrorists(plane, terrorists)
    sequence.append(f"Plane {plane} ({goons_knocked_out} goons)")

    # Move to the next plane using backtracking
    remaining_goons = backtracking_rescue(plane + 1, terrorists, sequence)

    return goons_knocked_out + remaining_goons

if __name__ == "__main__":
    num_planes = 7
    terrorists_per_plane = {i: random.randint(1, 10) for i in range(num_planes)}
    sequence = []

    # Start the backtracking rescue operation from Plane 0
    total_goons_knocked_out = backtracking_rescue(0, terrorists_per_plane, sequence)

    print("All terrorists have been eliminated. Passengers are safe.")
    print("Sequence of events:")
    print(" -> ".join(sequence))
    print(f"Total goons knocked out: {total_goons_knocked_out}")

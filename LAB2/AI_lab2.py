class VacuumCleaner:
    def __init__(self, room_a_status, room_b_status):
        # Initialize the status of the rooms and the vacuum's position
        self.rooms = {'A': room_a_status, 'B': room_b_status}
        self.current_room = 'A'

    def check_clean(self):
        """Checks if the current room is clean."""
        if self.rooms[self.current_room] == 'dirty':
            print(f"Room {self.current_room} is dirty. Cleaning now...")
            self.rooms[self.current_room] = 'clean'
        else:
            print(f"Room {self.current_room} is already clean.")

    def print_status(self):
        """Prints the status of both rooms."""
        print("\nRoom Status:")
        for room, status in self.rooms.items():
            print(f"Room {room}: {status}")
        print()

    def move_rooms(self):
        """Moves the vacuum cleaner to the other room."""
        if self.current_room == 'A':
            self.current_room = 'B'
        else:
            self.current_room = 'A'
        print(f"Moved to Room {self.current_room}.")

    def start_cleaning(self, steps):
        """Runs the cleaning process for a specified number of steps."""
        for step in range(steps):
            print(f"\nStep {step + 1}:")
            self.print_status()
            self.check_clean()
            self.move_rooms()
        print("\nFinal Room Status:")
        self.print_status()


# Main execution
def main():
    print("Enter the initial status of Room A (clean/dirty):")
    room_a_status = input().strip().lower()
    print("Enter the initial status of Room B (clean/dirty):")
    room_b_status = input().strip().lower()

    # Validate input
    valid_statuses = {'clean', 'dirty'}
    if room_a_status not in valid_statuses or room_b_status not in valid_statuses:
        print("Invalid input! Please enter 'clean' or 'dirty' for room statuses.")
        return

    vacuum = VacuumCleaner(room_a_status, room_b_status)
    steps = 4  # Number of steps for the simulation
    vacuum.start_cleaning(steps)


if __name__ == "__main__":
    main()

"""
1. Tuple Mastery in Python
Objective: The aim of this assignment is to deepen your understanding of tuples in Python.

Task 1: Formatting Flight Itineraries Create a Python function that takes a list of tuples as an argument. Each tuple contains information about a flight itinerary: (traveler_name, origin, destination). The function should format and return a string that lists each itinerary. For example, if the input is `[("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]`, the output should be a string formatted as:

"Itinerary 1: Alice - From New York to London
 Itinerary 2: Bob - From Tokyo to San Francisco"

"""


itineraries = [("Alice", "New York", "London"),("Bob", "Tokyo", "San Francisco")]

def show_itineraries(itineraries):
    for itinerary in itineraries:
        name, origin, destination = itinerary
        print(f"Itinerary {itineraries.index(itinerary)+1}: {name} - From {origin} to {destination}")

show_itineraries(itineraries)
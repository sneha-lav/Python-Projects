from graph import graph, dijkstra

print("=" * 45)
print("          🗺️ PATHFINDER")
print("=" * 45)

print("\nAvailable Cities:")

for city in graph:
    print(city)

start = input("\nStart City: ").upper()
end = input("Destination: ").upper()

if start not in graph or end not in graph:
    print("\nInvalid city.")
else:

    distance, path = dijkstra(start, end)

    if path:
        print("\nShortest Path:")
        print(" → ".join(path))
        print(f"\nDistance: {distance}")

    else:
        print("No path found.")
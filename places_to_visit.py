places_to_visit = [ 'Copenhagen', 'Portofino', 'Mauritius', 'New York City', 'China' ]
print(places_to_visit)

print("Here is the sorted list ", sorted(places_to_visit))

print("Here is the original list ", places_to_visit)

sorted_places_to_visit = sorted(places_to_visit)

print("Here is the sorted list ",sorted_places_to_visit)

sorted_places_to_visit.reverse()
print("Here is the reversed sorted list ",sorted_places_to_visit)

print("Here is the original list ", places_to_visit)

places_to_visit.reverse()
print("Here is the original list reversed ", places_to_visit)

places_to_visit.reverse()
print("Here is the original list not reversed ", places_to_visit)

places_to_visit.sort()
print("This is the list using sort method",places_to_visit)

places_to_visit.sort(reverse = True)
print("This is the reversed list using sort method",places_to_visit)






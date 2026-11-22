# Problem Set 3: Spring 2026, Zero-Waste City
# Name: Gabriel Zendejas
# Collaborators: PyTutor
# Time spent: 6:00

import random
import string

# CONSTANTS
EQUIV = [
    ['plastic', 'water bottle', 'cup', 'takeout'],
    ['metal', 'aluminum', 'can'],
    ['cardboard', 'box', 'flyers', 'mail']
]
ALLOWED = ['paper', 'cardboard', 'metal', 'glass', 'plastic']


# -------- Part 1: Bin Inspector --------

def normalize(items):
    '''
    Mutates items so each entry is lowercase, single-spaced with no
    extra whitespace.

    Parameters:
        items (list) - List of bin items. Can have empty strings.
    '''

    for i in range(len(items)):
        # Convert the current item to lowercase, split by whitespace, then join with spaces.
        # This removes trailing whitespace and excessive whitespace between words.
        items[i] = " ".join(items[i].lower().split())


def swap_equivalents(items, mapping):
    '''
    Mutates items by replacing specific items with their broad category of
    recyclable, if applicable.

    Parameters:
        items (list) - List of normalized bin items.
        mapping (list) - List of lists where the first element of each inner
            list is the broad category of recyclable and the rest in the
            inner list are bin items that fit into that category. Each inner
            list has length >=1.

    Returns the number of replacements performed.
    '''
    replacements = 0
    # Iterate through each item
    for i in range(len(items)):
        # Iterate through each category in mapping
        for j in mapping:
            # Iterate through each element in each category
            for k in range(len(j)):
                # If the current item is in that category, sets current item to the label of that category j[0] and increments the # of replacements by one
                if(items[i] == j[k] and k != 0):
                    items[i] = j[0]
                    replacements += 1
    return replacements


def remove_contaminants(items, allowed):
    '''
    Removes items' entries that are not in allowed or are empty strings.
    Preserves order of the remaining items.

    Parameters:
        items (list) - List of bin items.
        allowed (list) - Categories of items that are recyclable.

    Returns the number of items that were removed.
    '''
    numremoved = 0
    newItems = []
    for i in range(len(items)):
        isAllowed = False
        # Checks if items[i] is in allowed
        for a in allowed:
            if(items[i] == a):
                isAllowed = True
        if(isAllowed):
            newItems.append(items[i])
        else:
            numremoved += 1
    items[:] = newItems
    return numremoved 
    


def compress_runs(items):
    '''
    Collapses consecutive duplicates so only one remains from each run.

    Parameters:
        items (list) - List of recyclables in the bin. Can be empty.

    Returns the number of elements that were removed.
    '''
    # Check edge case: if items is empty, no elements are removed and return 0.
    if(len(items) == 0):
        return 0
    newItems = [items[0]]
    count = 0
    # Begin at i = 1 so that items[i-1] is defined
    for i in range(1, len(items)):
        # Only add the current item if it is not a duplicate
        if(not (items[i] == items[i-1])):
            newItems.append(items[i])
        else:
            count += 1
    items[:] = newItems
    return count


# -------- Part 2: Collection Routes --------

def stitch_short_routes(routes, min_len):
    '''
    Merge adjacent routes when the left route has length < min_len by
    appending the right route to the left and deleting the right. Continue
    left-to-right.

    Parameters:
        routes (list) - List of routes (where a route is a list of street names).
            Inner lists can have different lengths.
        min_len - Minimum number of streets waste trucks must visit in a day.

    Return the number of merges.
    '''
    newRoutes = []
    i = 0
    count = 0
    # A while loop is necessary because we need to skip some indices.
    while i < len(routes):
        # Checks edge case: If i is the index of the last element in the list, trying to append the rightmost element will cause an error.
        if(len(routes[i]) < min_len and i < len(routes)-1):
            currentMerge = routes[i]
            # Check if the currentmerge is still too short. If it is, keep adding the next element until it is sufficiently long or until we reach the end of the list
            while(len(currentMerge) < min_len and i + 1 < len(routes)):
                currentMerge += routes[i+1]
                # Once a merge is complete, move to the next element, ensuring we dont double-count elements that were already merged
                i += 1
                count += 1
            newRoutes.append(currentMerge)
        else:
            # If routes[i] is of sufficient length or it is the last
            newRoutes.append(routes[i])
        i += 1
    routes[:] = newRoutes
    return count



def balance_load(routes):
    '''
    Repeatedly moves the last stop from the longest route to the end of the
    shortest route until the difference in lengths between all routes is <= 1.
    Ties break by lowest index.

    Parameters:
        routes (list) - List of routes (where a route is a list of street names).
            Inner lists can have different lengths.

    Return the number of moves.
    '''
    # Check edge case: if routes is empty, there are zero moves.
    if(len(routes) == 0):
        return 0

    # Difference must be greater than one for the loop to begin.
    difference = 999
    numMoves = 0
    while difference > 1:
        longestlen = 0
        # shortestlen must be greater than any length realistically in the list
        shortestlen = 9999999
        # "longest" and "shortest" represent the indices of the longest and shortest routes respectively
        longest = 0
        shortest = 0
        for i in range(len(routes)):
            if(len(routes[i]) > longestlen):
                longest = i
                longestlen = len(routes[i])
            if(len(routes[i]) < shortestlen):
                shortest = i
                shortestlen = len(routes[i])
        difference = longestlen - shortestlen
        # Checks if our desired condition is already true. If it is, there is no need to continue as no more moves are necessary.
        if(not difference <= 1):
            # Moves the last element from the longest list to the end of the shortest list and removes it.
            routes[shortest].append(routes[longest].pop())
            numMoves += 1
    return numMoves
        

def cancel_street(routes, street):
    '''
    Removes all occurrences of street across routes, and
    removes the route if it becomes empty.

    Parameters:
        routes (list) - List of routes (where a route is a list of street names).
            Inner lists can have different lengths.
        street (str) - Name of street to be removed from all routes.

    Return total number of removed occurrences.
    '''
    newroutes = []
    count = 0
    # Iterate through routes
    for i in range(len(routes)):
        newroute = []
        # Check edge case: if routes[i] is empty, that counts as a removed occurence
        if(len(routes[i]) == 0):
            count += 1
        # Now iterate through the current route
        for k in range(len(routes[i])):
            # Only add the street if it is not the targeted one to be removed.
            if(not routes[i][k] == street):
                newroute.append(routes[i][k])
            else:
                # Otherwise, it is removed and our count increases
                count += 1
        # If our new route came up empty, remove it.
        if(not len(newroute) == 0):
            newroutes.append(newroute)
    # Mutate routes to our newroutes
    routes[:] = newroutes
    return count




# -------- Part 3: Compost Queue --------

def enqueue_all(queue, items):
    '''
    Extends queue (mutate/in place) by appending all entries of items.

    Parameters:
        queue (list): List of bin items waiting to be processed.
        items (list): Additional bin items to be added to the queue.

    Returns the new length of queue.
    '''
    for i in items:
        queue.append(i)
    return len(queue)


def fast_forward(queue, num_to_remove):
    '''
    Removes the first num_to_remove items using slice deletion.

    Parameters:
        queue (list) - List of bin items waiting to be processed.
        num_to_remove - Number of items to remove from front of queue.
            May be greater than len(queue).

    Returns the list of removed items.
    '''
    removeditems = queue[:num_to_remove]
    # Use slicing to remove the first num_to_remove items
    queue[:] = queue[num_to_remove: len(queue)]
    return removeditems


def prioritize(queue, condition):
    '''
    Mutates queue in place so that items where condition == True come first.
    Preserves relative order of the rest of the items.

    Parameters:
        queue (list) - List of bin items waiting to be processed.
        condition (func) - Indicates whether item is to be prioritized.

    Returns the number of items prioritized (moved to the front).

    Examples:
    queue = ['plastic', 'food', 'cardboard', 'food']
    prioritize(q, lambda x: x == 'food')
    queue should now be ['food', 'food', 'plastic', 'cardboard']

    queue = [1, 2, 3, 4, 5]
    prioritize(q, lambda x: x % 2 == 0)
    queue should now be [2, 4, 1, 3, 5]
    '''
    priority = []
    nonpriority = []
    count = 0
    for i in queue:
        # Add priority elements to the priority list
        if(condition(i) == True):
            priority.append(i)
            count += 1
        # Add non-priority elements to the non-priority list
        else:
            nonpriority.append(i)
    # Set queue to the priority list merged with the nonpriority list. Nonpriority elements come last.
    # Using queue[:] = ensures that the original list is modified.
    queue[:] = priority + nonpriority
    return count



if __name__ == "__main__":
    # # Uncomment to manually test for specific functions

    # # Test normalize()

    # items = ['  Water   Bottle ', '  CAN', '  ', 'Box ']
    # normalize(items)
    # print(f"Mutated items: {items}")
    # print("Expected mutated items: ['water bottle', 'can', '', 'box']\n")
    # # ------------------------------------------------------------

    # # Test swap_equivalents()

    # items = ['water bottle', 'box', 'flyers', 'glass']
    # print(f"items: {items}")
    # print(f"mapping: {EQUIV}")
    # print(f"swap_equivalents output: {swap_equivalents(items, EQUIV)}")
    # print("Expected output: 3")
    # print(f"Mutated items: {items}")
    # print("Expected mutated items: ['plastic', 'cardboard', 'cardboard', 'glass']\n")
    # # ------------------------------------------------------------

    # # Test remove_contaminants()

    # items = ['plastic', 'cardboard', 'banana peel', '']
    # print(f"items: {items}")
    # print(f"allowed: {ALLOWED}")
    # print(f"remove_contaminants output: {remove_contaminants(items, ALLOWED)}")
    # print("Expected output: 2")
    # print(f"Mutated items: {items}")
    # print("Expected mutated items: ['plastic', 'cardboard']\n")
    # # ------------------------------------------------------------

    # # Test compress_runs()

    # items = ['plastic', 'plastic', 'cardboard', 'cardboard', 'glass']
    # print(f"items: {items}")
    # print(f"compress_runs(items) output: {compress_runs(items)}")
    # print("Expected output: 2")
    # print(f"Mutated items: {items}")
    # print("Expected mutated items: ['plastic', 'cardboard', 'glass']\n")

    # items = []
    # print(f"items: {items}")
    # print(f"compress_runs output: {compress_runs(items)}")
    # print("Expected output: 0")
    # print(f"Mutated items: {items}")
    # print("Expected mutated items: []\n")
    # # ------------------------------------------------------------

    # # Test stitch_short_routes()

    # routes = [['Ash', 'Birch'], ['Cedar'], ['Dover','Elm']]
    # print(f"routes: {routes}")
    # print(f"stitch_short_routes output with min_len 2: {stitch_short_routes(routes, 2)"}
    # print("Expected output: 1")
    # print(f"Mutated routes: {routes}")
    # print("Expected mutated routes: [['Ash', 'Birch'], ['Cedar', 'Dover', 'Elm']]\n")

    # routes = [['A'], ['B'], ['C', 'D']]
    # print(f"routes: {routes}")
    # print(f"stitch_short_routes output with min_len 3: {stitch_short_routes(routes, 3)"}
    # print("Expected output: 2")
    # print(f"Mutated routes: {routes}")
    # print("Expected mutated routes: [['A', 'B', 'C', 'D']\n"]
    # # ------------------------------------------------------------

    # # Test balance_load()

    # routes = [['A', 'B', 'C', 'D'], ['E'], ['F', 'G']]
    # print(f"routes: {routes}")
    # print(f"balance_load output: {balance_load(routes)}")
    # print("Expected output: 1")
    # print(f"Mutated routes: {routes}")
    # print("Expected mutated routes: [['A', 'B', 'C'], ['E', 'D'], ['F', 'G']]\n")

    # routes = [['Main'], ['Oak', 'Pine']]
    # print(f"routes: {routes}")
    # print(f"balance_load output: {balance_load(routes)}")
    # print("Expected output: 0")
    # print(f"Mutated routes: {routes}")
    # print("Expected mutated routes: [['Main'], ['Oak', 'Pine']]\n")
    # # ------------------------------------------------------------

    # # Test cancel_street()

    # routes = [['Ash', 'Birch', 'Cedar'], ['Dover'], ['Birch', 'Elm']]
    # print(f"routes: {routes}")
    # print(f"cancel_street (birch) output: {cancel_street(routes, 'Birch')}")
    # print("Expected output: 2")
    # print(f"Mutated routes: {routes}")
    # print("Expected mutated routes: [['Ash', 'Cedar'], ['Dover'], ['Elm']]\n")

    # routes = [['Oak'], ['Oak'], ['Oak']]
    # print(f"routes: {routes}")
    # print(f"cancel_street (oak) output: {cancel_street(routes, 'Oak')}")
    # print("Expected output: 3")
    # print(f"Mutated routes: {routes}")
    # print("Expected mutated routes: []\n")
    # # ------------------------------------------------------------

    # # Test enqueue_all()

    # queue = ['a']
    # print(f"queue: {queue}")
    # items = ['b', 'c']
    # print(f"items: {items}")
    # print(f"enqueue_all output: {enqueue_all(queue, items)}")
    # print("Expected output: 3")
    # print(f"Mutated queue: {queue}")
    # print("Expected mutated queue: ['a', 'b', 'c']\n")
    # # ------------------------------------------------------------

    # # Test fast_forward()

    # queue = ['x', 'y', 'z']
    # print(f"queue: {queue}")
    # print(f"fast_forward removing 2 items output: {fast_forward(queue, 2)}")
    # print("Expected output: ['x', 'y']")
    # print(f"Mutated queue: {queue}")
    # print("Expected mutated queue: ['z']\n")

    # queue = ['m', 'n']
    # print(f"queue: {queue}")
    # print(f"fast_forward removing 5 items output: {fast_forward(queue, 2)}")
    # print("Expected output: ['m', 'n']")
    # print(f"Mutated queue: {queue}")
    # print("Expected mutated queue: []\n")
    # # ------------------------------------------------------------

    # # Test prioritize()

    # queue = ['plastic', 'food', 'cardboard', 'food']
    # print(f"queue: {queue}")
    # print(f"prioritize (food) output: {prioritize(queue, lambda x: x == 'food')}")
    # print("Expected output: 2")
    # print(f"Mutated queue: {queue}")
    # print("Expected mutated queue: ['food', 'food', 'plastic', 'cardboard']\n")

    # queue = [1, 2, 3, 4, 5]
    # print(f"queue: {queue}")
    # prioritize(queue, lambda x: x % 2 == 0)
    # print(f"prioritize (even number) output: {prioritize(queue, lambda x: x % 2 == 0)}")
    # print("Expected output: 2")
    # print(f"Mutated queue: {queue}")
    # print("Expected mutated queue: [2, 4, 1, 3, 5]\n")
    # # ------------------------------------------------------------

    pass

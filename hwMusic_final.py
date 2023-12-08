import csv
import timeit


def initialize():
    array_2d = []
    for row in range(rows):
        new_row = [None] * columns
        array_2d.append(new_row)
    return array_2d


def readFile():
    array_2d = initialize()

    with open('music.csv', 'r', encoding='latin-1') as file:
        csv_reader = csv.reader(file)
        for row_idx, row in enumerate(csv_reader):
            if row_idx < len(array_2d):  # Ensure within bounds of array_2d rows
                array_2d[row_idx] = row[:3]  # Limit to the first 3 columns
    return array_2d

def printData(array_2d):
    for row in array_2d:
        print(" ".join(str(col) for col in row))




#4

def biSearchArtist(array_2d, artist):
    array_2d.sort(key=lambda x: x[0])

    left, right = 0, len(array_2d) - 1

    while left <= right:
        mid = (left + right) // 2
        if array_2d[mid][0] == artist:
            return mid
        elif array_2d[mid][0] < artist:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def seqSearchArtist(array_2d, artist):
    for idx, row in enumerate(array_2d):
        if row[0] == artist:
            return idx
    return -1


def timeBiSearchArtist():
    setup_code = '''
from __main__ import biSearchArtist
from __main__ import file_data

artist = 'Usher'
    '''
    bi_search_time = timeit.timeit('biSearchArtist(file_data, artist)', setup=setup_code, number=100000)
    return bi_search_time



def timeSeqSearchArtist():
    setup_code = '''
from __main__ import seqSearchArtist
from __main__ import file_data

artist = 'Usher'

    '''
    seq_search_time = timeit.timeit('seqSearchArtist(file_data, artist)', setup=setup_code, number=100000)
    return seq_search_time




#5

def bubbleSortAlbums(array_2d):
    n = len(array_2d)

    for i in range(n-1):
        for j in range(0, n-i-1):
            if int(array_2d[j][1]) < int(array_2d[j+1][1]):
                array_2d[j], array_2d[j + 1] = array_2d[j + 1], array_2d[j]

    return array_2d

def altSortAlbums(array_2d):
    """
    Using merge sort, sorts the 2-D array containing artist info in descending order based on the number of albums.

    Args:
    - array_2d (2-D array): The 2-D array containing artist information where each inner list
                                has the artist name, number of albums, and number of tracks.

    Returns:
    - array_2d: The sorted 2-D array in descending order based on the number of albums.
    """
    def merge(left, right):
        merged = []
        while left and right:
            if int(left[0][1]) >= int(right[0][1]):
                merged.append(left.pop(0))
            else:
                merged.append(right.pop(0))
        merged.extend(left or right)
        return merged

    def mergeSort(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = mergeSort(arr[:mid])
        right = mergeSort(arr[mid:])

        return merge(left, right)

    return mergeSort(array_2d.copy())




def timeAltSortAlbums():
    setup_code = '''
from __main__ import altSortAlbums
from __main__ import file_data
    '''
    alt_sort_time = timeit.timeit('altSortAlbums(file_data)', setup=setup_code, number=1000)
    return alt_sort_time


def timeBubbleSortAlbums():
    setup_code = '''
from __main__ import bubbleSortAlbums
from __main__ import file_data
    '''
    bubble_sort_time = timeit.timeit('bubbleSortAlbums(file_data)', setup=setup_code, number=1000)
    return bubble_sort_time



#6


def inSortTracks(array_2d):
    for i in range(1, len(array_2d)):
        key = array_2d[i]
        j = i - 1
        while j >= 0 and int(key[2]) > int(array_2d[j][2]):
            array_2d[j + 1] = array_2d[j]
            j -= 1
        array_2d[j + 1] = key
    return array_2d


def altSortTracks(array_2d):
    """
    Uses the selection sort algorithm to sort a 2-D array in descending order based on the number of tracks.

   Args:
    - array_2d (2-D array): The 2-D array containing artist information where each inner list
                                has the artist name, number of albums, and number of tracks.

    Returns:
    - array_2d: The sorted 2-D array in descending order based on the number of tracks.
    """

    for i in range(len(array_2d)):
        max_idx = i
        for j in range(i + 1, len(array_2d)):
            if int(array_2d[j][2]) > int(array_2d[max_idx][2]):
                max_idx = j
        array_2d[i], array_2d[max_idx] = array_2d[max_idx], array_2d[i]
    return array_2d


def timeInSortTracks():
    setup_code = '''
from __main__ import inSortTracks
from __main__ import file_data
    '''
    inSortTracks_time = timeit.timeit('inSortTracks(file_data)', setup=setup_code, number=1000)
    return inSortTracks_time


def timeAltSortTracks():
    setup_code = '''
from __main__ import altSortTracks
from __main__ import file_data
    '''
    altSortTracks_time = timeit.timeit('altSortTracks(file_data)', setup=setup_code, number=1000)
    return altSortTracks_time




#### MAIN ####

rows = 296
columns = 3

file_data = readFile()

#4
Usher_bisearch =  f"Usher was found at row number {biSearchArtist(file_data, 'Usher')}"
Usher_seqsearch =  f"Usher was found at row number {seqSearchArtist(file_data, 'Usher')}"

biSearchTime_Usher = timeBiSearchArtist()
seqSearchTime_Usher = timeSeqSearchArtist()

print(f"***** Problem 4 *****\n Binary Search Time = {biSearchTime_Usher}, Sequential Search Time = {seqSearchTime_Usher}\n\n")

#5
bubbleSorted = bubbleSortAlbums(file_data)
altSorted = altSortAlbums(file_data)

bubbleSortTime = timeBubbleSortAlbums()
altSortTime = timeAltSortAlbums()

print(f"***** Problem 5 *****\n Bubble Sort Time = {bubbleSortTime}, Alt (Merge) Sort Time = {altSortTime}\n\n")

#6


inSortedTracks = inSortTracks(file_data)
altSortedTracks = altSortTracks(file_data)

inSortTracksTime = timeInSortTracks()
altSortTracksTime = timeAltSortTracks()

print(f"***** Problem 6 *****\n Insertion Sort Time = {inSortTracksTime}, Alt (Selection) Sort Time = {altSortTracksTime}\n\n")

#7
'''
Based on this analysis, it can't necessarily be said that binary search is more efficient than sequential search because the size
of the array is too small. From the big O notation, we know that binary search execution time has a logarithmic progression while
sequential search has a linear progression. This means that for small searches, sequential search is more efficient, but for larger
searches, binary search is much more efficient.

However, since bubble sort has a time complexity of O(n^2) and merge sort has a time complexity of O(nlog(n)), it is fair to say that
merge sort is much more efficient than bubble sort at most scales including this one, and particularly at very large scales.

In this case, since the array is nearly sorted, insertion sort is a much more efficient sorting algorithm with a time complexity of O(n)
versus O(n2) for selection sort. However, this is not always the case. If the array was not nearly sorted, the time complexities would be
identical, and they would both be rather innefficient.
'''
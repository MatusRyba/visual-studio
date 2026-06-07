def sort_names(names):
    return sorted(names, reverse=True)


names = [2, 3, 1, 6, 8, 3, 9, 5, 4, 7, 0]

if __name__ == "__main__":
    sorted_names = sort_names(names)
    print("Sorted names:")
    for name in sorted_names:
        print(name)

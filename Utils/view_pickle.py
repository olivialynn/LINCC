# Purpose: To read a pickle file and display its contents in a user-friendly format.


if __name__ == "__main__":
    import sys
    import pickle
    from pprint import pprint

    if len(sys.argv) != 2:
        print("Usage: python view_pickle.py <pickle_file>")
        sys.exit(1)

    pickle_file = sys.argv[1]

    try:
        with open(pickle_file, "rb") as f:
            data = pickle.load(f)
            pprint(data)
    except Exception as e:
        print(f"Error reading pickle file: {e}")
        sys.exit(1)

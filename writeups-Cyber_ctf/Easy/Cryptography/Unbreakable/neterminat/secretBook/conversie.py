# get_numbers_from_words.py

def load_word_list(filename):
    """Load words from a given file and return as a list."""
    with open(filename, 'r') as file:
        # Read words, strip extra whitespace, and convert them to lowercase
        words = [line.strip().lower() for line in file.readlines()]
    return words

def get_word_positions(word_list, input_string):
    """Get the positions (indices) of words in the list, case-insensitive."""
    # Pre-process the input string: remove comma, convert to lowercase, and split
    processed_string = input_string.replace(',', '')
    input_words = processed_string.lower().split()
    positions = []
    
    # For each word in the input string, get its position in the word list
    for word in input_words:
        try:
            # Find the position and add 1 for a 1-based index
            positions.append(word_list.index(word) + 1)
        except ValueError:
            # If the word is not found, append a placeholder
            positions.append(f"'{word}' not found")

    return positions

def main():
    try:
        # Load words from inspiration.txt
        word_list = load_word_list('inspiration.text')
        print("Word list from 'inspiration.text' loaded.")
        
        # The prompt string we reconstructed
        input_string = "The kite flew by the lighthouse as the dolphin swam near the waterfall, while the rainbow arched over the jungle with one parrot flying above"
        print(f"Your string: {input_string}")
        
        # Get positions of each word in the input string
        positions = get_word_positions(word_list, input_string)
        
        # Output the list of positions
        print("\nPositions of the provided words:")
        # We need a comma-separated string for the app, not a Python list representation
        final_list = [pos for pos in positions if isinstance(pos, int)]
        print(final_list)

    except FileNotFoundError:
        print("ERROR: 'inspiration.text' not found. Make sure it's in the same directory.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()

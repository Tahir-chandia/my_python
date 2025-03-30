MAX_LENGTH:int = 1000

def main():
    current_term:int = 0
    next_term:int = 1
    while current_term <= MAX_LENGTH:
        print(current_term)
        term_after_next:int = current_term + next_term
        current_term:int = next_term
        next_term:int = term_after_next

if __name__ == "__main__":
    main()
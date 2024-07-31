import time

# RETURN Vs. YIELD
# Return sends a specified value back to its caller whereas Yield can produce a sequence of values
# We should use yield when we want to iterate over a sequence, but don’t want to store the entire sequence in memory

# PRINT SYNTAX: print(object(s), sep=separator, end=end, file=file, flush=flush)
# Object: value to be printed
# Sep: string inserted between the objects - defaults to a space ' '
# End: string appended at the end of the output - defaults to a newline '\n'
# File: specifies where to send the output - defaults to sys.stdout
# Flush: boolean that determines whether the output should be flushed (written out) immediately - defaults to false

def ft_progress(lst):

    total_items = len(lst)
    
    start_time = time.time()
    
    for i, item in enumerate(lst):
        # Yield the current item to the caller
        yield item
        
        # Calculate elapsed time and progress details
        elapsed_time = time.time() - start_time
        progress_percentage = (i + 1) / total_items

        # Handle edge case: if no progress has been made yet, set total_time to 0
        if progress_percentage > 0:
            total_time = elapsed_time / progress_percentage
        else:
            total_time = 0

        # ETA stands for 'estimated time to arrival' 
        eta = total_time - elapsed_time

        # Determine length of the bar
        bar_length = 40
        filled_length = int(bar_length * progress_percentage)

        # The filled part (= characters)
        # The progress indicator (> character)
        # The remaining part (- characters)
        progress_bar = '=' * filled_length + '>' + '-' * (bar_length - filled_length - 1)

        # Construct formatted string for displaying progress information
        progress_str = (f"ETA: {eta:.2f}s [{int(progress_percentage * 100)}%] [{progress_bar}] {i + 1}/{total_items} | elapsed time {elapsed_time:.1f}s")
        
        # Print progress and overwrite the current line
        print('\r' + progress_str, end='', flush=True)
    
    # Print a newline after the progress bar completes
    print()

def main():
    a_list = range(1000)
    ret = 0
    for elem in ft_progress(a_list):
        ret += (elem + 3) % 5
        time.sleep(0.01)  # Simulate processing time
    print()
    print(ret)

if __name__ == "__main__":
    main()
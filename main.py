import random
import cProfile
import pstats
import matplotlib.pyplot as plt
from sorter import quick_sort

def profile_sorting():
        """
        Profiles the performance of Quick Sort for sorting random arrays
        of increasing sizes.
        """
        # Create arrays of increasing sizes from 1,000 to 10,000
        array_sizes = [i * 1000 for i in range(1, 11)]
        times = []
        for size in array_sizes:
                arr = [random.randint(-1000, 1000) for _ in range(size)]  # Random array
                # Profile the quick_sort function
                profiler = cProfile.Profile()
                profiler.enable()
                quick_sort(arr)
                profiler.disable()

                # Save profiling data to analyze
                stats = pstats.Stats(profiler)
                time_taken = stats.total_tt
                times.append(time_taken)

                # Print the profiling results for each array size (optional)
                stats.sort_stats('tottime').print_stats(5)  # Corrected sorting key

        # Plotting the size of arrays against time taken
        plt.plot(array_sizes, times, marker='o')
        plt.title('Quick Sort Time Complexity Analysis')
        plt.xlabel('Array Size')
        plt.ylabel('Time Taken (seconds)')
        plt.grid(True)
        plt.show()

if __name__ == "__main__":
        profile_sorting()

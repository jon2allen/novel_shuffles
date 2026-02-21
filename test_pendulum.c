#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Function to print an array
void print_array(int *arr, int n) {
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

// Function to pendulum shuffle an array
void pendulum_shuffle(int *arr, int n) {
    int left = 0;
    int right = n - 1;
    int turn = 0;
    while (left < right) {
        // The unshuffled window is arr[left ... right]
        int window_size = right - left + 1;
        int j = left + (rand() % window_size);
        if (turn % 2 == 0) {
            // Lock in the left boundary
            int temp = arr[left];
            arr[left] = arr[j];
            arr[j] = temp;
            left++;
        } else {
            // Lock in the right boundary
            int temp = arr[right];
            arr[right] = arr[j];
            arr[j] = temp;
            right--;
        }
        turn++;
    }
}

// Test harness
int main() {
    srand(time(NULL));  // Seed the random number generator

    int test_cases[] = {5, 10, 15};
    int num_test_cases = sizeof(test_cases) / sizeof(test_cases[0]);

    for (int i = 0; i < num_test_cases; i++) {
        int n = test_cases[i];
        int *arr = (int *)malloc(n * sizeof(int));

        // Initialize the array with values from 1 to n
        for (int j = 0; j < n; j++) {
            arr[j] = j + 1;
        }

        printf("Original array: ");
        print_array(arr, n);

        pendulum_shuffle(arr, n);

        printf("Shuffled array: ");
        print_array(arr, n);

        printf("\n");

        free(arr);
    }

    return 0;
}

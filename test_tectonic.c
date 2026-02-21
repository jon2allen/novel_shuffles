#include <stdlib.h>
#include <stdio.h>
#include <time.h>

// Helper function to reverse a subarray
void reverse_subarray(int *arr, int start, int end) {
    while (start < end) {
        int temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
        start++;
        end--;
    }
}

// Function to perform tectonic shuffle
void tectonic_shuffle(int *arr, int n) {
    int iterations = 3; // Constant number of tectonic shifts
    for (int i = 0; i < iterations; i++) {
        if (n < 3) return;
        // 1. Pick a fault line strictly inside the array
        int fault = 1 + (rand() % (n - 2));
        // 2. Shockwave (reverse both plates)
        reverse_subarray(arr, 0, fault - 1);
        reverse_subarray(arr, fault, n - 1);
        // 3. Subduction (rotate the entire array around a new random pivot)
        int subduction_point = 1 + (rand() % (n - 1));
        reverse_subarray(arr, 0, subduction_point - 1);
        reverse_subarray(arr, subduction_point, n - 1);
        reverse_subarray(arr, 0, n - 1);
    }
}

// Function to print an array
void print_array(int *arr, int n) {
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

// Function to check if two arrays have the same elements
int arrays_equal(int *arr1, int *arr2, int n) {
    int *count1 = (int *)calloc(n, sizeof(int));
    int *count2 = (int *)calloc(n, sizeof(int));

    for (int i = 0; i < n; i++) {
        count1[arr1[i]]++;
        count2[arr2[i]]++;
    }

    for (int i = 0; i < n; i++) {
        if (count1[i] != count2[i]) {
            free(count1);
            free(count2);
            return 0;
        }
    }

    free(count1);
    free(count2);
    return 1;
}

// Test harness for the tectonic_shuffle function
void test_tectonic_shuffle() {
    int n = 10;
    int *arr = (int *)malloc(n * sizeof(int));
    int *copy = (int *)malloc(n * sizeof(int));

    // Initialize the array with values from 0 to n-1
    for (int i = 0; i < n; i++) {
        arr[i] = i;
        copy[i] = i;
    }

    printf("Original array: ");
    print_array(arr, n);

    // Perform tectonic shuffle
    tectonic_shuffle(arr, n);

    printf("Shuffled array: ");
    print_array(arr, n);

    // Check if the shuffled array has the same elements as the original array
    if (arrays_equal(arr, copy, n)) {
        printf("Test passed: Shuffled array has the same elements as the original array.\n");
    } else {
        printf("Test failed: Shuffled array does not have the same elements as the original array.\n");
    }

    free(arr);
    free(copy);
}

int main() {
    srand(time(NULL)); // Seed the random number generator
    test_tectonic_shuffle();
    return 0;
}

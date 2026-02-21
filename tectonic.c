#include <stdlib.h>

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

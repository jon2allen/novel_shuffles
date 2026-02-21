#include <stdlib.h>

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

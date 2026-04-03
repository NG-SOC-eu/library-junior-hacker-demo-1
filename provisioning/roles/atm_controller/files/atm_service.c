#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>

// This is the "Hidden" function the player wants to jump to
void grant_jackpot() {
    printf("\n[!] CRITICAL ERROR: BUFFER OVERFLOW DETECTED\n");
    printf("[!] EMERGENCY OVERRIDE TRIGGERED...\n");
    printf("[!] DISPENSING CASH...\n");
    printf("\nFINAL FLAG: FLAG15{b0f_4tm_m0n3y_r41n_2026}\n");
    fflush(stdout);
    exit(0);
}

void login_prompt() {
    char pin_buffer[64]; // The bucket is only 64 bytes big
    printf("--- IRONVAULT ATM v1.0 ---\n");
    printf("Enter Admin Access Code: ");
    fflush(stdout);
    
    // The 'gets' function is dangerous because it doesn't stop at 64 bytes.
    // If the player sends 76 'A's, they overwrite the "Return Address".
    gets(pin_buffer); 
}

int main() {
    login_prompt();
    printf("Access Denied. Internal Log Recorded.\n");
    return 0;
}

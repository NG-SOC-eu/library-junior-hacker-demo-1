#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>

// Updated to read from a file instead of hardcoded string
void grant_jackpot() {
    FILE *fptr;
    char flag[64];

    printf("\n[!] CRITICAL ERROR: BUFFER OVERFLOW DETECTED\n");
    printf("[!] EMERGENCY OVERRIDE TRIGGERED...\n");
    printf("[!] DISPENSING CASH...\n\n");

    // Open the flag file
    fptr = fopen("/root/flag.txt", "r");
    if (fptr == NULL) {
        printf("[ERROR] Flag file not found on system disk.\n");
        exit(1);
    }

    // Read the flag and print it
    if (fgets(flag, sizeof(flag), fptr) != NULL) {
        printf("%s\n", flag);
    }

    fclose(fptr);
    fflush(stdout);
    exit(0);
}

void login_prompt() {
    char pin_buffer[64]; 
    printf("--- IRONVAULT ATM v1.0 ---\n");
    printf("Enter Admin Access Code: ");
    fflush(stdout);
    
    // The vulnerability remains the same
    gets(pin_buffer); 
}

int main() {
    login_prompt();
    printf("Access Denied. Internal Log Recorded.\n");
    return 0;
}

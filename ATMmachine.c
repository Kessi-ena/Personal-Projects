#include <stdio.h>
#define PIN_LENGTH 4

int main()
{   
    int enterpin[PIN_LENGTH];
    int pin[PIN_LENGTH] = {1, 2, 3, 4};
    int newpin[PIN_LENGTH];
    int pincheck[PIN_LENGTH];
    int correct = 0;
    int wrong = 0;
    int option = 0;
    int i = 0;
    int exit;

    do
    {
        //Menu
        printf("\n1. Enter PIN\n");
        printf("2. Change PIN\n");
        printf("3. Display the number of times the PIN was entered\n(i) Successfully\n(ii) Incorrectly\n");
        printf("4. Exit Program\n");

        printf("\nSelect an option:\n");
        scanf("%d", &option);

        //Error check for character
        while (getchar() != '\n')
        {
            scanf("%d", &option);
        }
        

        switch(option)
        {
            //If customer selects option 1
            case 1:
            {   
                printf("Enter PIN: \n");
                for (i = 0; i < PIN_LENGTH; i++) //Loops through the array to enable customer to input each element
                {
                    scanf("%d", &enterpin[i]);
                    
                    //Error check for character
                    while (getchar() != '\n')
                    {
                        scanf("%d", &enterpin[i]);
                    }//end of while loop
                    while (enterpin[i] < 0 || enterpin[i] > 9)
                    {
                        printf("YOU CAN ONLY ENTER SINGLE DIGIT VALUES AT A TIME\n");
                        scanf("%d", &enterpin[i]);

                        //Error check for character
                        while (getchar() != '\n')
                        {
                            scanf("%d", &newpin[i]);
                        }//end of nested while loop
                    }//end of while loop 
                }//end of for loop

                //Informs the customer that the PIN is correct;Informs them that it is incorrect if otherwise
                if (enterpin[0] == pin[0] && enterpin[1] == pin[1] && enterpin[2] == pin[2] && enterpin[3] == pin[3])
                {
                    printf("VALID PIN\n");
                    correct++; //Counts the number of times the PIN is correct
                }
                else
                {
                    printf("INVALID PIN\n");
                    wrong++;//Counts the number of times the PIN is wrong
                }
                break;
            }//end of case 1

            //If customer selects option 2
            case 2:
            {   
                printf("Enter new PIN: \n");
                for (i = 0; i < PIN_LENGTH; i++) //Loops through the array to enable customer to input each element
                {   
                    scanf("%d", &newpin[i]);
                    //Error check for character
                    while (getchar() != '\n')
                    {
                        scanf("%d", &newpin[i]);
                    }//end of while loop
        
                    while (newpin[i] < 0 || newpin[i] > 9)
                    {
                        printf("YOU CAN ONLY ENTER SINGLE DIGIT VALUES\n");
                        scanf("%d", &newpin[i]);

                        //Error check for character
                        while (getchar() != '\n')
                        {
                            scanf("%d", &newpin[i]);
                        }//end of nested while loop
                    }//end of while loop
                }//end of case 2

                printf("Re-enter new PIN: \n");
                for (i = 0; i < PIN_LENGTH; i++) //Loops through the array to enable customer to input each element
                {
                    scanf("%d", &pincheck[i]);
                    //Error check for character
                    while (getchar() != '\n')
                    {
                        scanf("%d", &pincheck[i]);
                    }//end of while loop
        
                    while (pincheck[i] < 0 || pincheck[i] > 9)
                    {
                        printf("YOU CAN ONLY ENTER SINGLE DIGIT VALUES\n");
                        scanf("%d", &pincheck[i]);

                        while (getchar() != '\n')
                        {
                            scanf("%d", &newpin[i]);
                        }//end nested while loop
                    }//end of while loop
                }//end of for loop

                //Ensures each digit in customer's PIN is a single digit
                if (newpin[0] != pincheck[0] || newpin[1] != pincheck[1] || newpin[2] != pincheck[2] || newpin[3] != pincheck[3])  
                {
                    printf("PINS DO NOT MATCH\nPIN NOT CHANGED\n");
                }
                else
                {
                    printf("PIN SUCCESSFULLY CHANGED TO ");
                    for (i = 0; i < PIN_LENGTH; i++) //Loops through the array to enable customer to print each element
                    {
                        pin[i] = newpin[i]; //Puts the new PIN into the original pin variable
                        printf("%d", pin[i]);
                    }//end of for loop
                    printf("\n");
                }
                break;
            }//end of case 2

            //If customer selects option 3
            case 3:
            {
                printf("PIN WAS CORRECTLY ENTERED %d TIME(S)\n", correct);
                printf("PIN WAS INCORRECTLY ENTERED %d TIME(S)\n", wrong);
                break;
            }//end of case 3

            //If customer selects option 4
            case 4:
            {
                //Enables customer to verify that they want to exit the program
                printf("Are you sure you want to exit?\nSelect 1 for YES\nSelect 2 for NO\n");
                scanf("%d", &exit);

                //Error check for character
                    while (getchar() != '\n')
                    {
                        scanf("%d", &exit);
                    }//end of while loop

                if (exit == 1)//If 1 is selected, program displays an exit message
                {
                    printf("HAVE A NICE DAY\n");
                    break;
                }
                else if (exit == 2)//if 2 is selected, reruns the program from the beginning
                {
                    option = 0;
                    break;
                }
            }//end of case 4

            //If customer selects a non-existent option
            default:
            {
                printf("PLEASE SELECT A VALID OPTION\n");
                option = 0;//reruns the program
            }//end of default

        }//end of switch
    } while (option != 4);//Makes the program end if customer selects option 4
    
    return 0;
}



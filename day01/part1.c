#include <stdio.h>
#include <stdbool.h>

int
main(void)
{
    FILE *fptr;
    int exp_lines = 200;
    int numbers[exp_lines];
    bool solution_found = false;
    int solution = 0;

    fptr = fopen("input.txt", "r");
    for (int i = 0; i < exp_lines; i++)
    {
        fscanf(fptr, "%d", &numbers[i]);
    }

    for (int i = 0; i < exp_lines; i++)
    {
        for (int j = 0; j < exp_lines; j++)
        {
            if (numbers[i] + numbers[j] == 2020)
            {
                solution = numbers[i] * numbers[j];
                solution_found = true;
                break;
            }
        }
        if (solution_found == true)
        {
            break;
        }
    }

    fclose(fptr);
    if (solution != 0)
    {
        printf("the solution is %d\n", solution);
    }
    else
    {
        printf("did not find a solution %d\n", solution);
    }
    return 0;
}

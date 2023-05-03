#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * infinite_while - Run an infinite while loop.
 *
 * Return: Always 0 Success.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Entry point of the program
 * Description: Creates five zombie processes.
 *
 * Return: Always 0 Success.
 */
int main(void)
{
	pid_t pid;
	int i = 0;

	while (i < 5)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			i++;
		}
		else
		{
			return (0);
		}
	}
	infinite_while();

	return (0);
}

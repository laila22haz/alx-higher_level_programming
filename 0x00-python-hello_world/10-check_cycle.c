#include <stdio.h>
#include <stdlib.h>
/**
*check_cycle - check if the list had a cycle
*@list : the first element
*
*Return : 1 (SUCCESS) 0 (OTHERWISE)
*/
int check_cycle(listint_t *list)
{
	listint_t *ptr == NULL;
	listint_t *temp == NULL;

	if (list == NULL)
		return (0);
	ptr = list;
	temp = list;

	while(ptr != NULL && temp != NULL && temp->next != NULL)
	{
		ptr = ptr->next;
		temp = temp->next->next;

		if (ptr == temp)
			return (1);
	}
	return (0);
}
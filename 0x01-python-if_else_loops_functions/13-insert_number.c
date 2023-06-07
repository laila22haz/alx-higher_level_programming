#include "lists.h"
#include <stdlib.h>
/**
* insert_node - Inserts a number into a sorted singly-linked list.
* @head: A pointer the head of the linked list
* @i: The number to insert
*
* Return: the address of the new node, or NULL if it failed
*/

listint_t *insert_node(listint_t **head, int i)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = i;

	if (node == NULL || node->n >= i)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < i)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
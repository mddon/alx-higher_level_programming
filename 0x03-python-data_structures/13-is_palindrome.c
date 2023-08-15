#include "lists.h"

int is_palindrome(listint_t **head);
listint_t *reverse_listint(listint_t **head);

/**
 * reverse_listint - This function reverses a singly-linked listint_t list.
 * @head: - Pointer to the starting node of the list that will be reversed.
 * Return: Pointer to the head of the reversed list.
 */

listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to the head of the linked list.
 *
 * Return: If the linked list is not a palindrome return 0.
 *         If the linked list is a palindrome return 1.
 */
int is_palindrome(listint_t **head)
{
 	listint_t *current, *rev, *mid;
 	size_t size = 0, index;

 	if (*head == NULL || (*head)->next == NULL)
	{ 
		return (1);
	}

	current = *head;
	while (current)
	{
		size++;
		current = current->next;
	}

	current = *head;
	for (index = 0; index < (size / 2) - 1; index++)
	{
		current = current->next;
	}
	if ((size % 2) == 0 && current->n != current->next->n)
	{
		return (0);
	}

	current = current->next->next;
	rev = reverse_listint(&current);
	mid = rev;

	current = *head;
	do
	{
		if (current->n != rev->n)
			return (0);
		current = current->next;
		rev = rev->next;
	} while (rev != NULL);
	reverse_listint(&mid);

	return (1);
}

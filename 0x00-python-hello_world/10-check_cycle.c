#include "lists."
/*
 * check_cycle - wether list has a cycle
 * @list: pointer to list
 *@Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *rabbit, *turtle;

	if (!list)
		return (0);

rabbit = list->next;
turtle = list;
	while (rabbit && turtle && rabbit->next)
	{
		if (rabbit == turtle)
			return (1);
		turtle = turtle->next;
		rabbit = rabbit->next->next;
	}
return (0);
}

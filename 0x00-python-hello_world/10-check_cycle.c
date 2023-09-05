#include "lists.h"
int check_cycle(listint_t *list)
{
listint_t *s, *f;

	if (!list)
		return (0);

s = list;
f = list->next;

	while(s && f && f->next)
	{
		if (s == f)
			{
				return (1);
			}
		s = s->next;
		f = f->next->next;
	}
return (0);
}

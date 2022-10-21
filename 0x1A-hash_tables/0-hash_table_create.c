#include "hash_tables.h"

/**
 * hash_table_create - Create a hash table
 * @size: size of hash table created
 * Return: pointer to the new hash table created
 */

hash_table_t *hash_table_create(unsigned long int size)
{
	hash_table_t *arr = malloc(size * sizeof(hash_table_t));

	if (arr == NULL)
	{
		return (NULL);
	}

	return (arr);
}

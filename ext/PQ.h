#pragma once
#define MAX_SIZE 1000000
#include <Python.h>

// Priority_Queue for C
typedef struct
{

    PyObject_HEAD
    int arr[MAX_SIZE];
    int size;

} Priority_Queue;

//helper C functions
void insertHeap(int *arr, int value, int *size);
int heapRemove(int *arr, int *size);

//insert into heap
PyObject *
Priority_Queue_insert(Priority_Queue *self, PyObject *args);

//extract min of heap
PyObject *
Priority_Queue_ExtractMin(Priority_Queue *self);

//peek the minimum / top of the heap
PyObject *
Priority_Queue_GetMin(Priority_Queue *self);

//returns the size of the heap
PyObject *
Priority_Queue_Size(Priority_Queue *self);

//returns True if size is 0, false otherwise
PyObject *
Priority_Queue_Empty(Priority_Queue *self);

//constructor for PQ
int Priority_Queue_init(Priority_Queue *self, PyObject *args, PyObject *kwds);

//destructor for PQ
void Priority_Queue_dealloc(Priority_Queue *self);

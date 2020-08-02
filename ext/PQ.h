#pragma once
#define MAX_SIZE 1000000
#include <Python.h>

// Node type to pair id to distance
typedef struct
{

    int distance;
    int id;

} Node;

// Priority_Queue for C
typedef struct
{

    PyObject_HEAD
        Node arr[MAX_SIZE];
    int node_locations[MAX_SIZE];
    int size;

} Priority_Queue;

//helper C functions
void insertHeap(Node *arr, int *node_locations, Node value, int *size);
Node heapRemove(Node *arr, int *node_locations, int *size);

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

PyObject *
Priority_Queue_Get_Distance(Priority_Queue *self, PyObject *args);

//decreases the distance for a particular node which is not the minimum node if necessary
//using the array to look up its position
PyObject *
Priority_Queue_Decrease_Key(Priority_Queue *self, PyObject *args);

//debugging method to print the priority queue to the screen
//along with its node_locations array
PyObject *
Priority_Queue_Print(Priority_Queue *self);

//print just the Node array
PyObject *
Priority_Queue_PrintArray(Priority_Queue *self);

//print just the node locations
PyObject *
Priority_Queue_PrintNodes(Priority_Queue *self);

//constructor for PQ
int Priority_Queue_init(Priority_Queue *self, PyObject *args, PyObject *kwds);

//destructor for PQ
void Priority_Queue_dealloc(Priority_Queue *self);

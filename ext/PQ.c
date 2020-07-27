#define PY_SSIZE_T_CLEAN
#define MAX_SIZE 1000000
#include "PQ.h"
#include <Python.h>

//the C methods for heap insertion, removal, and access.
void insertHeap(int *arr, int value, int *size)
{
    //do nothing if the maximum size has been reached
    if (*size == MAX_SIZE)
        return;

    arr[*size] = value;
    int childPos = *size;
    int parentPos = ((*size - 1) / 2);

    //"heapify" up if necessary
    while (parentPos >= 0 && arr[parentPos] > arr[childPos])
    {

        int temp = arr[parentPos];
        arr[parentPos] = arr[childPos];
        arr[childPos] = temp;

        //recalculate the positions for parents
        childPos = parentPos;
        parentPos = ((childPos - 1) / 2);
    }

    (*size)++;
}

int heapRemove(int *arr, int *size)
{
    //return -1 if the size is 0
    if (*size == 0)
        return -1;

    //the value to return (minimum value)
    int result = arr[0];

    int pos = 0;
    arr[pos] = arr[--(*size)];

    int child = 2 * pos + 1;

    while (child < *size && (arr[pos] > arr[child] || arr[pos] > arr[child + 1]))
    {

        //swap with first child
        if (arr[child] < arr[child + 1])
        {
            int temp = arr[pos];
            arr[pos] = arr[child];
            arr[child] = temp;

            //recalculate child and pos
            pos = child;
            child = 2 * pos + 1;
        }

        //swap with second child
        else
        {
            int temp = arr[pos];
            arr[pos] = arr[child + 1];
            arr[child + 1] = temp;

            //recalculate child and pos
            pos = child;
            child = 2 * pos + 1;
        }
    }

    return result;
}

//insert an element into the heap
PyObject *
Priority_Queue_insert(Priority_Queue *self, PyObject *args)
{
    int val;

    if (!PyArg_ParseTuple(args, "i", &val))
        return NULL;

    //insert the element to the heap and heapify if necessary
    insertHeap(self->arr, val, &(self->size));

    //does not return a type same as None in python
    return Py_None;
}

PyObject *
Priority_Queue_ExtractMin(Priority_Queue *self)
{
    int result;

    //remove the element from the heap and heapify if necessary
    result = heapRemove(self->arr, &(self->size));

    return Py_BuildValue("i", result);
}

// Access the minimum element from the priority queue
PyObject *
Priority_Queue_GetMin(Priority_Queue *self)
{
    //if empty just return a value of -1 as the minimum element
    //this is okay for our use case as a distance of -1 is not possible
    if (self->size == 0)
        return Py_BuildValue("i", -1);

    return Py_BuildValue("i", self->arr[0]);
}

//accessor for the size of the priority queue
PyObject *
Priority_Queue_Size(Priority_Queue *self)
{
    return Py_BuildValue("i", self->size);
}

//method to return true if emtpy and false otherwise
PyObject *
Priority_Queue_Empty(Priority_Queue *self)
{
    return self->size == 0 ? Py_True : Py_False;
}

//constructor for the object
int Priority_Queue_init(Priority_Queue *self, PyObject *args, PyObject *kwds)
{
    //set the initial size to 0
    self->size = 0;

    //indicate success
    return 0;
}

//destructor for the object
void Priority_Queue_dealloc(Priority_Queue *self)
{
    Py_TYPE(self)->tp_free((PyObject *)self);
}

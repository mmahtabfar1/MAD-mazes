#define PY_SSIZE_T_CLEAN
#define MAX_SIZE 1000000
#include "PQ.h"
#include <Python.h>

/*


Below is C code to create a min heap / Priority Queue for python.
Below is a description of how to use this type in python.

from ext import Priority_Queue

heap = Priority_Queue()

heap.insert(distance, node) -> None
heap.extract_min() -> returns a tuple with (distance, id) and remove from heap
heap.get_min() -> return a tuple with (distance, id) does not remove
heap.empty() -> returns True if empty False otherwise
heap.size() -> returns 0 if empty false otherwise
 
extract_min will return the minimum distance NOT the minimum ID.


*/

//the C methods for heap insertion, removal, and access.
void insertHeap(Node *arr, Node value, int *size)
{
    //do nothing if the maximum size has been reached
    if (*size == MAX_SIZE)
        return;

    arr[*size] = value;
    int childPos = *size;
    int parentPos = ((*size - 1) / 2);

    //"heapify" up if necessary
    while (parentPos >= 0 && arr[parentPos].distance > arr[childPos].distance)
    {

        Node temp = arr[parentPos];
        arr[parentPos] = arr[childPos];
        arr[childPos] = temp;

        //recalculate the positions for parents
        childPos = parentPos;
        parentPos = ((childPos - 1) / 2);
    }

    (*size)++;
}

Node heapRemove(Node *arr, int *size)
{
    //return  a tuple of (-1, -1) if the size is 0
    if (*size == 0)
    {
        Node temp;
        temp.distance = -1;
        temp.id = -1;

        return temp;
    }
        

    //the value to return (minimum value)
    Node result = arr[0];

    int pos = 0;
    arr[pos] = arr[--(*size)];

    int child = 2 * pos + 1;

    while (child < *size && (arr[pos].distance > arr[child].distance || arr[pos].distance > arr[child + 1].distance))
    {

        //swap with first child
        if (arr[child].distance < arr[child + 1].distance)
        {
            Node temp = arr[pos];
            arr[pos] = arr[child];
            arr[child] = temp;

            //recalculate child and pos
            pos = child;
            child = 2 * pos + 1;
        }

        //swap with second child
        else
        {
            Node temp = arr[pos];
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
    int distance;
    int id;

    if (!PyArg_ParseTuple(args, "ii", &distance, &id))
        return NULL;

    //the Node to insert
    Node temp;
    temp.distance = distance;
    temp.id = id;

    //insert the element to the heap and heapify if necessary
    insertHeap(self->arr, temp, &(self->size));

    //does not return a type same as None in python
    return Py_None;
}

PyObject *
Priority_Queue_ExtractMin(Priority_Queue *self)
{
    Node result;

    //remove the element from the heap and heapify if necessary
    result = heapRemove(self->arr, &(self->size));

    return Py_BuildValue("(ii)", result.distance, result.id);
}

// Access the minimum element from the priority queue
PyObject *
Priority_Queue_GetMin(Priority_Queue *self)
{
    //if empty just return a value of -1 as the minimum element
    //this is okay for our use case as a distance of -1 is not possible
    if (self->size == 0)
        return Py_BuildValue("i", -1);

    return Py_BuildValue("(ii)", self->arr[0].distance, self->arr[0].id);
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

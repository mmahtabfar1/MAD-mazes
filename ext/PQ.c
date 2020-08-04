#define PY_SSIZE_T_CLEAN
#define MAX_SIZE 1000000
#include "PQ.h"
#include <Python.h>

/*


Below is C code to create a min heap / Priority Queue for python.
Below is a description of how to use this type in python.

from ext import Priority_Queue

heap = Priority_Queue()

heap.insert(id, distance) -> None

heap.extract_min() -> returns a tuple with (id, distance) and remove from heap
^ extract_min will return the minimum distance NOT the minimum ID.

heap.get_min() -> return a tuple with (id, distance) does not remove
heap.empty() -> returns True if empty False otherwise
heap.size() -> returns 0 if empty false otherwise

heap.decrease_key(id, new_distance) -> None
^ this will decrease the distance of a node with a particular ID to the new distance

heap.print() -> will print the heap array with node locations for debuggin purposes
heap.print_array() -> prints just array
heap.print_nodes() -> prints just the node locations
 
 heap.get_distance(id) -> returns the distance associated with the node with the given ID.


*/

//the C methods for heap insertion, removal, and access.
void insertHeap(Node *arr, int *node_locations, Node value, int *size)
{
    //do nothing if the maximum size has been reached
    if (*size == MAX_SIZE)
        return;

    arr[*size] = value;
    node_locations[value.id] = *size;
    int childPos = *size;
    int parentPos = ((*size - 1) / 2);

    //"heapify" up if necessary
    while (parentPos >= 0 && arr[parentPos].distance > arr[childPos].distance)
    {
        //update node_locations to reflect this change
        node_locations[arr[parentPos].id] = childPos;
        node_locations[arr[childPos].id] = parentPos;

        Node temp = arr[parentPos];
        arr[parentPos] = arr[childPos];
        arr[childPos] = temp;

        //recalculate the positions for parents
        childPos = parentPos;
        parentPos = ((childPos - 1) / 2);
    }

    (*size)++;
}

Node heapRemove(Node *arr, int *node_locations, int *size)
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

    //heapify down if necessary
    while (child < *size && (arr[pos].distance > arr[child].distance || arr[pos].distance > arr[child + 1].distance))
    {

        //swap with first child
        // if left child is less than right child
        // then swap with left child.
        if (arr[child].distance < arr[child + 1].distance)
        {

            //update node_locations to reflect this change
            node_locations[arr[pos].id] = child;
            node_locations[arr[child].id] = pos;

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

            //update node_locations to reflect this change
            node_locations[arr[pos].id] = child + 1;
            node_locations[arr[child + 1].id] = pos;

            Node temp = arr[pos];
            arr[pos] = arr[child + 1];
            arr[child + 1] = temp;

            //recalculate child and pos
            pos = child + 1;
            child = 2 * pos + 1;
        }
    }

    return result;
}

void Decrease_Key(Node *arr, int *node_locations, int new_distance, int node_id)
{

    //change the distance of the node with that particular ID in O(1)
    arr[node_locations[node_id]].distance = new_distance;

    //heapify up if necessary in O(logn) time
    int childPos = node_locations[node_id];
    int parentPos = ((childPos - 1) / 2);

    while (parentPos >= 0 && arr[parentPos].distance > arr[childPos].distance)
    {

        //update node_locations to reflect this change
        node_locations[arr[parentPos].id] = childPos;
        node_locations[arr[childPos].id] = parentPos;

        Node temp = arr[parentPos];
        arr[parentPos] = arr[childPos];
        arr[childPos] = temp;

        //recalculate the positions for parents
        childPos = parentPos;
        parentPos = ((childPos - 1) / 2);
    }
}

//insert an element into the heap
PyObject *Priority_Queue_insert(Priority_Queue *self, PyObject *args)
{

    int id;
    int distance;

    if (!PyArg_ParseTuple(args, "ii", &id, &distance))
        return NULL;

    //the Node to insert
    Node temp;
    temp.distance = distance;
    temp.id = id;

    //insert the element to the heap and heapify if necessary
    insertHeap(self->arr, self->node_locations, temp, &(self->size));

    //does not return a type same as None in python
    Py_RETURN_NONE;
}

PyObject *
Priority_Queue_Get_Distance(Priority_Queue *self, PyObject *args)
{
    int id;

    if (!PyArg_ParseTuple(args, "i", &id))
        return NULL;

    return Py_BuildValue("i", self->arr[self->node_locations[id]]);
}

PyObject *
Priority_Queue_Decrease_Key(Priority_Queue *self, PyObject *args)
{
    int id;
    int new_distance;

    if (!PyArg_ParseTuple(args, "ii", &id, &new_distance))
        return NULL;

    Decrease_Key(self->arr, self->node_locations, new_distance, id);

    //does not return a type same as None in python
    Py_RETURN_NONE;
}

PyObject *
Priority_Queue_ExtractMin(Priority_Queue *self)
{
    Node result;

    //remove the element from the heap and heapify if necessary
    result = heapRemove(self->arr, self->node_locations, &(self->size));

    return Py_BuildValue("(ii)", result.id, result.distance);
}

// Access the minimum element from the priority queue
PyObject *
Priority_Queue_GetMin(Priority_Queue *self)
{
    //if empty just return a value of -1 as the minimum element
    //this is okay for our use case as a distance of -1 is not possible
    if (self->size == 0)
        return Py_BuildValue("i", -1);

    return Py_BuildValue("(ii)", self->arr[0].id, self->arr[0].distance);
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
    if (self->size == 0)
        Py_RETURN_TRUE;

    Py_RETURN_FALSE;
}

//debugging method to print the priority queue along with
// it's node_locations array to the screen
PyObject *
Priority_Queue_Print(Priority_Queue *self)
{
    printf("Priority_Queue:\n");
    //print start bracket
    printf("[");

    for (int i = 0; i < self->size - 1; i++)
    {
        printf("(%d, %d) ", self->arr[i].id, self->arr[i].distance);
    }

    //print end bracket and last element
    printf("(%d, %d)]\n", self->arr[self->size - 1].id, self->arr[self->size - 1].distance);

    printf("\nNode_locations:\n");

    for (int i = 0; i < self->size; i++)
    {
        printf("Node %d is locatd at index %d\n", self->arr[i].id, self->node_locations[self->arr[i].id]);
    }

    Py_RETURN_NONE;
}

//print just the Priority_Queue
PyObject *
Priority_Queue_PrintArray(Priority_Queue *self)
{

    printf("Priority_Queue:\n");
    //print start bracket
    printf("[");

    for (int i = 0; i < self->size - 1; i++)
    {
        printf("(%d, %d) ", self->arr[i].id, self->arr[i].distance);
    }

    //print end bracket and last element
    printf("(%d, %d)]\n", self->arr[self->size - 1].id, self->arr[self->size - 1].distance);

    Py_RETURN_NONE;
}

//print just the Node locations
PyObject *
Priority_Queue_PrintNodes(Priority_Queue *self)
{

    printf("\nNode_locations:\n");

    for (int i = 0; i < self->size; i++)
    {
        printf("Node %d is locatd at index %d\n", self->arr[i].id, self->node_locations[self->arr[i].id]);
    }

    Py_RETURN_NONE;
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

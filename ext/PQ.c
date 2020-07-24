#define PY_SSIZE_T_CLEAN
#define MAX_SIZE 1000000
#include <Python.h>

typedef struct
{
    PyObject_HEAD;
    int arr[MAX_SIZE];
    int size;

} Priority_Queue;

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
static PyObject *
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

static PyObject *
Priority_Queue_ExtractMin(Priority_Queue *self)
{
    int result;

    //remove the element from the heap and heapify if necessary
    result = heapRemove(self->arr, &(self->size));

    return Py_BuildValue("i", result);
}

// Access the minimum element from the priority queue
static PyObject *
Priority_Queue_GetMin(Priority_Queue *self)
{
    //if empty just return a value of -1 as the minimum element
    //this is okay for our use case as a distance of -1 is not possible
    if (self->size == 0)
        return Py_BuildValue("i", -1);

    return Py_BuildValue("i", self->arr[0]);
}

static PyObject *
Priority_Queue_Size(Priority_Queue *self)
{
    return Py_BuildValue("i", self->size);
}

//constructor for the object
static int
Priority_Queue_init(Priority_Queue *self, PyObject *args, PyObject *kwds)
{

    //set the initial size to 0
    self->size = 0;

    //indicate success
    return 0;
}

//destructor for the object
static void
Priority_Queue_dealloc(Priority_Queue *self)
{
    Py_TYPE(self)->tp_free((PyObject *)self);
}

//methods for the object
static PyMethodDef Priority_Queue_methods[] = {

    {"insert", (PyCFunction)Priority_Queue_insert, METH_VARARGS,
     "Insert a new integer into the heap"},

    {"extract_min", (PyCFunction)Priority_Queue_ExtractMin, METH_NOARGS,
     "Remove and return the minimum element from the heap"},

    {"get_min", (PyCFunction)Priority_Queue_GetMin, METH_NOARGS,
     "Return the minimum element in the heap"},

    {"size", (PyCFunction)Priority_Queue_Size, METH_NOARGS,
     "Return the current size of the heap"},

    {NULL}, //Sentinel
};

//This struct describes how the Priority Queue type beahves, it defines a set of flags
//and associated function pointers that the interpreter inspects when specific operations
//are requested
static PyTypeObject Priority_Queue_Type = {

    PyVarObject_HEAD_INIT(NULL, 0).tp_name = "PQ.Priority_Queue",
    .tp_doc = "Min Heap / Priority Queue",
    .tp_basicsize = sizeof(Priority_Queue),
    .tp_itemsize = 0,
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_new = PyType_GenericNew,
    .tp_init = (initproc)Priority_Queue_init,
    .tp_methods = Priority_Queue_methods,
    .tp_dealloc = (destructor)Priority_Queue_dealloc,

};

static PyModuleDef PQmodule = {

    PyModuleDef_HEAD_INIT,
    .m_name = "PQ",
    .m_doc = "Min_Heap implementation in C for python",
    .m_size = -1,

};

//initialization function
PyMODINIT_FUNC
PyInit_PQ(void)
{
    PyObject *m;
    if (PyType_Ready(&Priority_Queue_Type) < 0)
        return NULL;

    m = PyModule_Create(&PQmodule);
    if (m == NULL)
        return NULL;

    Py_INCREF(&Priority_Queue_Type);
    if (PyModule_AddObject(m, "Priority_Queue", (PyObject *)&Priority_Queue_Type) < 0)
    {
        Py_DECREF(&Priority_Queue_Type);
        Py_DECREF(m);
        return NULL;
    }

    return m;
}
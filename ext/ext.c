#include "PQ.h"
#include "Stack.h"
#include <Python.h>

//
//Stack
//
static PyMethodDef Stack_methods[] = {

    {"push", (PyCFunction)Stack_push, METH_VARARGS,
     "Insert an integer on the top of the stack"},

    {"pop", (PyCFunction)Stack_pop, METH_NOARGS,
     "Pop the top of the stack"},

    {"peek", (PyCFunction)Stack_peek, METH_NOARGS,
     "Peek the top of the stack"},

    {"size", (PyCFunction)Stack_size, METH_NOARGS,
     "Return the size of the stack"},

    {"empty", (PyCFunction)Stack_empty, METH_NOARGS,
     "Returns True if empty False otherwise"},

    {NULL}, //Sentinel

};

//describes how the Stack type should behave, it defines sets of flags
//and associated funciton pointers that the interpreter will use when specific
//operations are requested
static PyTypeObject Stack_Type = {

    PyVarObject_HEAD_INIT(NULL, 0).tp_name = "ext.Stack",
    .tp_doc = "Integer Stack",
    .tp_basicsize = sizeof(Stack),
    .tp_itemsize = 0,
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_new = PyType_GenericNew,
    .tp_init = (initproc)Stack_init,
    .tp_methods = Stack_methods,
    .tp_dealloc = (destructor)Stack_dealloc,

};

//
//Priority Queue
//
static PyMethodDef Priority_Queue_methods[] = {

    {"insert", (PyCFunction)Priority_Queue_insert, METH_VARARGS,
     "Insert a new integer into the heap"},

    {"extract_min", (PyCFunction)Priority_Queue_ExtractMin, METH_NOARGS,
     "Remove and return the minimum element from the heap"},

    {"get_min", (PyCFunction)Priority_Queue_GetMin, METH_NOARGS,
     "Return the minimum element in the heap"},

    {"size", (PyCFunction)Priority_Queue_Size, METH_NOARGS,
     "Return the current size of the heap"},

    {"empty", (PyCFunction)Priority_Queue_Empty, METH_NOARGS,
     "Returns boolean whether or not heap is empty"},

    {"get_distance", (PyCFunction)Priority_Queue_Get_Distance, METH_VARARGS,
     "Returns the distance associated with the given node ID"},

    {"decrease_key", (PyCFunction)Priority_Queue_Decrease_Key, METH_VARARGS,
     "Decrease the distance of a particular node"},

    {"print", (PyCFunction)Priority_Queue_Print, METH_NOARGS,
     "Prints the queue to the screen for debugging purposes"},

    {"print_array", (PyCFunction)Priority_Queue_PrintArray, METH_NOARGS,
     "Prints out just the Node array to the screen"},

    {"print_nodes", (PyCFunction)Priority_Queue_PrintNodes, METH_NOARGS,
     "Prints out just the Node locations to the screen"},

    {NULL}, //Sentinel

};

//This struct describes how the Priority Queue type beahves, it defines a set of flags
//and associated function pointers that the interpreter inspects when specific operations
//are requested
static PyTypeObject Priority_Queue_Type = {

    PyVarObject_HEAD_INIT(NULL, 0).tp_name = "ext.Priority_Queue",
    .tp_doc = "Min Heap / Priority Queue",
    .tp_basicsize = sizeof(Priority_Queue),
    .tp_itemsize = 0,
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_new = PyType_GenericNew,
    .tp_init = (initproc)Priority_Queue_init,
    .tp_methods = Priority_Queue_methods,
    .tp_dealloc = (destructor)Priority_Queue_dealloc,

};

//
// ext module
//
static PyModuleDef extmodule = {

    PyModuleDef_HEAD_INIT,
    .m_name = "ext",
    .m_doc = "extension module for data structures",
    .m_size = -1,

};

//initialization function
PyMODINIT_FUNC
PyInit_ext(void)
{
    PyObject *m;
    if (PyType_Ready(&Priority_Queue_Type) < 0)
    {
        return NULL;
    }

    if (PyType_Ready(&Stack_Type) < 0)
    {
        return NULL;
    }

    m = PyModule_Create(&extmodule);
    if (m == NULL)
        return NULL;

    Py_INCREF(&Priority_Queue_Type);
    Py_INCREF(&Stack_Type);

    if (PyModule_AddObject(m, "Priority_Queue", (PyObject *)&Priority_Queue_Type) < 0)
    {
        Py_DECREF(&Priority_Queue_Type);
        Py_DECREF(m);
        return NULL;
    }

    if (PyModule_AddObject(m, "Stack", (PyObject *)&Stack_Type) < 0)
    {
        Py_DECREF(&Stack_Type);
        Py_DECREF(m);
        return NULL;
    }

    return m;
}

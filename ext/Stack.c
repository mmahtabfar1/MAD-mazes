#define PY_SSIZE_T_CLEAN
#define MAX_SIZE 1000000
#include "Stack.h"
#include <Python.h>

//Stack insert method
PyObject *
Stack_push(Stack *self, PyObject *args)
{
    int val;

    if (!PyArg_ParseTuple(args, "i", &val))
        return NULL;

    //if the stack is full do not do anything
    if (self->size == MAX_SIZE)
        return Py_None;

    //push value onto the stack
    self->arr[self->size++] = val;

    //return python none object
    return Py_None;
}

//Stack pop method
PyObject *
Stack_pop(Stack *self)
{
    if (self->size != 0)
        self->size--;

    return Py_None;
}

//Stack peek method
PyObject *
Stack_peek(Stack *self)
{
    //this will be considered an error since a value of -1 will never be on the stack
    if (self->size == 0)
        return Py_BuildValue("i", -1);

    return Py_BuildValue("i", self->arr[self->size - 1]);
}

//access the size of the stack
PyObject *
Stack_size(Stack *self)
{
    return Py_BuildValue("i", self->size);
}

//returns true if empty and false otherwise
PyObject *
Stack_empty(Stack *self)
{
    return self->size == 0 ? Py_True : Py_False;
}

//constructor for the Stack
int Stack_init(Stack *self, PyObject *args, PyObject *kwds)
{
    //set the initial size to 0
    self->size = 0;

    //indicate success
    return 0;
}

//destructor for the stack
void Stack_dealloc(Stack *self)
{
    Py_TYPE(self)->tp_free((PyObject *)self);
}

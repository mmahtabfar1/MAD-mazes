#define PY_SSIZE_T_CLEAN
#define MAX_SIZE 1000000
#include "Stack.h"
#include <Python.h>

/*


Below is C code to create an integer stack in Python
Below is a description of how to use this type in python

from ext import Stack

stack = Stack()

stack.push(val) -> will push val onto the stack
stack.pop() -> returns None!! will remove top of stack
stack.peek() -> returns int equal to the top of the stack
stack.empty() -> returns True if empty False otherwise
stack.size() -> returns the size of the stack


*/

//Stack insert method
PyObject *
Stack_push(Stack *self, PyObject *args)
{
    int val;

    if (!PyArg_ParseTuple(args, "i", &val))
        return NULL;

    //if the stack is full do not do anything
    if (self->size == MAX_SIZE)
        Py_RETURN_NONE;

    //push value onto the stack
    self->arr[self->size++] = val;

    //return python none object
    Py_RETURN_NONE;
}

//Stack pop method
PyObject *
Stack_pop(Stack *self)
{
    if (self->size != 0)
        self->size--;

    Py_RETURN_NONE;
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
    if (self->size == 0)
        Py_RETURN_TRUE;

    Py_RETURN_FALSE;
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

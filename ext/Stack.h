#pragma once
#define MAX_SIZE 1000000
#include <Python.h>

//stack type for C
typedef struct
{

    PyObject_HEAD
    int arr[MAX_SIZE];
    int size;

} Stack;

//stack insert method
PyObject *
Stack_push(Stack *self, PyObject *args);

//Stack pop method
PyObject *
Stack_pop(Stack *self);

//Stack peek method
PyObject *
Stack_peek(Stack *self);

//access the size of the stack
PyObject *
Stack_size(Stack *self);

//returns true if empty and false otherwise
PyObject *
Stack_empty(Stack *self);

//constructor for the stack
int Stack_init(Stack *self, PyObject *args, PyObject *kwds);

//destructor for the stack
void Stack_dealloc(Stack *self);

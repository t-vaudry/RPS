#include "pyInterface.h"
//void** CallPy(char* scriptName, char* functionName, PyStringObject* botFileName, PyCodeObject* codeArg, PyDictObject* dictArgs, PyStringObject* moveInput);

PyCodeObject* codeResult = NULL;
PyDictObject* dictResult = NULL;
char* scriptName = "pyfunc";
char* compileFuncName = "compileString";
char* executeFuncName = "executeCode";

//TO DO -> CREATE A BOT STRUCTURE, WITH SCRIPT NAME, function name, code_obj, dictionary
RPSBot* PlayBotRound(RPSBot* pCurrentBot, int move)
{
	PyStringObject* moveInput = NULL;
	if (move == 0)
	{
		moveInput = PyString_FromString("R");
	}
	else if (move == 1)
	{
		moveInput = PyString_FromString("P");
	}
	else if (move == 2)
	{
		moveInput = PyString_FromString("S");
	}
	else
	{
		moveInput = PyString_FromString("");
	}

	
	void** pReturnValues = (void**)malloc(3 * sizeof(void*));
	pReturnValues = CallPy(scriptName, executeFuncName, NULL, pCurrentBot->codeArg, pCurrentBot->dictArg, moveInput);
	pCurrentBot->codeArg = (PyCodeObject*)pReturnValues[0];
	pCurrentBot->dictArg = (PyDictObject*)pReturnValues[1];

	PyStringObject* outputMove = (PyStringObject*) pReturnValues[2];
	char* outputMoveString = PyString_AsString(outputMove);
	//printf("The most recent played move is");
	//printf(outputMoveString);
	//printf("\n");
	if (outputMoveString[0] == 'R')
	{
		pCurrentBot->outputMove = 0;
	}
	else if (outputMoveString[0] == 'P')
	{
		pCurrentBot->outputMove = 1;
	}
	else
	{
		pCurrentBot->outputMove = 2;
	}

	return pCurrentBot;
}

RPSBot* CompileBot(char* botFileNameString)
{
	PyStringObject* botFileName = PyString_FromString(botFileNameString);
	void** pReturnValues = (void**)malloc(3 * sizeof(void*));
	pReturnValues = CallPy(scriptName, compileFuncName, botFileName, NULL, NULL, NULL);


	RPSBot* pNewBot = (RPSBot*)malloc(sizeof(RPSBot));
	pNewBot->codeArg = (PyCodeObject*)pReturnValues[0];
	pNewBot->dictArg = (PyDictObject*)pReturnValues[1];
	pNewBot->fitness = 0;

	return pNewBot;
}

void** CallPy(char* scriptName, char* functionName, PyStringObject* botFileName, PyCodeObject* codeArg, PyDictObject* dictArg, PyStringObject* moveInput)
{
    PyObject *pScriptName, *pModule, *pFunc;
	PyObject *pReturnValue = NULL;
	void** pReturnValues = (void**)malloc(3 * sizeof(void*));
    PyObject *pArgs = NULL;

    //Py_Initialize();


    pScriptName = PyString_FromString(scriptName);

    pModule = PyImport_Import(pScriptName);



    Py_DECREF(pScriptName);



    if (pModule != NULL) {
        pFunc = PyObject_GetAttrString(pModule, functionName);

        if (pFunc && PyCallable_Check(pFunc)) {

        	if (strcmp(functionName,"compileString")==0)
        	{
        		pArgs = PyTuple_New(1);
        		PyTuple_SetItem(pArgs, 0, botFileName);
        	}
        	else
        	{
        		pArgs = PyTuple_New(3);
        		PyTuple_SetItem(pArgs, 0, codeArg);
        		PyTuple_SetItem(pArgs, 1, dictArg);
        		PyTuple_SetItem(pArgs, 2, moveInput);

        	}

			Py_XDECREF(pReturnValue);
            pReturnValue = PyObject_CallObject(pFunc, pArgs); //return object
            
			Py_XDECREF(pArgs);
			if (strcmp(functionName, "compileString") == 0)
			{
				//Py_XDECREF(botFileName);
			}
			else
			{
				//Py_XDECREF(codeArg);
				//Py_XDECREF(dictArg);
				//Py_XDECREF(moveInput);
			}
			


            int numReturnValues;
            if (pReturnValue != NULL)
            {
            	numReturnValues = PyList_Size(pReturnValue);
            	//printf("NUM RV %d",numReturnValues);
            	codeResult = (PyCodeObject*)PyList_GetItem(pReturnValue,0);
            	dictResult = (PyDictObject*)PyList_GetItem(pReturnValue,1);
            	pReturnValues[1] = (void*)dictResult;

            	//if (PyCode_Check(codeResult) == 1) //if it is code object
				//{	
					pReturnValues[0] = (void*)codeResult;
				//}

            	if (numReturnValues == 3)
            	{
            		pReturnValues[2] = (void*)(PyStringObject*)PyList_GetItem(pReturnValue,2);
            	}

               // Py_DECREF(pReturnValue);
            }
            else
            {
			   Py_DECREF(pFunc);
			   Py_DECREF(pModule);
			   PyErr_Print();
			   fprintf(stderr,"Call failed\n");
            }
        }

        Py_XDECREF(pFunc);
        Py_DECREF(pModule);
    }

    else
    {
        PyErr_Print();
        fprintf(stderr, "Failed to load ");
    }
    //Py_Finalize();



    return pReturnValues;
}


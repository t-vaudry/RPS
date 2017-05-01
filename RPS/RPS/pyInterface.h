#ifdef _DEBUG
#undef _DEBUG
#include <Python.h>
#define _DEBUG
#else
#include <Python.h>
#endif

typedef struct RPSBot
{
	PyCodeObject* codeArg;
	PyDictObject* dictArg;
	int outputMove;
	float fitness;
}RPSBot;

RPSBot* CompileBot(char* botFileNameString);
RPSBot* PlayBotRound(RPSBot* pCurrentBot, int move);
void** CallPy(char* scriptName, char* functionName, PyStringObject* botFileName, PyCodeObject* codeArg, PyDictObject* dictArg, PyStringObject* moveInput);
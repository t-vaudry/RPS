#pragma once

#include <fstream>

#ifndef __ANALYTICS_H__
#define __ANALYTICS_H__

#define MAX_BUFFER 10000

using namespace std;

struct Analytics {
    ofstream mOutput;
    char* mPath;

    Analytics(char* path)
    {
        mPath = path;
    }
    void LogAnalytics(float value, char* filename);
};

void Analytics::LogAnalytics(float value, char* filename)
{
    char* externalPath;
    strncpy_s(externalPath, MAX_BUFFER, mPath, MAX_BUFFER);
    strncat_s(externalPath, MAX_BUFFER, filename, MAX_BUFFER);
    mOutput.open(externalPath);
    mOutput << value << ",";
    mOutput.close();
}

#endif // __ANALYTICS_H__
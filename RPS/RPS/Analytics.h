#pragma once

#include <fstream>

#ifndef __ANALYTICS_H__
#define __ANALYTICS_H__

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
    strcpy(externalPath, mPath);
    strcat(externalPath, filename);
    mOutput.open(externalPath);
    mOutput << value << ",";
    mOutput.close();
}

#endif __ANALYTICS_H__
#pragma once
#include <vector>
#include "Individual.h"

using namespace std;

struct Library {
    vector<Individual*> library;

    void Add(Individual* champion)
    {
        library.push_back(champion);
    }
};

static Library gLibrary;

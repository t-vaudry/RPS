#pragma once
#include <vector>
#include "Individual.h"
#include "Constants.h"

using namespace std;

struct History {
    vector< pair<MOVE, MOVE> > mHistory;

    void Add(MOVE one, MOVE two)
    {
        if (!(mHistory.size() < MAX_HISTORY_SAVED))
        {
            mHistory.erase(mHistory.begin());
        }

        mHistory.push_back(make_pair(one, two));
    }

    bool Empty()
    {
        return mHistory.empty();
    }

    MOVE GetLastMove()
    {
        return mHistory.back().first;
    }

    int GetSize()
    {
        return mHistory.size();
    }

    pair<MOVE, MOVE> operator[](int index)
    {
        return mHistory[mHistory.size() - 1 - index];
    }
};

static History gHistory;

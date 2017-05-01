#pragma once
#include <vector>
#include "Individual.h"
#include "Constants.h"

using namespace std;

struct History {
    vector< pair<MOVE, MOVE> > mHistory;

    void Add(MOVE one, MOVE two) {
        if (!(mHistory.size() < MAX_HISTORY_SAVED))
        {
            mHistory.erase(mHistory.begin());
        }

        mHistory.push_back(make_pair(one, two));
    }

    MOVE GetLastMove() {
        return mHistory.back().first;
    }
};

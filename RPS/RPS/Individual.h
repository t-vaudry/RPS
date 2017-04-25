#pragma once

#include <iostream>
#include <vector>

#include "Condition.h"

using namespace std;

typedef enum
{
    R,
    P,
    S
} MOVE; 

struct Rule
{
private:
    vector<CONDITION> mConditions;
    MOVE mMove;
    int mScore; //Based on number of conditions
    int mPoints; //Based on how often used/successful
};

class Individual
{
private:
    vector<Rule> mRules;
    float mFitness;
    bool mIsPlayerOne;
    MOVE mDefaultMove;
    MOVE mNextMove;
    Rule* mRulePlayed;
    MOVE mPlayedMoves[10];
    float mAverageScore;
    float mAverageRulePoints;
    int mID;

    static int mIDCounter;
public:
    Individual();
    ~Individual();
};


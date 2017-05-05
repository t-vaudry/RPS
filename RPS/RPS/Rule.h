#pragma once
#include <vector>

#ifndef __RULE_H__
#define __RULE_H__

using namespace std;

typedef enum {
    W, // WIN
    L, // LOSS
    D, // DRAW
    X  // DON'T CARE
} OUTCOME;

typedef enum
{
    R, // ROCK
    P, // PAPER
    S, // SCISSORS
    NO // NO MOVE
} MOVE;

OUTCOME DetermineOutcome(MOVE one, MOVE two);

struct Condition
{
public:
    OUTCOME mOutcome;

    Condition(bool oneConditionOnly)
    {
        mOutcome = oneConditionOnly ? static_cast<OUTCOME>(rand() % 3) : static_cast<OUTCOME>(rand() % 4);
    }
    Condition(MOVE one, MOVE two)
    {
        mOutcome = DetermineOutcome(one, two);
    }
};

class Rule
{
private:
    vector<Condition> mConditions;
    int mAction;    // +1 : play what would win, 0 : play the same, -1 : play what would lose?
    int mLocation;  // Location in history to use for reference
    int mScore;     // Based on number of conditions
    int mTimesUsed; // Based on how often used/successful
    int mTimesWon;  // Based on how often successful

public:
    Rule(bool oneConditionOnly = true);

    bool IsRuleSatisfied(int turn = 0);
    bool IsRuleSatisfied(Rule& rule);

    MOVE GetNextMove();

    void AddCondition();
    void ChangeAction();
    void ChangeLocation();
    void ModifyCondition(int index);

    static Rule GenerateRandomRule();

    static float GetGeneticDistanceBetweenRules(Rule& rule1, Rule& rule2);

    inline int GetAction() { return mAction; }
    inline int GetLocation() { return mLocation; }
    inline Condition GetConditionAt(int index) { return mConditions[index]; }
    inline int GetConditionsSize() { return mConditions.size(); }
    inline int GetScore() { return mScore; }
    inline int GetTimesUsed() { return mTimesUsed; }
    inline int GetTimesWon() { return mTimesWon; }

    inline void IncrementTimesUsed() { mTimesUsed++; }
    inline void IncrementTimesWon() { mTimesWon++; }
};

#endif // __RULE_H__

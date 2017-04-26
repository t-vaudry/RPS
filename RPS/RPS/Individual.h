#pragma once

#include <iostream>
#include <vector>

#include "Condition.h"

using namespace std;

typedef enum
{
    Add,
    Modify
} MUTATIONTYPE;

typedef enum
{
    ModifyCondition,
    AddCondition,
    ChangeAction
} MODIFICATIONTYPE;

typedef enum
{
    R,
    P,
    S
} MOVE; 

struct Rule
{
    //TODO ANITA: public or make accessors?
public:
    vector<Condition> mConditions;
    MOVE mMove;
    int mScore; //Based on number of conditions
    int mPoints; //Based on how often used/successful

public:
    //TODO ANITA: Do we need all 3? We probably don't ever need to pass conditions
    static bool IsRuleSatisfied(Rule& rule);
    static bool IsRuleSatisfied(Rule& rule, int turn = 0); //Could replace the basic version
    static bool IsRuleSatisfied(Rule& rule, vector<Condition>& conditions);

    static Rule GenerateRandomRule(bool oneConditionOnly = false);

    inline int GetRuleScore() { return mScore; }
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
    Individual(bool isPlayerOne);
    Individual(Individual& parent, bool mutate);

    void MutatePlayer(MUTATIONTYPE mutationBaseType);

    void DeterminePastPlayedMoves();
    void DetermineInitialFitness();

    void UpdateNextMove();
    void UpdateFitness();
    void UpdateAverageScore();
    void UpdateAverageRulePoints();

    float GetWinningRatio();

    float GetGeneticDistanceTo(const Individual* otherInd);
    float GetSemanticDistanceTo(const Individual* otherInd);

    //Overloaded operators
    inline double operator()() { return mFitness; }
    inline bool operator< (const Individual& otherInd) const { return mFitness < otherInd.mFitness; }
    inline bool operator> (const Individual& otherInd) const { return mFitness > otherInd.mFitness; }

    //Getters
    inline float GetFitness() const { return mFitness; }
    ~Individual();
};

struct less_than_key
{
    inline bool operator() (const Individual* ind1, const Individual* ind2)
    {
        return (ind1->GetFitness() < ind2->GetFitness());
    }
};


#pragma once

#ifndef __INDIVIDUAL_H__
#define __INDIVIDUAL_H__

#include <iostream>
#include <vector>

#include "Rule.h"

using namespace std;

typedef enum
{
    Add,
    Modify
} MUTATION_TYPE;

typedef enum
{
    ModifyCondition,
    AddCondition,
    ChangeAction,
    ChangeLocation
} MODIFICATION_TYPE;

class Individual
{
private:
    vector<Rule> mRules;
    float mFitness;
    MOVE mDefaultMove;
    MOVE mNextMove;
    Rule* mRulePlayed;
    MOVE mPlayedMoves[10];
    float mAverageScore;
    float mAverageRulePoints;
    int mID;

    static int sIDCounter;
    static const float sMutationParameters[2];
    static const float sModificationParameters[4];
public:
    Individual();
    Individual(Individual& parent, bool mutate);

    void MutatePlayer(MUTATION_TYPE mutationBaseType);

    inline void AddRule(Rule rule) { mRules.push_back(rule); }

    void DeterminePastPlayedMoves();
    void DetermineInitialFitness();

    void UpdateNextMove();
    void UpdateFitness();
    void UpdateAverageScore();
    void UpdateAverageRulePoints();

    float GetWinningRatio();

    float GetGeneticDistanceTo(Individual* otherInd);
    float GetSemanticDistanceTo(Individual* otherInd);

    //Overloaded operators
    inline double operator() () { return mFitness; }
    inline bool operator< (const Individual& otherInd) const { return mFitness < otherInd.mFitness; }
    inline bool operator> (const Individual& otherInd) const { return mFitness > otherInd.mFitness; }

    //Getters
    inline float GetFitness() const { return mFitness; }
    inline float GetAverageScore() const { return mAverageScore; }
    inline float GetAverageRulePoints() const { return mAverageRulePoints; }
    inline MOVE GetNextMove() const { return mNextMove; }
    inline float GetNumberOfRules() const { return mRules.size(); }
    inline Rule GetRule(int index) const { return mRules[index]; }

    inline void ClearRules() { mRules.clear(); }
    ~Individual();
};

struct LessThanKey
{
    inline bool operator() (const Individual* ind1, const Individual* ind2)
    {
        return (ind1->GetFitness() < ind2->GetFitness());
    }
};

#endif // __INDIVIDUAL_H__
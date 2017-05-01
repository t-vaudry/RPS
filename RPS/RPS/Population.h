#pragma once

#ifndef __POPULATION_H__
#define __POPULATION_H__

#include <vector>
#include <algorithm>
#include <assert.h>
#include "Individual.h"
#include "Constants.h"

#define MUTATION true

using namespace std;

typedef enum {
    MUTATE,
    CROSSOVER,
    CLONE
} EVOLUTION;

class Population
{
public:
    Population(int size);
    ~Population();

    void Evolve();
    void SwitchChampion();

    void UpdateAverageFitness();
    void UpdateFitness();
    void UpdateNextMoves();

    // Getters
    float GetAverageAccuracyOfRules();
    float GetAveragePointsOfRules();
    float GetAverageNumberOfRules();
    inline Individual* GetChampion() { return mChampion; }
    inline float GetChampionFitness() { return mChampion->GetFitness(); }
    inline MOVE GetChampionNextMove() { return mChampion->GetNextMove(); }

private:
    vector<Individual*> mIndividuals;
    Individual* mChampion;
    float mAverageFitness;
    const int mSize;

    vector<Individual*> Crossover(Individual* father, Individual* mother);
    vector<Individual*> Crowd(vector<Individual*> children, vector<Individual*> parents);

    static const float sEvolutionParameters[3];
};

#endif // __POPULATION_H__
#pragma once
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
    inline Individual* GetChampion();
    inline float GetChampionFitness();
    inline MOVE GetChampionNextMove();

private:
    vector<Individual*> mIndividuals;
    Individual* mChampion;
    float mAverageFitness;
    const int mSize;

    vector<Individual*> Crossover(Individual* father, Individual* mother);
    vector<Individual*> Crowd(vector<Individual*> children, vector<Individual*> parents);

    static const float sEvolutionParameters[3];
};
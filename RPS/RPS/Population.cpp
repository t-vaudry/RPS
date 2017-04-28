#include "Population.h"

const float Population::sEvolutionParameters[3] = { 1.0f, 1.0f, 1.0f };

Population::Population(int size) : mSize(size) {
    for (int i = 0; i < mSize; i++) {
        mIndividuals.push_back(new Individual);
    }

    mChampion = mIndividuals[rand() % mSize - 1];
    mAverageFitness = 0.0f;
}

Population::~Population() {
    if (mChampion) {
        mChampion = NULL;
    }

    if (!mIndividuals.empty()) {
        mIndividuals.clear();
    }
}

float Population::AverageAccuracyOfRules() {
    float sumRules = 0.0f;

    for (int i = 0; i < mSize; i++) {
        sumRules += mIndividuals[i]->GetAverageScore();
    }

    return sumRules / (float) mSize;
}

float Population::AveragePointsOfRules() {
    float sumPoints = 0.0f;

    for (int i = 0; i < mSize; i++) {
        mIndividuals[i]->UpdateAverageRulePoints();
        sumPoints += mIndividuals[i]->GetAverageRulePoints();
    }

    return sumPoints / (float) mSize;
}

float Population::AverageNumberOfRules() {
    float numRules = 0.0f;

    for (int i = 0; i < mSize; i++) {
        numRules += mIndividuals[i]->GetNumberOfRules();
    }

    return numRules / (float) mSize;
}

vector<Individual*> Population::Crossover(Individual* father, Individual* mother) {
    vector<Individual*> children;
    vector<Individual*> parents;

    for (int i = 0; i < 2; i++) {
        children.push_back(new Individual);
        children[i]->ClearRules();
    }

    float denominator = mother->GetFitness() + father->GetFitness() + 2;
    float numerator = mother->GetFitness() + 1;
    float motherRelativeFitness = 0.0f;

    if (denominator != 0) {
        motherRelativeFitness = numerator / denominator;
    }

    float random = 0.0f;
    int largestNumOfRules = mother->GetRulesSize() > father->GetRulesSize() ? mother->GetRulesSize() : father->GetRulesSize();

    for (int k = 0; k < 2; k++) {
        for (int i = 0; i < largestNumOfRules; i++) {
            random = static_cast <float> (rand()) / static_cast <float> (RAND_MAX);
            if (random < motherRelativeFitness) {
                if (mother->GetRulesSize() > i) {
                    children[k]->PushBackRule(mother->GetRule(i));
                }
            }
            else {
                if (father->GetRulesSize() > i) {
                    children[k]->PushBackRule(father->GetRule(i));
                }
            }
        }

        if (children[k]->GetRulesSize() == 0) {
            // THOMAS: Do we want to randomly assign a rule from a parent? Why not random rule?
            children[k]->PushBackRule(mother->GetRule(rand() % mother->getRulesSize() - 1));
        }
    }

    parents.push_back(mother);
    parents.push_back(father);

    return Crowd(children, parents);

}

vector<Individual*> Population::Crowd(vector<Individual*> children, vector<Individual*> parents) {
    vector<Individual*> keepers;
    int parentToTake = 0;

    // Genetic Distance
    float distance = children[0]->GetGeneticDistanceTo(parents[0]);
    if (children[0]->GetGeneticDistanceTo(parents[1]) < distance) {
        parentToTake = 1;
    }

    keepers.push_back((children[0]->GetFitness() > parents[parentToTake]->GetFitness()) ? children[0] : parents[parentToTake]);
    keepers.push_back((children[1]->GetFitness() > parents[!parentToTake]->GetFitness()) ? children[1] : parents[!parentToTake]);

    return keepers;
}

void Population::Evolve() { // TODO: maintain diversity
    vector<Individual*> parents;

    SwitchChampion();
    parents.push_back(mChampion); // Pass the most fit individual
    mIndividuals.erase(mIndividuals.begin() + mIndividuals.size() - 1);

    while (parents.size() < mSize * PARENT_SIZE - 1) {
        int indexSelectedParent;
        Individual* fittestPlayer;

        for (int i = 0; i < 3; i++) {
            int random = rand() % mSize - 1;
            Individual* tempPlayer = mIndividuals[random];

            if (fittestPlayer == NULL) {
                fittestPlayer = tempPlayer;
                indexSelectedParent = random;
            }
            else if (abs(fittestPlayer->GetFitness() - tempPlayer->GetFitness()) < 0.0001) {
                if (tempPlayer->GetAverageScore() > fittestPlayer->GetAverageScore()) {
                    fittestPlayer = tempPlayer;
                    indexSelectedParent = random;
                }
            }
            else if (tempPlayer->GetFitness() > fittestPlayer->GetFitness()) {
                fittestPlayer = tempPlayer;
                indexSelectedParent = random;
            }
        }

        // TODO: Remove the two players that lost
        parents.push_back(fittestPlayer);
        mIndividuals.erase(mIndividuals.begin() + indexSelectedParent);
    }

    vector<Individual*> offspring;
    for (int j = 0; j < 10 * CHILD_SIZE / PARENT_SIZE; j++) {
        for (int i = 0; i < mSize * PARENT_SIZE - 1; i++) {
            Individual* tempIndiv;
            Individual* tempIndiv2;

            EVOLUTION evolutionType;
            float evolve = (float)rand() / (float)RAND_MAX;
            float temp = 0.0f;

            for (int k = 0; k < 3; k++) {
                temp += sEvolutionParameters[k];
                if (evolve <= temp) {
                    evolutionType = static_cast<EVOLUTION>(k);
                    break;
                }
            }

            switch (evolutionType) {
            case MUTATE:
            {

            }
            case CROSSOVER:
            {}
            case CLONE:
            {}
            }
        }
    }

    sort(begin(mIndividuals), end(mIndividuals), LessThanKey());

    vector<Individual*> newPopulation;
    for (int i = 0; i < mSize; i++) {
        newPopulation.push_back(offspring[mSize * PARENT_SIZE - i - 1]);
    }

    mIndividuals = newPopulation;
    SwitchChampion();


}

void Population::SwitchChampion() {
    sort(begin(mIndividuals), end(mIndividuals), LessThanKey());
    mChampion = mIndividuals.back();
}

void Population::UpdateAverageFitness() {
    float sumFitness = 0.0f;

    for (int i = 0; i < mSize; i++) {
        sumFitness += mIndividuals[i]->GetFitness();
    }

    mAverageFitness = sumFitness / (float) mSize;
}

void Population::UpdateFitness() {
    for (int i = 0; i < mSize; i++) {
        mIndividuals[i]->UpdateFitness();
    }
}

void Population::UpdateNextMoves() {
    for (int i = 0; i < mSize; i++) {
        mIndividuals[i]->UpdateNextMove();
    }
}

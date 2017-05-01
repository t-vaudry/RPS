#include "Population.h"

const float Population::sEvolutionParameters[3] = { 1.0f, 1.0f, 1.0f };

Population::Population(int size) : mSize(size)
{
    for (int i = 0; i < mSize; i++)
    {
        mIndividuals.push_back(new Individual);
    }

    mChampion = mIndividuals[rand() % mSize - 1];
    mAverageFitness = 0.0f;
}

Population::~Population()
{
    if (mChampion)
    {
        mChampion = NULL;
    }

    if (!mIndividuals.empty())
    {
        mIndividuals.clear();
    }
}

vector<Individual*> Population::Crossover(Individual* father, Individual* mother)
{
    vector<Individual*> children;
    vector<Individual*> parents;

    for (int i = 0; i < 2; i++)
    {
        children.push_back(new Individual);
        children[i]->ClearRules();
    }

    float denominator = mother->GetFitness() + father->GetFitness() + 2;
    float numerator = mother->GetFitness() + 1;
    float motherRelativeFitness = 0.0f;

    if (denominator != 0)
    {
        motherRelativeFitness = numerator / denominator;
    }

    float random = 0.0f;
    int motherRules = mother->GetNumberOfRules();
    int fatherRules = father->GetNumberOfRules();
    int largestNumOfRules = motherRules > fatherRules ? motherRules : fatherRules;

    for (int k = 0; k < 2; k++)
    {
        for (int i = 0; i < largestNumOfRules; i++)
        {
            random = static_cast <float> (rand()) / static_cast <float> (RAND_MAX);
            if (random < motherRelativeFitness)
            {
                if (motherRules > i)
                {
                    children[k]->AddRule(mother->GetRule(i));
                }
            }
            else
            {
                if (fatherRules > i)
                {
                    children[k]->AddRule(father->GetRule(i));
                }
            }
        }

        if (children[k]->GetNumberOfRules() == 0)
        {
            // THOMAS: Do we want to randomly assign a rule from a parent? Why not random rule?
            children[k]->AddRule(mother->GetRule(rand() % motherRules - 1));
        }
    }

    parents.push_back(mother);
    parents.push_back(father);

    return Crowd(children, parents);
}

vector<Individual*> Population::Crowd(vector<Individual*> children, vector<Individual*> parents)
{
    vector<Individual*> keepers;
    int parentToTake = 0;

    // Genetic Distance
    float distance = children[0]->GetGeneticDistanceTo(parents[0]);
    if (children[0]->GetGeneticDistanceTo(parents[1]) < distance)
    {
        parentToTake = 1;
    }

    /* // Semantic Distance
    float distance = children[0]->GetSemanticDistanceTo(parents[0]);
    if (children[0]->GetSemanticDistanceTo(parents[1]) < distance)
    {
        parentToTake = 1;
    } */

    keepers.push_back((children[0]->GetFitness() > parents[parentToTake]->GetFitness()) ? children[0] : parents[parentToTake]);
    keepers.push_back((children[1]->GetFitness() > parents[!parentToTake]->GetFitness()) ? children[1] : parents[!parentToTake]);

    return keepers;
}

void Population::Evolve()
{ // TODO: maintain diversity
    vector<Individual*> parents;

    SwitchChampion();
    parents.push_back(mChampion); // Pass the most fit individual
    mIndividuals.erase(mIndividuals.begin() + mIndividuals.size() - 1);

    while (parents.size() < mSize * PARENT_SIZE)
    {
        int indexSelectedParent;
        Individual* fittestPlayer;

        for (int i = 0; i < 3; i++)
        {
            int random = rand() % mSize - 1;
            Individual* tempPlayer = mIndividuals[random];

            if (fittestPlayer == NULL)
            {
                fittestPlayer = tempPlayer;
                indexSelectedParent = random;
            }
            else if (abs(fittestPlayer->GetFitness() - tempPlayer->GetFitness()) < 0.0001)
            {
                if (tempPlayer->GetAverageScore() > fittestPlayer->GetAverageScore())
                {
                    fittestPlayer = tempPlayer;
                    indexSelectedParent = random;
                }
            }
            else if (tempPlayer->GetFitness() > fittestPlayer->GetFitness())
            {
                fittestPlayer = tempPlayer;
                indexSelectedParent = random;
            }
        }

        // TODO: Remove the two players that lost
        parents.push_back(fittestPlayer);
        mIndividuals.erase(mIndividuals.begin() + indexSelectedParent);
    }

    vector<Individual*> offspring;
    for (int j = 0; j < 10 * CHILD_SIZE / PARENT_SIZE; j++)
    {
        for (int i = 0; i < mSize * PARENT_SIZE; i++)
        {
            Individual* tempIndiv = parents[i - 1];
            Individual* tempIndiv2;

            EVOLUTION evolutionType;
            float evolve = (float)rand() / (float)RAND_MAX;
            float temp = 0.0f;

            for (int k = 0; k < 3; k++)
            {
                temp += sEvolutionParameters[k];
                if (evolve <= temp)
                {
                    evolutionType = static_cast<EVOLUTION>(k);
                    break;
                }
            }

            switch (evolutionType)
            {
            case MUTATE:
            {
                vector<Individual*> tempParents, tempChildren, tempKeepers;
                tempParents.push_back(tempIndiv);
                tempParents.push_back(tempIndiv);

                tempChildren.push_back(new Individual(*tempIndiv, MUTATION));
                tempChildren.push_back(new Individual(*tempIndiv, MUTATION));

                tempKeepers = Crowd(tempChildren, tempParents);
                offspring.push_back(tempKeepers[0]);
                offspring.push_back(tempKeepers[1]);

                tempParents.clear();
                tempChildren.clear();
                tempKeepers.clear();
            }
            case CROSSOVER:
            {
                vector<Individual*> tempKeepers;
                tempIndiv2 = parents[rand() % parents.size() - 1];

                tempKeepers = Crossover(tempIndiv, tempIndiv2);
                offspring.push_back(tempKeepers[0]);
                offspring.push_back(tempKeepers[1]);

                tempKeepers.clear();
            }
            case CLONE:
            {
                offspring.push_back(tempIndiv);
                offspring.push_back(new Individual(*tempIndiv, !MUTATION));
            }
            }
        }
    }

    assert(offspring.size() == 8 * mSize);

    sort(begin(offspring), end(offspring), LessThanKey());

    vector<Individual*> newPopulation;
    for (int i = 0; i < mSize; i++)
    {
        newPopulation.push_back(offspring[mSize * PARENT_SIZE - i - 1]);
    }

    mIndividuals = newPopulation;
    SwitchChampion();
}

float Population::GetAverageAccuracyOfRules()
{
    float sumRules = 0.0f;

    for (int i = 0; i < mSize; i++)
    {
        sumRules += mIndividuals[i]->GetAverageScore();
    }

    return sumRules / (float)mSize;
}

float Population::GetAveragePointsOfRules()
{
    float sumPoints = 0.0f;

    for (int i = 0; i < mSize; i++)
    {
        mIndividuals[i]->UpdateAverageRulePoints();
        sumPoints += mIndividuals[i]->GetAverageRulePoints();
    }

    return sumPoints / (float)mSize;
}

float Population::GetAverageNumberOfRules()
{
    float numRules = 0.0f;

    for (int i = 0; i < mSize; i++)
    {
        numRules += mIndividuals[i]->GetNumberOfRules();
    }

    return numRules / (float)mSize;
}

Individual* Population::GetChampion()
{
    return mChampion;
}

float Population::GetChampionFitness()
{
    return mChampion->GetFitness();
}

MOVE Population::GetChampionNextMove()
{
    return mChampion->GetNextMove();
}

void Population::SwitchChampion()
{
    sort(begin(mIndividuals), end(mIndividuals), LessThanKey());
    mChampion = mIndividuals.back();
}

void Population::UpdateAverageFitness()
{
    float sumFitness = 0.0f;

    for (int i = 0; i < mSize; i++)
    {
        sumFitness += mIndividuals[i]->GetFitness();
    }

    mAverageFitness = sumFitness / (float) mSize;
}

void Population::UpdateFitness()
{
    for (int i = 0; i < mSize; i++)
    {
        mIndividuals[i]->UpdateFitness();
    }
}

void Population::UpdateNextMoves()
{
    for (int i = 0; i < mSize; i++)
    {
        mIndividuals[i]->UpdateNextMove();
    }
}

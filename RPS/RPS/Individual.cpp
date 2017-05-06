#include "Individual.h"

#include "Constants.h"
#include "History.h"

int Individual::sIDCounter = 0;
const float Individual::sMutationParameters[2] = { ADD_RULE, MODIFY_RULE };
const float Individual::sModificationParameters[4] = { ADD_COND, MODIFY_COND, CHANGE_ACT, CHANGE_LOC };

Individual::Individual()
{
    //Initialize default values
    mID = sIDCounter++;
    mDefaultMove = static_cast<MOVE>(rand() % 3);
    mNextMove = mDefaultMove;
    mRulePlayed = nullptr;
    mAverageScore = 0.0f;
    mAverageRulePoints = 0.0f;

    mRules.clear();
    mRules.push_back(new Rule());

    DetermineInitialFitness();
    UpdateAverageScore();
}

Individual::Individual(Individual& parent, bool mutate)
{
    //Initialize default values
    mID = sIDCounter++;
    mDefaultMove = static_cast<MOVE>(rand() % 3);
    mNextMove = mDefaultMove;
    mRulePlayed = nullptr;
    mAverageRulePoints = 0.0f;
    mAverageRulePoints = 0.0f;

    mRules = parent.mRules;

    if (mutate)
    {
        MUTATION_TYPE mutationType = Add;
        float mutation = static_cast <float> (rand()) / static_cast <float> (RAND_MAX);

        float temp = 0;
        for (int i = 0; i < 2; i++)
        {
            temp += sMutationParameters[i];
            if (mutation <= temp)
            {
                mutationType = static_cast<MUTATION_TYPE>(i);
                break;
            }
        }

        MutatePlayer(mutationType);
    }

    DetermineInitialFitness();
    UpdateAverageScore();
}

Individual::~Individual() {
    ClearRules();
}

void Individual::MutatePlayer(MUTATION_TYPE mutationBaseType)
{
    MODIFICATION_TYPE modificationType = AddCondition;
    float modification = static_cast <float> (rand()) / static_cast <float> (RAND_MAX);

    float temp = 0;
    for (int i = 0; i < 4; i++)
    {
        temp += sModificationParameters[i];
        if (modification <= temp) {
            modificationType = static_cast<MODIFICATION_TYPE>(i);
            break;
        }
    }

    switch (mutationBaseType)
    {
    case Add:
    {
        mRules.push_back(new Rule());
        break;
    }
    case Modify:
    {
        int randomRule = rand() % mRules.size();
        int randomCondition = rand() % (mRules[randomRule].GetConditionsSize());

        switch (modificationType)
        {
        case ModifyCondition:
            mRules[randomRule].ModifyCondition(randomCondition);
            break;
        case AddCondition:
            //ANITA: Do we still want to create conditions with arbitrary number of conditions?
            mRules[randomRule].AddCondition();
            break;
        case ChangeAction:
            mRules[randomRule].ChangeAction();
            break;
        case ChangeLocation:
            mRules[randomRule].ChangeLocation();
        }
    }
    default:
        break;
    }
}

void Individual::DeterminePastPlayedMoves()
{
    int historyLookBack = gHistory.GetSize() < MAX_HISTORY_LOOKBACK ? gHistory.GetSize() : MAX_HISTORY_LOOKBACK;
    
    for (int i = 0; i < historyLookBack; i++)
    {
        Rule* ruletemp = nullptr;
        int highestScore = -1;
        for (int j = 0; j < mRules.size(); j++)
        {
            if (mRules[j].IsRuleSatisfied(i))
            {
                int rulescore = mRules[j].GetScore();
                //ANITA: Changed the conditions here
                //THOMAS: What?
                if (rulescore > highestScore)
                {
                    ruletemp = &mRules[j];
                    highestScore = rulescore;
                }
            }
        }

        if (ruletemp != nullptr)
        {
            mPlayedMoves[i] = ruletemp->GetNextMove(); // TODO: Revisit, is this right?
        }
        else
        {
            mPlayedMoves[i] = mDefaultMove;
        }
    }
}

void Individual::DetermineInitialFitness()
{
    float reward = 0;
    int historyLookBack = MAX_HISTORY_LOOKBACK;

    if (!gHistory.Empty())
    {
        //Get the moves played by the player in the past 10 rounds
        DeterminePastPlayedMoves();

        for (int i = 0; i < historyLookBack; i++)
        {
            if (DetermineOutcome(mPlayedMoves[i], gHistory[i].second) == W)
            {
                reward += 1;
            }
            else if (DetermineOutcome(mPlayedMoves[i], gHistory[i].second) == L)
            {
                reward += -1;
            }
        }

        //TODO: Evaluate based on history
        //TODO: evaluate fitness every turn? Or less
        if (historyLookBack != 0)
        {
            mFitness = mFitness*(1 - ALPHA) + (reward / historyLookBack)*ALPHA;
        }
    }
}

void Individual::UpdateNextMove()
{
    Rule* ruletemp = nullptr;
    int highestScore = -1;

    for (int i = 0; i < mRules.size(); i++)
    {
        if (mRules[i].IsRuleSatisfied(0))
        {
            int ruleScore = mRules[i].GetScore();
            if (ruleScore > highestScore)
            {
                ruletemp = &mRules[i];
                highestScore = ruleScore;
            }
        }
    }

    if (ruletemp != nullptr)
    {
        mNextMove = ruletemp->GetNextMove();
        mRulePlayed = ruletemp;
    }
    else
    {
        mNextMove = static_cast<MOVE>(rand() % 3);
        mRulePlayed = nullptr;
    }
}

void Individual::UpdateFitness()
{
    //mark that the rule was selected
    if (mRulePlayed)
    {
        mRulePlayed->IncrementTimesUsed();
    }

    float reward = 0;

    if (!gHistory.Empty())
    {
        if (DetermineOutcome(gHistory[0].first, gHistory[0].second) == W)
        {
            reward = 1;

            //mark that the rule won
            if (mRulePlayed)
            {
                mRulePlayed->IncrementTimesWon();
            }
        }
        else if (DetermineOutcome(gHistory[0].first, gHistory[0].second) == L)
        {
            reward = -1;
        }

    //TODO: Evaluate based on history
    //TODO: evaluate fitness every turn? Or less
    mFitness = mFitness*(1 - ALPHA) + reward*ALPHA;
    }
}

void Individual::UpdateAverageScore()
{
    int scoreTemp = 0;
    for (int i = 0; i < mRules.size(); i++)
    {
        scoreTemp += mRules[i].GetScore();
    }

    mAverageScore = scoreTemp / mRules.size();
}

void Individual::UpdateAverageRulePoints()
{
    float pointTemp = 0;
    for (int i = 0; i < mRules.size(); i++)
    {
        pointTemp += mRules[i].GetTimesWon();
    }
    mAverageRulePoints = mRules.size() == 0 ? 0.0f : pointTemp / float(mRules.size());
}

float Individual::GetWinningRatio()
{
    int totalTimesCalled = 0;
    int totalTimesWon = 0;

    for (int i = 0; i < mRules.size(); i++)
    {
        totalTimesCalled += mRules[i].GetTimesUsed();
        totalTimesWon += mRules[i].GetTimesWon();
    }

    return totalTimesCalled == 0 ? 0.0f : totalTimesWon / totalTimesCalled;
}

float Individual::GetGeneticDistanceTo(Individual* otherInd)
{
    float sum1 = 0.0f;

    for (int i = 0; i < mRules.size(); i++)
    {
        float sum2 = 0.0f;
        for (int j = 0; j < otherInd->mRules.size(); j++)
        {
            sum2 += Rule::GetGeneticDistanceBetweenRules(mRules[i], otherInd->mRules[j]);
        }
        sum1 += sum2;
    }

    return (float)(sum1 / mRules.size());
}

/* TODO: Semantic distance needs to be rethought */
float Individual::GetSemanticDistanceTo(Individual* otherInd)
{
    float distance = 0.0f;

    for (int i = 0; i < mRules.size(); i++)
    {
        MOVE playedMove = NO;
        int highscore = 0;

        for (int j = 0; j < otherInd->mRules.size(); j++)
        {
            if (mRules[i].IsRuleSatisfied(otherInd->mRules[j]))
            {
                int tempScore = otherInd->GetRule(j).GetScore();
                if (playedMove == NO || tempScore > highscore)
                {
                    //playedMove = otherInd->mRules[j].mAction;
                    highscore = tempScore;
                }
            }
        }

        //if (playedMove == NO || playedMove != mRules[i].mAction)
        {
            distance += 1.0f;
        }
    }

    return distance;
}

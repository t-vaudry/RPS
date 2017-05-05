#include "Individual.h"

#include "Constants.h"

int Individual::mIDCounter = 0;

Individual::Individual()
{
    //Initialize default values
    mID = mIDCounter++;
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
    mID = mIDCounter++;
    mDefaultMove = static_cast<MOVE>(rand() % 3);
    mNextMove = mDefaultMove;
    mRulePlayed = nullptr;
    mAverageRulePoints = 0.0f;
    mAverageRulePoints = 0.0f;

    mRules = parent.mRules;

    if (mutate)
    {
        MUTATION_TYPE mutationType = Add;
        //TODO: Determine mutation type based on probabilities of all mutations

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
    MODIFICATION_TYPE modificationType = ChangeAction;
    //TODO: Determine modificationType

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

        //ANITA: Why was there a +1 here?
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
    //TODO: Need history to get lookback
    //int historyLookBack = History.size() < MAX_HISTORY_LOOKBACK ? History.size() : MAX_HISTORY_LOOKBACK;
    int historyLookBack = MAX_HISTORY_LOOKBACK;
    for (int i = 0; i < historyLookBack; i++)//TODO: 10 should be parametrized to whatever we decide the max lookback in history is
    {
        Rule* ruletemp = nullptr;
        int highestScore = -1;
        for (int j = 0; j < mRules.size(); j++)
        {
            if (mRules[j].IsRuleSatisfied(i))
            {
                int rulescore = mRules[j].GetScore();
                //ANITA: Changed the conditions here
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

//TODO ANITA: Need to determine how we are checking for win/loss
void Individual::DetermineInitialFitness()
{
    float reward = 0;
    int historyLookBack = MAX_HISTORY_LOOKBACK;
    //TODO ANITA: Add history
    //if (!History.empty())
    {
        //Get the moves played by the player in the past 10 rounds
        DeterminePastPlayedMoves();

        for (int i = 0; i < historyLookBack; i++)
        {
            //if (static_cast<int>(createCondition(playedMove[i], History.at(History.size() - i - 1).second)) < pow(2, 3))
            //{
            //    reward += 1; //fitness = fitness*(1 - alpha) + reward*alpha;
            //}
            //else if (static_cast<int>(createCondition(playedMove[i], History.at(History.size() - i - 1).second)) > pow(2, 5))
            //{
            //    reward += -1; //fitness = fitness*(1 - alpha) + reward*alpha;
            //}
        }

        //TODO: Evaluate based on history
        //TODO: evaluate fitness every turn? Or less
        if (historyLookBack != 0)
        {
            //mFitness = mFitness*(1 - ALPHA) + (reward / historyLookBack)*ALPHA;
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
//TODO
//if (!History.empty())
{
    //TODO: How to make conditions now?
    //if (static_cast<int>(Condition::CreateCondition(nextMove, History.at(History.size() - 1).second)) < pow(2, 3))
    {
        reward += 1; //fitness = fitness*(1 - alpha) + reward*alpha;

                        //mark that the rule won
        if (mRulePlayed)
            mRulePlayed->IncrementTimesWon();
    }
    //else if (static_cast<int>(createCondition(nextMove, History.at(History.size() - 1).second)) > pow(2, 5))
    {
        reward += -1; //fitness = fitness*(1 - alpha) + reward*alpha;
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

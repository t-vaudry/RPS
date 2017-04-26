#include "Individual.h"

#include "Constants.h"

Individual::Individual()
{
    //TODO
}

Individual::Individual(bool isPlayerOne)
{
    //Initialize default values
    mID = mIDCounter++;
    mIsPlayerOne = isPlayerOne;
    mDefaultMove = static_cast<MOVE>(rand() % 3);
    mNextMove = mDefaultMove;
    mRulePlayed = nullptr;
    mAverageRulePoints = 0.0f;
    mAverageRulePoints = 0.0f;

    mRules.clear();
    mRules.push_back(Rule::GenerateRandomRule(true));

    DetermineInitialFitness();
    UpdateAverageScore();
}

Individual::Individual(Individual& parent, bool mutate)
{
    //Initialize default values
    mID = mIDCounter++;
    mIsPlayerOne = parent.mIsPlayerOne;
    mDefaultMove = static_cast<MOVE>(rand() % 3);
    mNextMove = mDefaultMove;
    mRulePlayed = nullptr;
    mAverageRulePoints = 0.0f;
    mAverageRulePoints = 0.0f;

    mRules = parent.mRules;

    if (mutate)
    {
        MUTATIONTYPE mutationType = Add;
        //TODO: Determine mutation type based on probabilities of all mutations

        MutatePlayer(mutationType);
    }
    DetermineInitialFitness();
    UpdateAverageScore();
}

void Individual::MutatePlayer(MUTATIONTYPE mutationBaseType)
{
    MODIFICATIONTYPE modificationType = ChangeAction;
    //TODO: Determine modificationType

    switch (mutationBaseType)
    {
    case Add:
    {
        mRules.push_back(Rule::GenerateRandomRule(true));
        break;
    }
    case Modify:
    {
        int randomRule = rand() % mRules.size();

        //ANITA: Why was there a +1 here?
        int randomCondition = rand() % (mRules[randomRule].mConditions.size());

        switch (modificationType)
        {
        case ModifyCondition:
            mRules.at(randomRule).mConditions.at(randomCondition) = Condition::CreateCondition();
            break;
        case AddCondition:
            //ANITA: Do we still want to create conditions with arbitrary number of conditions?
            mRules.at(randomRule).mConditions.push_back(Condition::CreateCondition());
            break;
        case ChangeAction:
            mRules.at(randomRule).mMove = static_cast<MOVE>(rand() % 3);
            break;
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
            if (Rule::IsRuleSatisfied(mRules[j], i))
            {
                int rulescore = mRules[j].GetRuleScore();
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
            mPlayedMoves[i] = ruletemp->mMove;
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
    int histroyLookBack = MAX_HISTORY_LOOKBACK;
    //TODO ANITA: Add history
    //if (!History.empty())
    {
        //Get the moves played by the player in the past 10 rounds
        DeterminePastPlayedMoves();

        if (mIsPlayerOne)
        {
            for (int i = 0; i < histroyLookBack; i++)
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
        }
        else
        {
            for (int i = 0; i < histroyLookBack; i++)
            {
                //if (static_cast<int>(createCondition(History.at(History.size() - 1 - i).first, playedMove[i])) < pow(2, 3))
                //{
                //    reward += -1; //fitness = fitness*(1 - alpha) + reward*alpha;
                //}
                //else if (static_cast<int>(createCondition(History.at(History.size() - i - 1).first, playedMove[i])) > pow(2, 5))
                //{
                //    reward += 1;// fitness = fitness*(1 - alpha) + reward*alpha;
                //}
            }
        }

        //TODO: Evaluate based on history
        //TODO: evaluate fitness every turn? Or less
        if (histroyLookBack != 0)
        {
            //mFitness = mFitness*(1 - ALPHA) + (reward / historyLookBack)*ALPHA;
        }
    }
}

void Individual::UpdateNextMove()
{

}
void Individual::UpdateFitness()
{

}
void Individual::UpdateAverageScore()
{

}
void Individual::UpdateAverageRulePoints()
{

}

float Individual::GetWinningRatio()
{
    return 0;
}

float Individual::GetGeneticDistanceTo(const Individual* otherInd)
{
    return 0;
}
float Individual::GetSemanticDistanceTo(const Individual* otherInd)
{
    return 0;
}

#include "Rule.h"
#include "History.h"

using namespace std;

Rule::Rule(bool oneConditionOnly)
{
    mConditions.push_back(new Condition(oneConditionOnly));
    mAction = (rand() % 3) - 1;
    mLocation = 0;
    mScore = 0;
    mTimesUsed = 0;
    mTimesWon = 0;
}

bool Rule::IsRuleSatisfied(int turn) // TODO: Out of bounds somewhere
{
    if (mConditions.size() > gHistory.GetSize())
        return false;

    bool satisfied = true;
    for (int i = 0; i < mConditions.size(); i++)
    {
        if (gHistory.GetSize() < turn + i + 1)
            return false;

        satisfied = mConditions[turn].mOutcome == X || mConditions[turn].mOutcome == DetermineOutcome(gHistory[turn].first, gHistory[turn].second);
        if (!satisfied)
            break;
    }
    return satisfied;
}

bool Rule::IsEquivalent(Rule& rule)
{
    int maxSize = rule.GetConditionsSize() > mConditions.size() ? rule.GetConditionsSize() : mConditions.size();
    bool isSatisfied = true;
    for (int i = 0; i < maxSize; i++)
    {
        isSatisfied &= ((mConditions[i].mOutcome == X) || (mConditions[i].mOutcome == rule.GetConditionAt(i).mOutcome) || (rule.GetConditionAt(i).mOutcome == X));
    }

    return isSatisfied;
}

MOVE Rule::GetNextMove()
{
    MOVE nextMove = NO;
    MOVE opponentMove = NO;
    switch (mAction)
    {
    case -1:
        opponentMove = gHistory[mLocation].second;
        switch (opponentMove)
        {
        case R:
            nextMove = S;
            break;
        case P:
            nextMove = R;
            break;
        case S:
            nextMove = P;
            break;
        }
        break;
    case 0:
        nextMove = gHistory[mLocation].first;
        break;
    case 1:
        opponentMove = gHistory[mLocation].second;
        switch (opponentMove)
        {
        case R:
            nextMove = P;
            break;
        case P:
            nextMove = S;
            break;
        case S:
            nextMove = R;
            break;
        }
        break;
    default:
        break;
    }

    return nextMove;
}

void Rule::AddCondition()
{
    mConditions.push_back(new Condition(false));
}

void Rule::ChangeAction()
{
    mAction = (rand() % 3) - 1;
}

void Rule::ChangeLocation()
{
    mLocation = rand() % mConditions.size();
}

void Rule::ModifyCondition(int index)
{
    if (mConditions.size() == 1)
    {
        mConditions[0] = new Condition(true);
    }
    else
    {
        mConditions[index] = new Condition(false);
    }
}

float Rule::GetGeneticDistanceBetweenRules(Rule& one, Rule& two)
{
    float conditions = 0.0f;
    float action = 0.0f;
    float location = 0.0f;
    float distance;

    int maxSize = one.GetConditionsSize() > two.GetConditionsSize() ? one.GetConditionsSize() : two.GetConditionsSize();
    for (int i = 0; i < maxSize; i++)
    {
        if (!((one.GetConditionAt(i).mOutcome == X) || (two.GetConditionAt(i).mOutcome == X)))
        {
            if (one.GetConditionAt(i).mOutcome == two.GetConditionAt(i).mOutcome)
            {
                conditions += 1.0f;
            }
        }
    }

    if (one.GetAction() != two.GetAction())
    {
        action = 1.0f;
    }

    if (one.GetLocation() != two.GetLocation())
    {
        location = 1.0f;
    }

    distance = conditions*WEIGHTED_CONDITION + action*WEIGHTED_ACTION + location*WEIGHTED_LOCATION;
    return distance;
}

Rule Rule::GenerateRandomRule()
{
    Rule newRule = new Rule(false);

    for (int i = 0; i < rand() % gHistory.GetSize(); i++)
    {
        newRule.mConditions.push_back(new Condition(false));
    }

    newRule.mLocation = -1 * (rand() % newRule.mConditions.size());
    return newRule;
}

OUTCOME DetermineOutcome(MOVE one, MOVE two)
{
    OUTCOME outcome;
    switch (one)
    {
    case R:
        switch (two)
        {
        case R: outcome = D; break;
        case P: outcome = L; break;
        case S: outcome = W; break;
        default: break;
        }
        break;
    case P:
        switch (two)
        {
        case R: outcome = W; break;
        case P: outcome = D; break;
        case S: outcome = L; break;
        default: break;
        }
        break;
    case S:
        switch (two)
        {
        case R: outcome = L; break;
        case P: outcome = W; break;
        case S: outcome = D; break;
        default: break;
        }
        break;
    default:
        outcome = X;
        break;
    }

    return outcome;
}
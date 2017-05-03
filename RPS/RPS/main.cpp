#include "Population.h"
#include "History.h"
#include "Library.h"
#include "Analytics.h"

extern "C" {
#include "pyInterface.h"
}

using namespace std;

typedef enum {
    WIN,
    LOSS,
    TIE
} OUTCOME;

void PlayBot(char* file, char* directory);
OUTCOME DetermineOutcome(MOVE one, MOVE two);

int main()
{
    PlayBot("", "");
    return 0;
}

void PlayBot(char* file, char* directory)
{
    Analytics* analytics = new Analytics(directory);

    Py_Initialize();
    PyRun_SimpleString("import sys");
    PyRun_SimpleString("sys.path.append(\".\")");

    Population* population = new Population(500);
    History* history = new History;
    Library* library = new Library;
    RPSBot* pyCurrentBot = CompileBot(file);
    int rounds = 0;

    while (rounds < NUM_OF_ROUNDS)
    {
        // TODO: Calculate and output completion(%) for Google Test

        int lossCount = 0;
        for (int i = 0; i < GENERATION_ROUNDS; i++)
        {
            population->UpdateNextMoves();
            MOVE ourMove = population->GetChampionNextMove();
            MOVE botMove;

            pyCurrentBot = PlayBotRound(pyCurrentBot, (rounds != 0) ? history->GetLastMove() : -1);
            botMove = static_cast<MOVE>(pyCurrentBot->outputMove);

            history->Add(ourMove, botMove);

            OUTCOME outcome = DetermineOutcome(ourMove, botMove);
            if (outcome == WIN)
            {
                lossCount = 0;
            }
            else if (outcome == LOSS)
            {
                lossCount++;
            }
            else // outcome == TIE
            {
                lossCount = 0;
            }

            population->UpdateFitness();
            population->UpdateAverageFitness();

            if (lossCount == LOSING_STREAK)
            {
                library->Add(population->GetChampion());

                float tempFitness = population->GetChampionFitness();
                while (population->GetChampionFitness() < (tempFitness + abs(tempFitness * 0.1)))
                {
                    population->Evolve();
                }

                lossCount = 0;
            }

            rounds++;
        }

        population->Evolve();
    }

    // TODO: Analytics
    // analytics->LogAnalytics(0.0f, "test.txt");
    // TODO: Output 100%

    delete analytics;
    delete population;
    delete history;
    delete library;
    delete pyCurrentBot;
}

OUTCOME DetermineOutcome(MOVE one, MOVE two)
{
    OUTCOME outcome;
    switch (one)
    {
    case R:
        switch (two)
        {
        case R: outcome = TIE; break;
        case P: outcome = LOSS; break;
        case S: outcome = WIN; break;
        default: break;
        }
        break;
    case P:
        switch (two)
        {
        case R: outcome = WIN; break;
        case P: outcome = TIE; break;
        case S: outcome = LOSS; break;
        default: break;
        }
        break;
    case S:
        switch (two)
        {
        case R: outcome = LOSS; break;
        case P: outcome = WIN; break;
        case S: outcome = TIE; break;
        default: break;
        }
        break;
    default:
        break;
    }

    return outcome;
}
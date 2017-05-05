#include "Population.h"
#include "History.h"
#include "Library.h"
#include "Analytics.h"

extern "C" {
#include "pyInterface.h"
}

using namespace std;

void PlayBot(char* file, char* directory);

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

            pyCurrentBot = PlayBotRound(pyCurrentBot, (rounds != 0) ? gHistory.GetLastMove() : -1);
            botMove = static_cast<MOVE>(pyCurrentBot->outputMove);

            gHistory.Add(ourMove, botMove);

            OUTCOME outcome = DetermineOutcome(ourMove, botMove);
            if (outcome == W)
            {
                lossCount = 0;
            }
            else if (outcome == L)
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
                gLibrary.Add(population->GetChampion());

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
    delete pyCurrentBot;
}
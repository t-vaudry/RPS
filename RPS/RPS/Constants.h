#pragma once

// Coevolution constants
#define POPULATION_SIZE         1000
#define NUM_OF_ROUNDS           1000
#define GENERATION_ROUNDS       10
#define LOSING_STREAK           2
#define WINNING_STREAK          2

// History constant
#define MAX_HISTORY_SAVED       20

// Individual constants
#define ALPHA                   0.05
#define MAX_HISTORY_LOOKBACK    10
#define ADD_RULE                0.4
#define MODIFY_RULE             0.6
#define ADD_COND                0.3
#define MODIFY_COND             0.6
#define CHANGE_ACT              0.1

// Population constants
#define MUTATION_PROB           0.5
#define CROSSOVER_PROB          0.4
#define CLONE_PROB              0.1
#define PARENT_SIZE             0.2
#define CHILD_SIZE              0.8

// Genetic distance percentages
#define WEIGHTED_CONDITION      0.66 // Relative to probability of modifying condition
#define WEIGHTED_ACTION         0.94 // Relative to probability of changing action
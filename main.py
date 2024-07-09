import sys
import SQLParser 
import SQLGenAlg
import SQLCostCalculator
from SQLParser import parse_sql
from SQLGenAlg import genetic_algorithm
from SQLCostCalculator import read_join_stats_from_excel

def main():
    SQLfilename = sys.argv[1]
    join_selectivity_file = sys.argv[2]

    #load table sizes and join selectivities
    read_join_stats_from_excel(join_selectivity_file)

    print("test")

    #parse SQL file
    SQLJoins = parse_sql(SQLfilename)

    #run GA on joins
    genetic_algorithm(SQLJoins)



if __name__ == "__main__":
    main()
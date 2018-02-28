import pandas as pd
root = '/media/sf_virtual_share/'

def main():
    detailed_results = pd.read_csv(root + 'NCAATourneyDetailedResults.csv')
    detailed_results.insert(3, 'WTeamSeed', None)
    detailed_results.insert(6, 'LTeamSeed', None)
    seeds = pd.read_csv(root + 'NCAATourneySeeds.csv')

    for i, row in detailed_results.iterrows():
        wTeamSeedRow = seeds.loc[(seeds['Season'] == row['Season']) & (seeds['TeamID'] == row['WTeamID'])]
        lTeamSeedRow = seeds.loc[(seeds['Season'] == row['Season']) & (seeds['TeamID'] == row['LTeamID'])]
        # detailed_results.iloc[index]['WTeamSeed'] = wTeamSeedRow.iloc[0]['Seed']
        # detailed_results.iloc[index]['LTeamSeed'] = lTeamSeedRow.iloc[0]['Seed']

        detailed_results.loc[detailed_results.index[i], 'WTeamSeed'] = wTeamSeedRow.loc[wTeamSeedRow.index[0], 'Seed']
        detailed_results.loc[detailed_results.index[i], 'LTeamSeed'] = lTeamSeedRow.loc[lTeamSeedRow.index[0], 'Seed']

    detailed_results.to_csv('NCAATourneyDetailedResultsWithSeeds.csv')

if __name__ == "__main__":
    main()

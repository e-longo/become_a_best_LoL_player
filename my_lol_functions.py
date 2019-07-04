import pandas as pd

# # função utilizada para recuperar o accountId do jogador, passando como parâmetro a região, o nickname e o development api key

# def get_account_id(my_region, nickname, development_api_key):
#   watcher = RiotWatcher('RGAPI-62c3fa21-5d62-4741-9a7d-6862ab3ac9d7')
#   my_region = 'br1'
#   nickname = 'ElFeRtOn'

#   me = watcher.summoner.by_name(my_region, nickname)
  
#   return me['accountId']

# função utilizada para recuperar os dados de campeões, sendo estes: key (chave identificadora), name e tags (classes)
def get_champions(watcher, version_patch):
  champions_data = watcher.data_dragon.champions(version_patch)
  ix = 0
  df_champions = pd.DataFrame(columns=['key','name','tags'])

  for champ in champions_data['data'].keys():
    df_champions.loc[ix, 'key'] = champions_data['data'][champ]['key']
    df_champions.loc[ix, 'name'] = champions_data['data'][champ]['name']
    df_champions.loc[ix, 'tags'] = champions_data['data'][champ]['tags']
    ix += 1

  return df_champions

# função utilizada para recuperar as partidas jogadas. São passados como parâmetro a região e o account_id e é devolvido um data frame com as partidas
def get_matches(watcher, my_region, my_account_id):
  matches = watcher.match.matchlist_by_account(my_region, my_account_id)
  matches_list = []

  for x in matches['matches']:
    matches_list.append(x['gameId'])
  
  return matches_list

# função utilizada para recuperar os dados de uma determinada partida. São passados como parâmetros a região e o id da partida. É retornado um dicionário com os dados
def get_match_data(watcher, my_region, match_id):
  return watcher.match.by_id(my_region, match_id)

# função utilizada para recuperar o participantId do jogador em uma determinada. São passados como parâmetro o nickname do jogador e a partida.
def get_participantId(watcher, match, nickname):
  for participant in match['participantIdentities']:
    if participant['player']['summonerName'] == nickname:
      return participant['participantId']
  return -1

# função utilizada para recuperar as estatísticas do jogador em uma determinada partida.
def get_participantStatistics(match, participant_id):  
  game_duration = match['gameDuration']
  df_part = pd.DataFrame(match['participants'])
  df_part = df_part[df_part['participantId'] == participant_id]
  
  features_list = ['participantId','win','kills','deaths','assists','largestKillingSpree','largestMultiKill','killingSprees','longestTimeSpentLiving','totalDamageDealt',\
                 'trueDamageDealt','totalDamageDealtToChampions','trueDamageDealtToChampions','totalHeal','totalUnitsHealed','damageSelfMitigated',\
                 'damageDealtToObjectives','damageDealtToTurrets','visionScore','totalDamageTaken','goldEarned','goldSpent','turretKills','inhibitorKills',\
                 'totalMinionsKilled','neutralMinionsKilled','neutralMinionsKilledTeamJungle','neutralMinionsKilledEnemyJungle','totalTimeCrowdControlDealt',\
                 'champLevel','visionWardsBoughtInGame','sightWardsBoughtInGame','wardsPlaced','wardsKilled','firstBloodKill','firstBloodAssist','firstTowerKill',\
                 'firstTowerAssist','firstInhibitorKill','firstInhibitorAssist']
  
  df_part_stat = df_part['stats'].apply(pd.Series)
  df_part_stat = df_part_stat.reindex(columns=features_list)
  df_part_stat['KDA'] = df_part_stat[['kills','deaths','assists']].apply(lambda x: (x[0] + x[2]) / (1 if x[1] == 0 else x[1]), axis=1)
  
  df_other_inf = df_part[['participantId','teamId']].copy()
#  df_other_inf = df_part[['participantId','championId','teamId']].copy()

  df_final = pd.merge(df_other_inf, df_part_stat, on='participantId')
  df_final['gameDuration'] = game_duration
  
  df_final['red_team'] = df_final['teamId'].apply(lambda x: 1 if x == 200 else 0)
  df_final['blue_team'] = df_final['teamId'].apply(lambda x: 1 if x == 100 else 0)
  
  df_final = df_final.fillna(0)
  df_final = df_final.apply(lambda x: x.astype(int))
  
  df_final = df_final.drop(['participantId','teamId'], axis=1)

  return df_final

# função utilizada para recuperar os dados de todas as partidas em um único data frame e já no formato pronto para ser utilizado
def get_dados(watcher, my_region, account_id, nickname):
  match_list = get_matches(watcher, my_region, account_id)
  
  df_list = []
  
  for match in match_list:
    df_dados = get_participantStatistics(get_match_data(watcher,my_region,match),get_participantId(watcher,get_match_data(watcher,my_region,match),nickname))
    df_list.append(df_dados)
  
  return pd.concat(df_list, ignore_index=True)

def get_accuracy(preds, outliers):
    full_data = pd.read_csv("data.csv")
    
    df = pd.DataFrame(full_data['win'], columns = ['win'])
    df = df.drop(df.index[outliers]).reset_index(drop = True)
    
    df['preds'] = preds
    df['result'] = df[['win','preds']].apply(lambda x: 1 if x[0] == x[1] else 0, axis=1)
    
    return (df['result'].sum() / df.shape[0]) * 100

### Install

Este projeto foi desevolvido utilizando o Python 3.7.1.

- [NumPy](http://www.numpy.org/) 
- [Pandas](http://pandas.pydata.org)
- [matplotlib](http://matplotlib.org/)
- [scikit-learn](http://scikit-learn.org/stable/)
- [RiotWatcher](https://riot-watcher.readthedocs.io/en/latest/)

**Features:**
- win: indica se a partida foi uma vitória (valor igual a 1) ou se foi uma derrota (valor igual a 0);
- kills: quantidade de campeões que foram abatidos naquela partida pelo jogador;
- deaths: quantidade de mortes sofridas naquela partida pelo jogador;
- assists: quantidade de assistências prestadas em abatimentos (kills) naquela partida pelo jogador;
- largestKillingSpree: maior killing spree obtido pelo jogador naquela partida;
- largestMultiKill: maior multi kill obtido pelo jogador naquela partida;
- killingSprees: quantidade de killing spree obtido pelo jogador naquela partida;
- longestTimeSpentLiving: maior duração de tempo em segundos que o jogador ficou sem morrer naquela partida;
- totalDamageDealt: valor total de dano inflingido pelo jogador naquela partida;
- trueDamageDealt: valor total de dano verdadeiro inflingido pelo jogador naquela partida;
- totalDamageDealtToChampions: valor total de dano inflingido em campeões pelo jogador naquela partida;
- trueDamageDealtToChampions: valor total de dano verdadeiro inflingido em campeões pelo jogador naquela partida;
- totalHeal: valor total de cura realizado pelo jogador naquela partida;
- totalUnitsHealed: quantidade total de unidade curadas pelo jogador naquela partida;
- damageSelfMitigated: valor de dano auto mitigado pelo jogador;
- damageDealtToObjectives: total de dano inflingido em objetivos pelo jogador;
- damageDealtToTurrets: total de dano inflingido pelo jogador em torres;
- visionScore: pontuação de visão obtida pelo jogador naquela partida;
- totalDamageTaken: total de dano recebido pelo jogador naquela partida;
- goldEarned: valor total de ouro ganho pelo jogador naquela partida;
- goldSpent: valor total de ouro gasto pelo jogador naquela partida;
- turretKills: quantidade de torres adversárias destruídas;
- inhibitorKills: quantidade de inibidores adversários destruídos;
- totalMinionsKilled: quantidade total de minions abatidos pelo jogador naquela partida;
- neutralMinionsKilled: quantidade de minions neutros abatidos pelo jogador naquela partida;
- neutralMinionsKilledTeamJungle: quantidade de monstros da jungle do seu time abatidos pelo jogador naquela partida;
- neutralMinionsKilledEnemyJungle: quantidade de monstros da jungle do time adversário abatidos pelo jogador naquela partida;
- totalTimeCrowdControlDealt: tempo total de controle de grupo infligido pelo jogador;
- champLevel: nível que o campeão do jogador terminou a partida;
- visionWardsBoughtInGame: quantidade de "vision wards" (pink wards) compradas pelo jogador naquela partida;
- sightWardsBoughtInGame: quantidade de "sight wards" (green wards) compradas pelo jogador naquela partida;
- wardsPlaced: quantidade de wards colocadas pelo jogador naquela partida;
- wardsKilled: quantidade de wards inimigas retiradas pelo jogador naquela partida;
- firstBloodKill: indica se o jogador obteve ou não (1 para sim e 0 para não) o first blood (teve o primeiro abate) da partida;
- firstBloodAssist: indica se o jogador ajudou a obter ou não (1 para sim e 0 para não) o first blood (teve o primeiro abate) da partida;
- firstTowerKill: indica se o jogador obteve ou não (1 para sim e 0 para não) o first break (destruiu a primeira torre) da partida;
- firstTowerAssist: indica se o jogador ajudou a obter ou não (1 para sim e 0 para não) o first break (destruiu a primeira torre) da partida;
- firstInhibitorKill: indica se o jogador destuiu ou não (1 para sim e 0 para não) o primeiro inibidor da partida;
- firstInhibitorAssist: indica se o jogador ajudou a destuir ou não (1 para sim e 0 para não) o primeiro inibidor da partida;
- KDA: métrica calculada a partir da quantidade de kills, deaths e assists do jogador da valor. O cálculo é (kills + assists) / deaths. Se o valor de deaths for igual a 0 o mesmo é substituído por 1;
- gameDuration: tempo de duração da partida em segundos;
- red_team: indica se o time o do jogador é o vermelho ou não (1 para sim e 0 para não);
- blue_team:  indica se o time o do jogador é o azul ou não (1 para sim e 0 para não).

**Créditos:**
Na construção deste trabalho foi utilizado um código fornecido pela UDACITY no projeto de customer_segments do curso de engenheiro de machine learning. Este código está anexado e é chamado de visuals.py. Ele tem o objetivo de plotar alguns gráficos para melhor visualização/entendimento dos dados. Vale lembrar que algumas funções deste código foram alteradas para serem utilizados neste projeto. Todavia todos os créditos deste código, o visuals.py, são dados à UDACITY.

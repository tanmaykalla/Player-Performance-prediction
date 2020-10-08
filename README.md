# Player-Performance-prediction

Introduction: In this Model, we have used multinomial and binary logistic regression. Logistic regression is the appropriate regression analysis to conduct when the dependent variable(Y) is binary or discreet.  Like all regression analyses, logistic regression is a predictive analysis.  Logistic regression is used to describe data and to explain the relationship between one dependent binary variable and one or more nominal, ordinal, interval or ratio-level independent variables(Xi). We have used multivariable logistic regression which is basically two or more independent variables (Xi) are taken into consideration simultaneously to predict the value of a dependent variable (Y) for each subject.

Fantasy Premier League(FPL):- FPL is a game based on the top flight English football league in which the user selects a complete team of players from different clubs. Every player is assigned some pre-decided valuation and subject to this, the total value of the team can’t exceed £100 million. The selected team earns points according to the performance of each player in the following game. After every game, a free transfer of any player is allowed to every user. For eg. a player scoring a goal, goalkeeper saving several attempts on goal etc. result in more points for the particular player.

Problem and Data:-  The aim is to access a given team and predict the number of points a team scores by summing the expected points of each player according to different dependent variables. This would give a prior knowledge of the performance of a player which can be used to decide which player to transfer out.
Four different kinds of players and the metrics through which they earn points(positive or negative) is described below:-
Strikers:- Goals, Assists,  Minutes played, Yellow cards.
Midfielders:- Goals, Assists, Minutes played, Clean sheet, Yellow cards, Red cards.
Defenders:- Goals, Assists, Minutes played, Clean sheet, Yellow cards, Red cards.
Goalkeepers:- Number of Saves and Clean Sheet  
3/2/1 bonus points are awarded to the top 3 performers of a particular game. It is very difficult to predict who would be the best performers in a match because of the dependence of other players. Thus the performance of all the 21(11+10) players other than the one under scrutiny is difficult to capture.

Below are the definitions of the data sets that we have used for this model:
Influence: It is evaluated the degree to which that player has made an impact on a single match or throughout the season. It takes account of events and activities that could directly or indirectly affect the outcome of the fixture.
Fixture Difficulty: The FD provides an immediate view of the difficulty of forthcoming fixtures for your players. It is based on a complex algorithm that analyses the performance statistics for each team across their home and away matches
Creativity: It evaluates player performance in terms of producing goalscoring chances for others. It is used as a data set to identify the players most likely to supply assists.
Threat: It will produce a value that examines a player’s threat on goal. It determines the individual most likely to score goals. 
Form: Form is a player’s average score per match, calculated from all matches played by his club in 5 game weeks.
Key Pass: A key pass is defined as the final pass or pass-cum-shot leading to the recipient of the ball having an attempt at goal without scoring.
Chances created: A situation where a player should reasonably be expected to score usually in a one-on-one scenario or from very close range
Clean Sheet: It means a team prevent their opponents from scoring any goals during an entire match.

Analysis and results:

Overall points on a player are based on a few of the major factors for each ( factors reduced for simplicity). Following are the key factors (independent variables) for different point contributors for a player.
 
Goals: Form, Fixture Difficulty, Threat, Minutes

Assists: Form, Fixture Difficulty, Key Passes, Creativity, Influence, Minutes

Clean Sheets: Form, Fixture Difficulty, Minutes, Influence

Yellow Cards: fixture difficulty, tackles, fouls, goals conceded, minutes

Saves: Fixture, form, goals conceded,  minutes, influence

Minutes: Minutes played by the players have been assumed as complete 90 because the players who are regular players for their respective teams for maximum availability of data. Moreover, minutes played by players is highly dependent on mid-week game fixtures of other competitions, data of which is not available in such depth. Thus maximum points for minutes played have been assumed. 


Now the above-mentioned factors help us in predicting the dependent variable which in turn would give us the total points scored, that is the total performance of that particular individual 

The below-mentioned charts give us the weight of each of the independent parameter in predicting the dependent parameter


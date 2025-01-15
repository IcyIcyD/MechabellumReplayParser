<h1>Mechabellum Replay Parser</h1>
<br>Hi there! This is a small for-fun project that parses replays from game Mechabellum by Game River.
<br>Code quality may be poor in some places, this project never meant to go public and was abandoned half-way through development due to inability to find any useful implications. If there is a demand, I may finish this and make project more coherent (like adding <i>argparser</i> instead of manually butchering main method).

<br><h2>Some theory</h2>
<br>In Mechabellum, replay file is a xml file with some additions. These additions are cut off in "get_model" method. <b>This xml file is a history of user inputs, proceeded by game.</b> This means:
<br><ol><li> NO WINRATE. It is impossible to get information "who won the game" by just parsing xml file. Therefore, to predict who won the game we have to either code entire Mechabellum game or get a lot, and I mean A LOT of info about winrates (from where?) to create some sort of prediction mechanism based on that data, which also can vary from patch to patch.
<li> NO CHEATING. It is impossible to get info in real time, meaning that this project would not give you or any other player any reasonable advantages amongst other players. I am strongly against cheating and discourage anyone to do not-fair play.
<li> ONLY DISCRETE DATA. Some features are basically impossible to get from replay file, for example, any spell impact. File has time and coordinates of spell usage, but what that spell actually did in such round is unknown. Same is true for AoE unit abilities, shields, missiles and anti-missile devices and techs.</li>
<li> SURVIVOR'S MISTAKE. Replay file has only user inputs, meaning that everything that was discraded by player is not a part of a replay file.</li>
</ol>
<br><h2>How to use it</h2>
<br>To get some data from lots of replays, you have to, well, have a lot of replays. What I do personally is I go for "Tournament" in-game tab and manually get all replays, since this is most accessible and high-quality data available at the moment.
<br>When you get a lot of replays, copypaste them into ./replays folder (create such folder if it does not exist), or you can also change <b>REPLAYS_PATH</b> constant.
<br>Then you ... well... do anything with it, really. Change main method however you want, run it and get some data in output_string.
<br>Right now main method collects statistics about unit drops. And commented code collects player's choices of techs, for example, "how many people brought Ignite on Wasps".
<br>
<br>Example output for unit drops (this is currently what main method does):

```
ROUND 2

1x level 1 Scorpion. Count: 44 
1x level 2 Phoenix. Count: 44 
1x level 2 Phantom Ray. Count: 43 
1x level 2 Sabertooth. Count: 28 
1x level 1 Typhoon. Count: 27 
1x level 2 Wasp. Count: 27 
1x level 1 Farseer. Count: 24 
1x level 2 Rhino. Count: 24 
1x level 2 Mustang. Count: 23 
1x level 2 Fire Badger. Count: 19 
2x level 2 Marksmen. Count: 16 
3x level 1 Marksmen. Count: 15 
3x level 1 Arclight. Count: 13 
1x level 2 Sledgehammer. Count: 11 
1x level 2 Stormcaller. Count: 10 
3x level 1 Fang. Count: 10 
1x level 2 Steel Ball. Count: 9 
1x level 1 Wraith. Count: 9 
2x level 2 Fang. Count: 7 
2x level 2 Arclight. Count: 4 
2x level 3 Fang. Count: 4 
2x level 3 Crawler. Count: 3 
1x level 2 Tarantula. Count: 3 
3x level 1 Crawler. Count: 1 
```
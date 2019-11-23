# mcts_improve

Improve the MCTS by NN, NEC, EVA.

## Structure of project
- `mian.py` Main file for training.
    - The `checkpoint` in `args` is the file that store all the trainning data including best one. Please add this folder in `.gitignore` as you push. Thanks!
- `play.py` Play the game in two players by using the NN trained in each iteration (including rejected ones).
- `plot.py` Plot the final plots, need at least one arg for this to run, see `run.sh` for examples.
- `othello` The directory with game info inside*.
- `Coach.py` The class do the self play and learning*.
- `Arena.py` The class make two player pit with each other*.
- `Game.py` The base Class of game*.
- `NeuralNet.py` The base Class of neural net for game*.
- `20_6Othello` File with all results of 6*6 Othello game in 20 iterations.
- `run.sh` The example run bash.
- `utils.py` Some useful functions*.
   

## Running
When you try to run, the varibale you can change are:
- All the variable in `args` in `main.py`, `play.py`.
    - The `checkpoint` in `main.py` and `play.py` must match for the players to use proper NN. 
- The game could be 6\*6 or 8\*8.
```
python3 main.py # > outputfile
```
or
```
./run.sh
```

## Next steps
Van 
- Run 8\*8 Othello games
- Run Vanilla MCTS with UCT and NN

## Contributing
**TODO**

## Authors

* **Fan Shen** - *Initial work* - [VVVVVan](https://github.com/VVVVVan)
* **Yuju Lee** - Please add your info
* **Audrina Zhou** - Please add your info

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* **TODO**


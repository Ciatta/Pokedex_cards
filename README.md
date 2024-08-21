# Pokedex_cards

A simple script is created to organize Pokemon cards in Pokedex order. </br>
For each Pokemon, the script finds its Pokedex number, page number, and position based on pages with 9 sleeves on each face (a page can contain 18 different Pokemon).

# Dependecies
- PyPokedex module
```
!pip install git+https://github.com/arnavb/pypokedex.git@master
```

# Usage
- Determine the page size, which indicates the maximum number of different Pokemon the page can hold.
  ```
   size = 18
  ``` 
- Add the cards that need to be sorted by their name or Pokedex number to the respective list.
  ```
  name_list = ['numel', 'darumaka', 'hypno']
  dex_list = [344, 994, 38]
  ```
- The script will then identify the Pokemon number, name, the page it should be placed on, and its position.
- It will organize the Pokemon in a dictionary and save the digital Pokedex to a file.
- Every time the script is run, it will load the Pokedex from the file.

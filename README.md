# openscad-board-maker
CLI script to generate openscad data for rectangular PCBs

## Usage

The script requires the solidpython module. This module can be installed by pip but does not appear to correctly install all its dependencies, so instead pull it from [Github](https:// github.com/SolidCode/SolidPython) and install using setup.py.

To use the scipt, just run giving it the width and height of your board:

```
openscad-board-maker.py 60 37
```

 You get a [Sick of Beige](http://dangerousprototypes.com/docs/Sick_of_Beige_compatible_cases) style board with 4mm rounded corners and 3mm fixing holes.
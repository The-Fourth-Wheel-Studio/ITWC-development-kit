# <img src="../image//component//abilitiesComponent.png" width = "30"> Abilities

## How to use

don't touch this one, just extend it and write your own code into the [doWhatever]() function

see all shared [abilities]()

## Attributes

### active : bool 

By default, set to false. if true [doWhatever]() will be called when [execute](abilitiesManager.md#execute---none) is called.

### player : Player

don't touch this one, he's automaticly set to the [GameManager.player]() value.

### Methods

- #### doWhatever

    - ##### Parameters
        This is where the only limit is your imagination ! overwrite this function as you please to do.. whatever, this function is called by the [abilitiesManager](abilitiesManager.md) when execute is called.

        - ###### delta
            see [delta](https://docs.godotengine.org/en/stable/tutorials/scripting/idle_and_physics_processing.html)
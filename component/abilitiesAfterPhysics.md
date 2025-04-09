# <img src="../image//component//abilitiesAfterPhysicsComponent.png" width = "30"> Abilities After Physics

## How to use

it's a littler bit like an [abilities](./abilities.md) but called after the move_and_slide() func of the player

don't touch this one, just extend it and write your own code into the [doWhatever]() function


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
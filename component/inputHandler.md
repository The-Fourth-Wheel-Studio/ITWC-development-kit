# <img src="../image/component/inputHandler.png" width = "30"> Input handler

## How to use

InputHandler is use to gather all input from the user that you can access through exported boolean, unfortunalty this component isn't very usefull because all gathered input are hardcoded. But you have the possibility to create some constraint between input.

this component is pretty straigth forward, you have @export boolean that translate the state of some input and you can access them by doing 
```gdscript
inputHandler.theBooleanYouWantToAccess
```
[see the list of every boolean here](#attributes)

## Attributes

- asJump : bool, store ```Input.is_action_pressed("jump")```
    
- isSprinting : bool, store ```Input.is_action_pressed("sprint")```

- direction : Vector2, store ```Input.get_vector("left", "right", "up", "down")```

- leftClick : bool, store ```Input.is_action_pressed("left_click")```

- isCrouch : bool, store ```Input.is_action_pressed("crouch")```

- constraint : Dictionary[String], the dictionary to handle constraint, set a key with the name of the first variable and in value set the name of the second variable, and the second variable will by overwrite like so : ```Common.xor(second var, first var)``` (see [Common]())

## Methods 

- ### gather -> none
    when called, this function set all boolean to there respective Input state, and apply constraint
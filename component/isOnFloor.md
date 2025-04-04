# <img src="../image/component/isOnFloorComponent.png" width = 30> Is On Floor

## How to use

Is on floor is basicly a component that give you a better is_on_floor function, this component provide a function called isOnFloorImprove that return true of false depending if the testing body is on floor or not.

This component also handle coyote time with two function : isCoyoteTime and resetCoyote

you can also use this component to snap object on floor with the betterSnap function.

## Attributes

- ### NodeToCheck : variant
     the object to check

- ### lenght : float
    the lenght of the raycast, the raycast is use to check if the checked object is just about to put is little feet on the ground

- ### raycast : raycast3D
     tho we have the length of the ray we need a actual ray and i look like you'r at the perfect place !

- ### coyoteTimer : timer
     coyote time need a timer, just put a timer as a child

- ### coyoteTime : float
    the actual coyote time in second

- ### wasOnFloor : bool
    store if the checked object was on floor last frame

## Methods

- ### isOnFloorImprove -> bool
    return if the checked object is on floor or bearly on floor

- ### isCoyoteTime -> bool 
    return if the coyote timer is active, use for exemple in the jump of the player. (yeah i didn't really know where to put this)

- ### resetCoyote -> none 
    reset the coyote timer (beep beep)

- ### betterSnap -> none 
    snap the checked object on the ground
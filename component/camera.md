# <img src="../image/component/cameraComponent.png" width="30"> Camera Component

cinemachine for godot :)

## how to use

you won't have to touch this component. But if you do good luck.

## Attributes

- currentCameraZone : [cameraZone](), set to the cameraZone where the player is by the [GameManager]()



- ### deadZoneCoordinates : Vector4
    a vec4 composed by 2 vec2 representing the coordinates of two point, the two point are the two corner of a rectangle, coordinate are beetween 0 and 1 and represent the proportion on screen 
\
    /!\ Dead zone variable aren't use anymore but still here because cleaning is time consuming

- ### cameraDeadZoneSpeed : float
    the speed of the camera when the player exit the dead zone
\
/!\ Dead zone variable aren't use anymore but still here because cleaning is time consuming

- ### normalFOV : float
    the FOV of the camera in a totaly normal situation

- ### fovVariation : float
    the FOV value that will be added to the normalFOV

- ### cameraRot : float
    set to ```self.rotation_degrees.y```

- ### references : Vector4
    composition of two vec2 representing the x and y transformation vector

## Methods

- ### ifObjectIsInDeadZone -> bool
    return if the object given in parameter is in the dead zone

    - #### parameter

        - ##### object : Node3D
            the object to check

- ### ifObjectIsCentered -> bool
    return true if the object is approximatly at the center of the screen, the function was definitly wrote by chatgpt tho

    - #### parameter

        - ##### object : Node3D
            the object to check

- ### getOnScreenObjectCoord -> Vector2
    return the object position on screen

    basicly : ```return self.unproject_position(object.global_position)```

    - #### parameter

        - ##### object : Node3D
            the object to check

- ### getNewReference -> none
    set the current cameraRot and reference to [NewReference(cameraRot)]()

    basicly : ```return self.unproject_position(object.global_position)```


- ### getProjectionVector -> Vector2
    rotate a vector ??? honestly idk what this one is but i think it's usefull '^^
    fell free to understand what it does
    ```
    var angleRad = deg_to_rad(angle)

	var x : float = curVec.x * cos(angleRad) + curVec.y * sin(angleRad)
	var y : float = - curVec.x * sin(angleRad) + curVec.y * cos(angleRad)
	return Vector2(x, y)
    ```

    - #### parameter

        - ##### curVec : Vector2

            the vector to rotate i guess 
        - ##### angle : float
            rotation need an angle so here it is

- ### NewReference -> Vector4
    ok big one, return a vector4 containing two vector2, so you can convert an x and y movement to a new reference :

    <img src="../image/explain/reference.png">
    
    - #### parameter

        - ##### angle : float
            the angle in degree

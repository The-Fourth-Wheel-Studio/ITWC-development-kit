# Component

Component are very important if you want to create anything in ITWC, there are basicly custom node that you can drag and drop in a specific order to create easly any object in the game.

## Player Component

player component are the component specific to the player, you won't use them very often unless you want to modify or create custom player.

- ### <img src="image/component/velocityComponent.png" width = "25"> [velocity component](component/velocityComponent.md)

**class name : ```velocityComponent``` </code>**

the velocity component handle... velocity ! who would have guess that... anyway this component allow you to do operation on velocity and get a final velocity after all your point mechanics

- ### <img src="image/component/inputHandler.png" width = "25" width = "25"> [input handler](./component//inputHandler.md)

**class name : ```inputHandler``` </code>**

the input handler is kinda useless, it's more a remnant of IDWN, basicly he gather all input (hardcoded) and set boolean for each input that you can access. the only advantage of this component is that you have the possibility to block certain combination of input

- ### <img src="image/component/repulseHandler.png" width="25"> [repulse handler](./component/repulseHandler.md)

**class name : ```repulseHandler``` </code>**

repulse handler is basicly a component that allow you to push player back, very usefull if you have the covid-19

- ### <img src="image/component/repulseHandlerZone.png" width="25"> [repulse handler zone](/component/repulseHandlerZone.md)

**class name : ```repulseHandlerZone``` </code>**

repulse handler zone is not very important, it's just a component to set a collision shape to a repulse handler, he use to have some kind of behavior but not anymore he's just here...

- ### <img src="image/component/abilitiesManager.png" width="25"> abilities manager

**class name : ```abilitiesManager```**

this component manage abilities (see, i'm not good at computer science but i can give good name (spoiler : i will name my children with number)) you can drag and drop any [ability component](#abilities) and he will execute them for you automaticly no need to do complicated setup ! (finally a good use of components)

- ### <img src="image/component/abilitiesComponent.png" width="25"> abilities

**class name : ```abilities```**

abilities is litterally nothing but an empty function, you can extend this class and write code in this function and when the ability is place in a [abilitiesManager](#abilities-manager) the function will be called.

- ### <img src="image/component/isOnFloorComponent.png" width="25"> is on floor component

**class name : ```isOneFloorComponent```**

is on floor component provide a better version of the is_on_floor() godot's built-in method.
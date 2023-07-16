## ICE 1 - Hurdle 3
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# def take_diversion():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
    
# while( not at_goal()):
#    if( not wall_in_front()):
#     move()
#    else:
#     take_diversion()
    

## Hurdle 4
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# def take_diversion():
#     count = 1
#     turn_left()
#     move()
#     while wall_on_right():
#         move()
#         count +=1
#     turn_right()
#     move()
#     turn_right()
#     for i in range(count):
#         move()
#     turn_left()
    
# while( not at_goal()):
#    if( not wall_in_front()):
#     move()
#    else:
#     take_diversion()
## This code can also be improved using the front is clear() function

# #Final Project:
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# while front_is_clear():
#     move()
    
# while not at_goal():
#     if not wall_on_right():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()
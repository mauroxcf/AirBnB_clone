# AirBnB_clone
![65f4a1dd9c51265f49d0 (1)](https://user-images.githubusercontent.com/66022141/98313272-76e75580-1fa1-11eb-8dd7-1ec74e985c09.png)
For this first part of the project, a command interpreter has been created using the Python programming language in order to be able to manage the objects of this project more easily in the following Airbnb_clone projects.

### What does?
With this console we can create, view, delete and update objects the objects will be saved in a json file to guarantee their persistence in each execution of the program

### Requirements and how to use?
- Have Python installed. (preferably version 3)
- Execute `console.py` file to start the console
```python
$ ./console
(hbnb)
```
#### **Commands**
- Create :heavy_plus_sign:
```python
(hbnb) create BaseModel       ->   Create a object. syntax : create <class name>
# output:
49faff9a-6318-451f-87b6-910505c55907
```
- Show :clipboard:
```python
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907      ->   show all the info of the object by the class name and ID. syntax : show <class name> <ID>
# output:
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'updated_at': datetime.datetime(2020, 11, 5, 20, 14, 23, 490068), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2020, 11, 5, 20, 14, 23, 490036)}
```
- All :mag_right:
```python
(hbnb) all BaseModel      ->   show all the info of the object class name. syntax : all <class name>
# output:
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'updated_at': datetime.datetime(2020, 11, 5, 20, 14, 23, 490068), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2020, 11, 5, 20, 14, 23, 490036)}"]
```
- Update :floppy_disk:
```python
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"    ->   update the object by adding a new atribbute and value of this. syntax : update <class name> <ID> <attribute> <attribute value>
(hbnb) 
(hbnb) 
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907      ->   show all the info of the object by the class name and ID. syntax : show <class name> <ID>
# output:
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'updated_at': datetime.datetime(2020, 11, 5, 20, 14, 23, 490068), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2020, 11, 5, 20, 14, 23, 490036)}
```
- Destroy :boom:
```python
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907      ->   destroy all the info of the object by. syntax : destroy <class name> <ID>
```
- Help :question:
```python
(hbnb) help create      ->   display info about the command. syntax : help <command>
# output:
Creates a object, saves it to the JSON file and prints the id
```
- Quit :x:
```python
(hbnb) quit or EOF      ->   exit the program.
```


## Made by
**Francisco Guzmán** - Twitter [@I7RANKI](https://twitter.com/I7RANKI) - Github [I7RANKI](https://github.com/I7RANK) :snake: :guitar:  
**Mauricio Contreras** - Twitter [@MauroJCF](https://twitter.com/MauroJCF) - Github [mauroxcf](https://github.com/mauroxcf) :snake:

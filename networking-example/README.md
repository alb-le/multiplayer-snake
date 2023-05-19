# Networking example for game development

### How to run

1. Install the necessary dependencies (preferably on a virtual environment):
```
(your_env) $ pip install pygame 
```
2. Before running the necessary scripts, change the IP ADDRESS on both files server.py...
![0](img/server.png)

and network.py:
![1](img/network.png)

The IP can be found with the following command:
![2](img/ipconfig.png)
3. Run the server script:
```
(your_env) $ python server.py
```
4. Run the first client on a terminal (or cmd):
```
(your_env) $ python client.py
```
5. Run the second client on another terminal (or cmd):
```
(your_env) $ python client.py
```

You should see two game windows, each one for a client:
![3](img/two-windows.png)

Try to move a square from each window and see the results!

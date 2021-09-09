# While Detect
## Feature
Detect while for c/c++.

## How to use
* Method 1
```bash
chmod a+x while_detect.py
./while_detect.py ex.c
```
* Method 2 - Single file
```bash
python3 ./while_detect.py ex.c
```
* Method 3 - Multi file
```bash
python3 ./while_detect.py *.c
```

## Example output
```shell
Argv has ['while_detect.py', 'ex.c']
Curret file is ex.c

-------------------------------

In file 'ex.c'
Start index is 59 (0x3b)
Start line is 5
ex.c : 5
5: 	while (1) {
6: 		if (1 == 0) {
7: 			printf("GG\n");
8: 		}
9: 		while (0) {
10: 			;
11: 		}
12: 	}

-------------------------------

In file 'ex.c'
Start index is 111 (0x6f)
Start line is 9
ex.c : 9
9: 		while (0) {
10: 			;
11: 		}

-------------------------------

In file 'ex.c'
Start index is 170 (0xaa)
Start line is 18
ex.c : 18
18: 	while (a++ < 10) {
19: 		;
20: 	}

-------------------------------

ex.c is done.

-------------------------------
```

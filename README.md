<h1>How does this work?</h1>
<p>This works by having the encrypter run, and encrypt all of the files. Then, once you get whatever you want from the target, you give them the decrypter. After they run that, it will decrypt all of their files. When this happens, a file title instructions.txt will drop once the encrypter runs. This carries all of the info you wish to give to the target.</p>
<h1>Behavior of the Ransomware</h1>
<p>This is a pretty simple script, but also very effective. The steps are as follows: </p>
<p>1. Encrypter.py runs, encrypts all files <br>2. it then Drops intrusctions.txt & ID.id <br>3. The file then kills itself<br>4.When you bring in decrypter.py and run it, it decrypts the files<br>5. It then kills ID.id, and any script excesse<br>6. It then kills itself.</p>
<h1>Warnings!</h1>
<p>Don't run the encrypter with the decrypter near it, it will encrypt it. Then you lose your stuff. Womp Womp ig.</p>
<p>Don't mess with the ID.id file. If this gets messed up at all, say goodbye to your files. They are never coming back.</p>
<p>Don't encrypt the files many times. The stuff doesn't stack, it only just double knots it. When you encrypt it multiple times, you lose the last ID. Every time it overwrites any ID near it, and you've lost the first layer's ability to be fixed.</p>
<h1>How to change Ransom Note?</h1>
<p>Go to "encrypter.py" and the first line you should see this:</p>
```python
instructions = "Bring me thy bitcoin"
```
<p>The part in the quetation marks, (Bring me thy bitcoin) is the part you change. Doing this changes the text in the file that the encrypter drops. You can type \\n in the text to start a new line.</p>
<h1>What does TeeHee.py do?</h1>
<p>💣 TeeHee >;3 💣</p>

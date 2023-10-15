## Fichiers SRT vers fichiers TXT.
Petit outil personnel pour traiter automatiquement les srt des moocs.

Converti les fichiers srt en fichiers txt. Un par un ou en lot.

Sans:
* Les ID.
* Le time code.
* Les sauts de lignes.
* Les lignes vides.

### Utilisation en ligne de commande.

Deux options,
* -f pour traiter un fichier
* -d pour un dossier

Si aucune option n'est utilisée, c'est le dossier dans lequel se trouve le programme qui est traiter.

Les fichiers originaux ne sont pas effacés.  
Les nouveaux fichiers sont créés dans le même dossier que l'original.

### Exemples:
#### Fichiers
Si le programme est dans le même dossier que le fichier. 

### in:
* ```python
  python srt_to_txt.py -f course_1.srt
  ```
### out:
* ```python
  course_1.txt
  ```

Si le programme est dans un autre dossier, à partir du dossier contenant le programme entrer le chemin absolu.

### in:
* ```python
  python srt_to_txt.py -f c:\mooc\course_1.srt
  ```
### out:
* ```python
  c:\mooc\course_1.txt
  ```
#### Dossiers

Si le dossier dans lequel se trouve le programme contient:
* course_1.srt
* course_2.srt
* course_3.srt

### in:
* ```python
  python srt_to_txt.py
  ```
### out:
* ```python
  course_1.txt
  course_2.txt
  course_3.txt
  ```

Si le programme est dans un autre dossier, à partir du dossier contenant le programme entrer le chemin absolu avec l'option -d.

### in:
* ```python
  python srt_to_txt.py -d c:\mooc
  ```
### out:
* ```python
  course_1.txt
  course_2.txt
  course_3.txt
  ```
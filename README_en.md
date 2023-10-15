 ## SRT files to TXT files. 
 Small personal tool for automatically processing mooc srt.  
 Works with Windows and Linux. Not tested with Apple.

Converts srt files into txt files. One by one or in batch.

Without:

* IDs.
* Time code.
* Line breaks.
* Blank lines.


### Command-line operation.

Two options,
* -f to process a file
* -d to process a folder

If no option is used, the folder in which the program is located is processed.

Original files are not deleted.  
New files are created in the same folder as the original.

### Exa4ples:
#### Files
If the program is in the same folder as the file. 

### in:
* ```python
  python srt_to_txt.py -f course_1.srt
  ```
### out:
* ```python
  course_1.txt
  ```

If the program is in another folder, start from the folder containing the program and enter the absolute path.

### in:
* ```python
  python srt_to_txt.py -f c:\mooc\course_1.srt
  ```
### out:
* ```python
  c:\mooc\course_1.txt
  ```
#### Dossiers

If the folder in which the program is located contains:
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

If the program is in another folder, from the folder containing the program enter the absolute path with the -d option.

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
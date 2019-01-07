## 2. Manipulating files

**INDEX**

2.1 Redirecting and appending

2.2 Listing

2.3 Renaming, copying, deleting

2.4 Summary

> 기본적으로 텍스트 에디터 활용에 대한 기술적인 조건을 전제로 하지 않는다.
>
> 순수 CLI Commands 로 파일을 다뤄본다.

---

### 2.1 Redirceting and appending

우선 문자열 한줄을 출력해보자.

```shell
$ echo "Someone Like You"
Someone Like You
```

그리고 해당 문자열을 포함하는 파일을 만들어 보자. (파일명은 `adele.txt`)

```shell
$ echo "Someone Like You" > adele.txt
```

- **`>` : redirect operator**
  - `$ echo` 문자열 출력을 가져와서 그 내용을 호출된 파일(`adele.txt`)로 redirect(전송, 보내다) 한다.

---

정말 우리가 원하는 대로 동작했는지 어떻게 알 수 있을까?

추후에 파일을 검사할 수 있는 고급 명령을 배우겠지만,

지금 단계에서는 일단 단순히 해당 파일의 내용을 터미널 창에 보여주는 명령어를 사용해 보자.

```shell
$ cat adele.txt
Someone Like You
```

* **`$ cat` : 단순히 파일의 내용을 화면에 보여준다.** (simply dumps the contents of the file to the screen)
  * *con**cat**ate (연쇄상의, 사슬처럼 잇다, 연결된)*
  * `$ cat ` 은 여러 파일의 내용을 결합하는 데 사용할 수 있다. (be used to combine the contents of multiple files)
  * 하지만 지금은 우선 `$ cat` 은 빠르고 지저분하게("quick-and-dirty") 특정 파일의 내용을 보여주는 방법으로 생각하자.

---

이번에는 `adele.txt `2번째 줄에 추가로 내용을 삽입해보자.

```shell
$ echo "Rolling in the deep" >> adele.txt
```

- **`>>` : append operator**
  - `$ echo` 문자열 출력을 가져와서 그 내용을 호출된 파일(`adele.txt`)로 append(덧붙이는, 첨가하다) 한다.
  - 만약 `>` 를 사용하게 되면 해당 파일에 출력내용을 덮어 쓰게 된다. 즉 기존의 내용은 날아간다.

```bash
$ cat adele.txt
Someone Like You
Roliing in the deep
```

---

- `diff`
  - 유사하지만 동일하지 않은 파일의 비교를 용이하게하기 위해 사용한다.

```bash
$ echo "someone like you" > adele_2.txt
$ echo "rolling in the deep" >> adele_2.txt
```

```bash
$ diff adele.txt adele_2.txt
< Someone Like You
< Roliing in the deep
---
> someone like you
> rolling in the deep
```

#### 2.1.1 Exercises

1. `echo` 와 `>` 를 사용하여,  좋아하는 노래제목을 영어로 한줄씩 각각 `line_1.txt` 와 `line_2.txt` 로 만든다.

> ```bash
> $ echo "foofoo" > line_1.txt
> $ echo "barbar" > line_2.txt
> ```

2.  `song.txt` 에 `line_1.txt` 와 `line_2.txt`의 내용을 넣는다.

> ```bash
> $ cat line_1.txt > song.txt
> $ cat line_2.txt >> song.txt
> ```

3. `cat` 을 사용하여 `song_reverse.txt` 파일을 만들고, 그 안에 각 `line_1.txt`와 `line_2.txt` 를 **거꾸로** 넣는 것을 **한줄의 명령** 으로 해본다.

> ```bash
> $ cat line_2.txt line_1.txt > song_reverse.txt
> ```

---

### 2.2 Listing

Unix 커맨드라인에서 가장 빈번하게 사용되는 명령어는 아마도 `ls` 이다. (short for "list")

```shell
$ ls 
Desktop
Document
Downloads
Library
adele.txt
```

* `ls` 는 단순히 (숨김파일을 제외하고) 현재 디렉토리(=폴더)에 있는 모든 파일과 디렉토리들을 보여준다.

또한 `ls`  는 파일(또는 디렉토리)이 존재하는지 확인하는 데 사용 될 수 있다.

```bash
$ ls foo
ls: foo: No such file or directory
```

> 보통 커맨드라인을 사용할 때 일반적인 패턴은 `cd` 로 디렉토리를 변경 한 다음 즉시 `ls` 를 이용해 현재 디렉토리의 내용을 보는 것이다.

---

유용한 기능들 중 하나는 `*` (wildcard character, star) 를 사용해 목록을 확인하는 것이다.

- 다음 명령어는 파일 확장자가 `.txt`  로 끝나는 모든 파일들을 보여준다.

```bash
$ ls *.txt
adele.txt   
adele_2.txt
```

* 여러가지 옵션들을 사용할 수 있다.

1. `ls -l` : long format 형식으로 보여주기.

```bash
$ ls -l
-rw-r--r--   1 junhokim  staff       0 Dec 29 16:04 adele.txt
-rw-r--r--   1 junhokim  staff       0 Dec 29 16:05 adele_2.txt
drwxr-xr-x   3 junhokim  staff      96 Dec 28 18:41 python101
```

```bash
$ ls -a # 숨김 파일까지 모두(all) 보여주기.

$ ls -t # 가장 최근에 수정된 순서(time) 로 보여주기.

$ ls -r # 역순(reverse)으로 보여주기.
```

---

2. `ls -rtl` : 파일이 변경된 시간을 역순으로 정렬해서 long format 형식으로 보여주기. *(list by **r**eversed **t**ime of modification (**l**ong format))*

* 이처럼 옵션들을 섞어서 사용할 수 있다.
  * **옵션들의 순서는 상관없다.** (`$ ls -rtl` == `$ ls -trl`)

```shell
$ ls -al # 모든(all) 파일을 long-format으로 보여주기.

$ ls -tla # 모든(all) 파일을 long-format 으로 가장 최근에 수정된 순서로 보여주기.
```

> 추가로  `-l` 옵션에서 long-format 이 보여주는 내용을 더 깊이 알고싶다면 [[ls -l explained]](https://www.garron.me/en/go2linux/ls-file-permissions.html) 를 참고하자.

---

* `-a` 옵션이 실제로 숨김파일을 출력해 주는지 보려면, 우선 숨김 파일을 만들어 보자 ( `touch`).

```shell
$ touch not_hidden.txt

$ touch .hidden.txt
```

* `$ touch` 명령어는 새로운 파일을 만든다. (디렉토리는 아님)
* Unix based OS 에서는 파일 혹은 디렉토리의 경우 이름 앞에 `.` 이 붙으면 숨김이다.
* `$ ls` 와 `$ls -a` 를 통해 비교해 보자.

#### 2.2.2 Exercises

1. 파일명이 "a" 로 시작되면 모든 파일 및 디렉토리(숨김파일 제외) 목록을 보는 명령어는 무엇인가.

> ```bash
> $ ls a*
> ```

2. 파일명에 "el" 문자열이 포함된 모든 파일 및 디렉토리(숨김파일 제외)를 파일이 변경된 시간을 역순으로 정렬해서 long format 으로 보는 명령어는 무엇인가.

> ```bash
> $ ls -rtl *el*
> ```

3. 모든 파일 및 디렉토리(숨김파일 포함)를 파일이 변경된 시간을 역순으로 정렬해서 long format 으로 보는 명령어는 무엇인가.

> ```bash
> ls -artl
> ```

---

### 2.3 Renaming, copying, deleting

1. `mv` : 이름바꾸기(move)

```shell
$ echo "test text" > test
$ ls test
$ mv test test_file.txt
$ ls 
test_file.txt
$ cat test_file.txt
test text
```

* `mv` 는 파일의 위치를 바꾸는 것도 가능하지만(현재 디렉토리 관련 내용을 배우지 않았기에), 일단은 Rename 기능만 소개한다.

---

2. `cp` : 복사하기(copy)

```shell
$ cp test_file.txt copy_file.txt
$ ls
test_file.txt
copy_file.txt
```

---

3. `rm` : 지우기(remove)

```shell
$ rm copy_file.txt
$ ls
test_file.txt
```

---

* **여기서부터 Tab(`⇥`) 키를 사용해 보도록 하면 좋을 듯 하다.**

* 이번에는 옵션과 함께 마찬가지로 `test_file.txt` 역시 지워보도록 하자.

```shell
$ rm -i te⇥
$ rm -i test_file.txt
remove test_file.txt? n
$ ls
test_file.txt
```

* 뒤의 파일 이름이 자동 완성된다. `⇥` 키는 직접 사용하면서 느끼는 게 가장 좋다. 비슷한 파일명이 있으면 두번 누르게 되면 목록이 뜨게 된다.
  * 파일명이 길어질수록 유용하게 쓸 수 있도록 하자.
* `-i` 옵션은 지우기 전에 확인을 받기위해 사용자에게 물어본다.
  * y 또는 Y 를 입력하고 enter 를 누르면 삭제가 진행되고 다른 모든 대답은 삭제를 진행하지 않는다.

* 이번에는 `n` 을 누르고 `enter` 이후 확인해 보면 지워지지 않음을 볼 수있다.

---

- `-f` 옵션은 반대로 어떠한 확인이나 절차를 모두 무시하고 강제로(force) 삭제하는 명령어 이다.

```bash
$ rm -f test_file.txt
```

>  정말 확실하지 않으면 사용을 자제하는 것이 좋다.

---

- `$ rm *.txt` 는 "확장자가 `.txt` 로 끝나는 모든 파일을 삭제하라"는 의미이다.

> ``` shell
> $ touch a.txt b.txt c.txt d.txt e.txt
> $ ls
> a.txt b.txt c.txt d.txt e.txt
> $ rm *.txt
> $ ls
> $
> ```
>

- **디렉토리의 삭제는 `rm` 혹은 `rm -f` 로 할 수 없다. 이후 디렉토리 관련 챕터에서 다룰 예정이다.**

---

#### 2.3.2 Exercises

1. 다음을 차례대로 해보자.
   1. `echo` 명령어와 redirect(`>`) 명령어를 사용하여, `"hello, world"`라는 텍스트를 담고있는 파일 `foo.txt` 를 생성한다. 
   2. 그리고 `cp` 명령어를 사용하여, `foo.txt` 를 복사한 `bar.txt` 를 만들자.
   3. (추가) `diff` 명령어를 사용하여 두 파일을 비교해보자. (manual page 를 이용해 보거나, `diff`명령어가 두가지 파일을 받아들일 수 있다는  사실을 활용해보자.)

   > ```bash
   > $ echo "hello, world" > foo.txt
   > $ cp foo.txt bar.txt
   > $ diff foo.txt bar.txt
   > ```

2. `cat` 과 `>` 을 사용하여, `foo.txt` 를 복사한 `baz.txt`를 만들자 (`cp` 사용 금지!)

> ```bash
> cat foo.txt > baz.txt
> ```

3. `rm nothing` 과 `rm -f nothing` 을 비교해보면 어떤가?

---

#### 번외: 왜 Unix 명령어는 이렇게 짧게 줄여 놨을까? (Unix commands, Y U NO LONGER?)

* `ls` 나 `mv` 같은 명령어는 `list` 나 `move` 같이 써도 될 것 같은데, 왜 외우기 힘들게 줄여놨을까? 
* 과거에는 인터넷 환경이 지금과 비교했을 때 좋지 않았다, 때문에 중앙 서버 컴퓨터와 사용자가 사용하는 컴퓨터를 연결하여 서버 컴퓨터를 조작할 때 사용자가 입력한 키가 실제 중앙 컴퓨터에 도달하는데 입력 지연(delay)이 상당했다. (즉 터미널에서 실제 `a`키를 입력하면 짧게는1초부터 길게는 몇 초까지의 지연 이후 화면에 `a`가 나타났다는 것.)
* 그래서 가장 많이 쓰이는 Unix 명령어들은 최대한 짧게 쓰게 된 것이다. 만약 `$ rm` 이 `$ remove` 였다면 3배, `$ ls` 가 `$ list` 였다면 2배의 추가 지연이 발생한다. (정말 가장 많이 쓰이는 명령어 중 이후에 배울 `$ cd` 는 `change directroy` 의 약자다.)

----

### 2.4 Summary

| Command          | Description                                         | Example                   |
| ---------------- | --------------------------------------------------- | ------------------------- |
| `>`              | 왼쪽의 출력물을 오른쪽의 파일로 Redirect(전송하기)  | `$ echo "foo" > foo.txt`  |
| `>>`             | 왼쪽의 출력물을 오른쪽의 파일로 Append(덧붙이기)    | `$ echo "bar" >> foo.txt` |
| `cat <file>`     | `<file>` 의 내용물을 화면에 출력                    | `$ cat foo.txt`           |
| `ls`             | 파일/디렉토리 들의 목록을 보여줌                    | `$ ls`                    |
| `ls <file>`      | `<file>` 만을 보여줌                                | `$ ls foo.txt`            |
| `ls -a`          | (숨김파일 포함) 모두 나열                           | `$ ls -a`                 |
| `ls -l`          | long-format 으로 나열                               | `$ ls -l`                 |
| `ls -alt`        | all 을 long-form 으로 수정한 시간 기준으로 나열     | `$ ls -alt`               |
| `touch <file>`   | 비어있는 `<file>` 생성                              | `$ touch foo`             |
| `mv <old> <new>` | `<old>` 의 이름을 `<new>`로 바꿈. (지금 단계에서는) | `$ mv foo bar`            |
| `cp <old> <new>` | `<old>` 를 `<new>` 이름으로 복사                    | `$ cp bar foo`            |
| `rm <file>`      | `<file>` 을 지운다.                                 | `$ rm foo`                |
| `rm -f <file>`   | `<file>` 을 강제(force)로 지운다.                   | `$ rm -f bar`             |


깃허브의 메인 브랜치 이름이 master에서 main으로 변경되었지만 git에서는 master가 메인 브랜치 이기 때문에 이름을 변경해주어야 합니다. 


PS D:\code\python_example> git branch

* master

현재 브랜치 이름은 master 입니다.


브랜치의 이름을 master에서 main으로 변경합니다.

PS D:\code\python_example> git branch -m master main

PS D:\code\python_example> git branch

* main

이제 브랜치 이름이 main 입니다. 



깃허브 저장소에 있는 내용을 로컬 저장소에 반영해주어야 합니다. 

이렇게 처음에 한번 해주어야 이후 정상적으로 로컬 repository의 파일을 깃허브 저장소에 업로드할 수 있습니다. 

 

git pull origin main --allow-unrelated-histories
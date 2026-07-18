# Resolución de conflictos

## Reseña: El flujo de trabajo «Pull-Merge-Push»
- Los siguientes códigos se encuentran en el vídeo de la lección:
```bash
atom all_checks.py

git add -p
git commit -m 'Rename min_absolute to min_gb, use parameter names'
git push
git pull
git log --graph --oneline --all
git log -p origin/master

atom all_checks.py
git add all_checks.py 
git commit
git push
git log --graph --oneline
```
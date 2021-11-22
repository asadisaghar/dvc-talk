# dvc-talk

Follow-along material for the Fagmandag at Inmeta-BAA, November 2021.

- Install dvc

      pip install dvc
      
- Initialize dvc 
    
      dvc init
      
- Add data/data.csv to dvc

      dvc add data/data.csv
      
  At this point you'll receive an Error that this file is already Git-tracked. Follow the intructions to remove it from Git and try again. This is to avoid potential issues with Authentication when pulling data from a dvc remote.
  
- Voilà! Now you can follow along everything else in the talk or [DVC documentation](https://dvc.org/doc)
  
![DVC cheatsheet](https://raw.githubusercontent.com/asadisaghar/dvc-talk/main/other/DVC_cheatsheet.webp )

<?php

$emp=array(
array(1,"sonu"),
array(2,"monu")
);




for ($row = 0; $row < 2; $row++) {  
  for ($col = 0; $col < 2; $col++) {  
    echo $emp[$row][$col]."  ";  
  }  
  echo "<br/>";  
} ?>
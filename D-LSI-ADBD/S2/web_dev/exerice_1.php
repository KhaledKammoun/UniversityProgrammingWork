// correction exercice 1 page 
<?php

$colors = ["red" ,"green"] ;
$color_index = array_rand($colors) ;
echo "Color : " . $colors[$color_index] ;
switch($colors[$color_index]) {
	case "red" : 
		echo "\nHello" ;
		break ;
	case "green" :
		echo "\nWelcome" ;
}